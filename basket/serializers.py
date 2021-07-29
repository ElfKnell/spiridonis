from rest_framework import serializers
from basket.models import Basket, Order, Selection
from product.serializers import ProductListCustomerSerializer, ProductListWholesalerSerializer, \
    ProductListRetailWholesalerSerializer, ProductListDropshipperSerializer
from users.serializers import CustomUserListSerializer


class BasketBaseSerializer:
    def get_product(self, obj):
        return obj.product.name_product

    def get_article(self, obj):
        return obj.product.article

    def get_photo(self, obj):
        return obj.product.photo

    def get_price(self, obj):
        if obj.user.role == 3:
            if obj.product.sale_price is None:
                return obj.product.price
            else:
                return obj.product.sale_price
        if obj.user.role == 4:
            return obj.product.opt_price
        if obj.user.role == 5:
            return obj.product.small_opt_price
        if obj.user.role == 6:
            return obj.product.drop_price


class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = '__all__'


class BasketCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = ['product', ]


# Детялі по кошику для різних покупців
class BasketDetailCustomerSerializer(serializers.ModelSerializer):
    product = ProductListCustomerSerializer(read_only=True)

    class Meta:
        model = Basket
        fields = ['product', 'count']


class BasketDetailWholesalerSerializer(serializers.ModelSerializer):
    product = ProductListWholesalerSerializer(read_only=True)

    class Meta:
        model = Basket
        fields = ['product', 'count']


class BasketDetailRetailWholesalerSerializer(serializers.ModelSerializer):
    product = ProductListRetailWholesalerSerializer(read_only=True)

    class Meta:
        model = Basket
        fields = ['product', 'count']


class BasketDetailDropshipperSerializer(serializers.ModelSerializer):
    product = ProductListDropshipperSerializer(read_only=True)

    class Meta:
        model = Basket
        fields = ['product', 'count']
# Кінець деталей по кошику


class OrderSerializer(serializers.ModelSerializer):

    basket = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_basket(self, obj):
        if obj.user.role == 3:
            queryset = obj.basket.all()
            return BasketDetailCustomerSerializer(queryset, many=True).data
        if obj.user.role == 4:
            queryset = obj.basket.all()
            return BasketDetailWholesalerSerializer(queryset, many=True).data
        if obj.user.role == 5:
            queryset = obj.basket.all()
            return BasketDetailRetailWholesalerSerializer(queryset, many=True).data
        if obj.user.role == 6:
            queryset = obj.basket.all()
            return BasketDetailDropshipperSerializer(queryset, many=True).data


# Деталі замовлень по користувачам
class OrderDetailCustomerSerializer(serializers.ModelSerializer):

    basket = BasketDetailCustomerSerializer(many=True, read_only=False)
    grand_total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_grand_total(self, obj):
        count = obj.basket.all().values_list('count', flat=True)
        price = obj.basket.all().values_list('product__price', flat=True)
        sale_price = obj.basket.all().values_list('product__sale_price', flat=True)

        list_price = []
        for i in list(price):
            list_price.append(float(i))

        list_sale_price = []
        for i in list(sale_price):
            if i is None:
                list_sale_price.append(0)
            else:
                list_sale_price.append(float(i))

        list_count = list(count)
        l_summa = []
        for i in range(len(list_count)):
            if list_sale_price[i] == 0:
                x = list_count[i] * list_price[i]
            else:
                x = list_count[i] * list_sale_price[i]
            l_summa.append(x)

        summa = round(sum(l_summa), 2)
        if sum(list_sale_price) == 0:
            sale = (100 - obj.sale) / 100
            summa_sale = round(summa * sale, 2)
            return summa_sale
        else:
            return summa


class OrderDetailWholesalerSerializer(serializers.ModelSerializer):

    basket = BasketDetailWholesalerSerializer(many=True, read_only=True)
    grand_total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_grand_total(self, obj):
        count = obj.basket.all().values_list('count', flat=True)
        price = obj.basket.all().values_list('product__opt_price', flat=True)

        list_price = []
        for i in list(price):
            list_price.append(float(i))

        list_count = list(count)
        l_summa = []
        for i in range(len(list_count)):
            x = list_count[i] * list_price[i]
            l_summa.append(x)

        summa = round(sum(l_summa), 2)
        return summa


class OrderDetailRetailWholesalerSerializer(serializers.ModelSerializer):

    basket = BasketDetailRetailWholesalerSerializer(many=True, read_only=True)
    grand_total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_grand_total(self, obj):
        count = obj.basket.all().values_list('count', flat=True)
        price = obj.basket.all().values_list('product__small_opt_price', flat=True)

        list_price = []
        for i in list(price):
            list_price.append(float(i))

        list_count = list(count)
        l_summa = []
        for i in range(len(list_count)):
            x = list_count[i] * list_price[i]
            l_summa.append(x)

        summa = round(sum(l_summa), 2)
        return summa


class OrderDetailDropshipperSerializer(serializers.ModelSerializer):

    basket = BasketDetailDropshipperSerializer(many=True, read_only=True)
    grand_total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_grand_total(self, obj):
        count = obj.basket.all().values_list('count', flat=True)
        price = obj.basket.all().values_list('product__drop_price', flat=True)

        list_price = []
        for i in list(price):
            list_price.append(float(i))

        list_count = list(count)
        l_summa = []
        for i in range(len(list_count)):
            x = list_count[i] * list_price[i]
            l_summa.append(x)

        summa = round(sum(l_summa), 2)
        return summa
# Кінець


class SelectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionListSerializer(serializers.ModelSerializer, BasketBaseSerializer):
    article = serializers.SerializerMethodField()
    product = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionDetailSerializer(serializers.ModelSerializer, BasketBaseSerializer):
    article = serializers.SerializerMethodField()
    product = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()

    class Meta:
        model = Selection
        fields = ['product', 'article', 'price', 'photo']
