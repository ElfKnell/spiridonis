from rest_framework import serializers
from basket.models import Basket, Order, Selection
from product.serializers import ProductListCustomerSerializer, ProductListWholesalerSerializer, \
    ProductListRetailWholesalerSerializer, ProductListDropshipperSerializer
from users.serializers import CustomUserListSerializer
from vproduct.serializers import VProductCustomerSerializer, VProductWholesalerSerializer, \
    VProductRetailWholesalerSerializer, VProductDropshipperSerializer


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
        fields = ['product', 'vproduct']


# Детялі по кошику для різних покупців
class BasketDetailCustomerSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    vproduct = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ['product', 'count', 'vproduct']

    def get_product(self, obj):
        if obj.product.is_variability:
            return obj.product.name_product
        else:
            return ProductListCustomerSerializer(obj.product, read_only=True).data

    def get_vproduct(self, obj):
        if obj.product.is_variability:
            return VProductCustomerSerializer(obj.vproduct, read_only=True).data
        else:
            return None


class BasketDetailWholesalerSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    vproduct = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ['product', 'count', 'vproduct']

    def get_product(self, obj):
        if obj.product.is_variability:
            return obj.product.name_product
        else:
            return ProductListWholesalerSerializer(obj.product, read_only=True).data

    def get_vproduct(self, obj):
        if obj.product.is_variability:
            return VProductWholesalerSerializer(obj.vproduct, read_only=True).data
        else:
            return None


class BasketDetailRetailWholesalerSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    vproduct = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ['product', 'count', 'vproduct']

    def get_product(self, obj):
        if obj.product.is_variability:
            return obj.product.name_product
        else:
            return ProductListRetailWholesalerSerializer(obj.product, read_only=True).data

    def get_vproduct(self, obj):
        if obj.product.is_variability:
            return VProductRetailWholesalerSerializer(obj.vproduct, read_only=True).data
        else:
            return None


class BasketDetailDropshipperSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    vproduct = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ['product', 'count', 'vproduct']

    def get_product(self, obj):
        if obj.product.is_variability:
            return obj.product.name_product
        else:
            return ProductListDropshipperSerializer(obj.product, read_only=True).data

    def get_vproduct(self, obj):
        if obj.product.is_variability:
            return VProductDropshipperSerializer(obj.vproduct, read_only=True).data
        else:
            return None
# Кінець деталей по кошику


# Замовлення
class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['number_order', 'basket', 'user', 'type_payment']


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
        price = list(obj.basket.all().values_list('product__price', flat=True))
        sale_price = list(obj.basket.all().values_list('product__sale_price', flat=True))
        is_variant = list(obj.basket.all().values_list('product__is_variability', flat=True))
        v_price = list(obj.basket.all().values_list('vproduct__price', flat=True))
        v_price_sale = list(obj.basket.all().values_list('vproduct__sale_price', flat=True))

        v_sum = []
        list_price = []
        list_sale_price = []
        for item in range(len(is_variant)):
            if is_variant[item]:
                list_price.append(0)
                list_sale_price.append(0)
                if v_price_sale[item] is None:
                    v_sum.append(float(v_price[item]))
                else:
                    v_sum.append(float(v_price_sale[item]))
            else:
                v_sum.append(0)
                if sale_price[item]:
                    list_sale_price.append(float(sale_price[item]))
                    list_price.append(0)
                else:
                    list_price.append(float(price[item]))
                    list_sale_price.append(0)

        list_count = list(count)
        l_summa = []
        for i in range(len(list_count)):
            if v_sum[i] != 0:
                x = list_count[i] * v_sum[i]
            else:
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
        is_variant = list(obj.basket.all().values_list('product__is_variability', flat=True))
        v_opt_price = list(obj.basket.all().values_list('vproduct__opt_price', flat=True))

        v_sum = []
        for item in range(len(is_variant)):
            if is_variant[item]:
                v_sum.append(float(v_opt_price[item]))
            else:
                v_sum.append(0)

        list_price = []
        for i in list(price):
            list_price.append(float(i))

        list_count = list(count)
        l_summa = []
        for i in range(len(list_count)):
            if v_sum[i] != 0:
                x = list_count[i] * v_sum[i]
            else:
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
        is_variant = list(obj.basket.all().values_list('product__is_variability', flat=True))
        v_small_opt_price = list(obj.basket.all().values_list('vproduct__small_opt_price', flat=True))

        v_sum = []
        for item in range(len(is_variant)):
            if is_variant[item]:
                v_sum.append(float(v_small_opt_price[item]))
            else:
                v_sum.append(0)

        list_price = []
        for i in list(price):
            list_price.append(float(i))

        list_count = list(count)
        l_summa = []
        for i in range(len(list_count)):
            if v_sum[i] != 0:
                x = list_count[i] * v_sum[i]
            else:
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
        is_variant = list(obj.basket.all().values_list('product__is_variability', flat=True))
        v_drop_price = list(obj.basket.all().values_list('vproduct__drop_price', flat=True))

        v_sum = []
        for item in range(len(is_variant)):
            if is_variant[item]:
                v_sum.append(float(v_drop_price[item]))
            else:
                v_sum.append(0)

        list_price = []
        for i in list(price):
            list_price.append(float(i))

        list_count = list(count)
        l_summa = []
        for i in range(len(list_count)):
            if v_sum[i] != 0:
                x = list_count[i] * v_sum[i]
            else:
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
