from rest_framework import serializers
from basket.models import Basket, Order, Selection
from product.serializers import ProductListCustomerSerializer, ProductListWholesalerSerializer, \
    ProductListRetailWholesalerSerializer, ProductListDropshipperSerializer, ProductUkListCustomerSerializer, \
    ProductRuListCustomerSerializer, ProductUkListWholesalerSerializer, ProductRuListWholesalerSerializer, \
    ProductUkListRetailWholesalerSerializer, ProductRuListRetailWholesalerSerializer, \
    ProductUkListDropshipperSerializer, ProductRuListDropshipperSerializer
from vproduct.serializers import VProductCustomerSerializer, VProductWholesalerSerializer, \
    VProductRetailWholesalerSerializer, VProductDropshipperSerializer


class SelectionEnBase:
    @staticmethod
    def get_product(obj):
        return obj.product.name_product


class SelectionUkBase:
    @staticmethod
    def get_product(obj):
        return obj.product.name_product_uk


class SelectionRuBase:
    @staticmethod
    def get_product(obj):
        return obj.product.name_product_ru


class BasketBaseSerializer:

    @staticmethod
    def get_article(obj):
        if obj.product.is_variability:
            return obj.vproduct.article
        else:
            return obj.product.article

    @staticmethod
    def get_photo(obj):
        photo = 'http://127.0.0.1:8000/media/' + str(obj.product.photo)
        return photo

    @staticmethod
    def get_price(obj):
        if obj.product.is_variability:

            if obj.user.role == 3:
                if obj.vproduct.sale_price is None:
                    return obj.vproduct.price
                else:
                    return obj.vproduct.sale_price
            if obj.user.role == 4:
                return obj.vproduct.opt_price
            if obj.user.role == 5:
                return obj.vproduct.small_opt_price
            if obj.user.role == 6:
                return obj.vproduct.drop_price
        else:
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
class BasketDetailCustomerBase:
    @staticmethod
    def get_vproduct(obj):
        if obj.product.is_variability:
            return VProductCustomerSerializer(obj.vproduct, read_only=True).data
        else:
            return None


class BasketDetailWholesalerBase:
    @staticmethod
    def get_vproduct(obj):
        if obj.product.is_variability:
            return VProductWholesalerSerializer(obj.vproduct, read_only=True).data
        else:
            return None


class BasketDetailRetailWholesalerBase:
    @staticmethod
    def get_vproduct(obj):
        if obj.product.is_variability:
            return VProductRetailWholesalerSerializer(obj.vproduct, read_only=True).data
        else:
            return None


class BasketDetailDropshipperSerializerBase:
    @staticmethod
    def get_vproduct(obj):
        if obj.product.is_variability:
            return VProductDropshipperSerializer(obj.vproduct, read_only=True).data
        else:
            return None


class BasketDetailCustomerSerializer(serializers.ModelSerializer, BasketDetailCustomerBase):
    product = serializers.SerializerMethodField()
    vproduct = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ['product', 'count', 'vproduct']

    @staticmethod
    def get_product(obj):
        if obj.product.is_variability:
            return obj.product.name_product
        else:
            return ProductListCustomerSerializer(obj.product, read_only=True).data


class BasketDetailUkCustomerSerializer(serializers.ModelSerializer, BasketDetailCustomerBase):
    product = serializers.SerializerMethodField()
    vproduct = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ['product', 'count', 'vproduct']

    @staticmethod
    def get_product(obj):
        if obj.product.is_variability:
            return obj.product.name_product_uk
        else:
            return ProductUkListCustomerSerializer(obj.product, read_only=True).data


class BasketDetailRuCustomerSerializer(serializers.ModelSerializer, BasketDetailCustomerBase):
    product = serializers.SerializerMethodField()
    vproduct = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ['product', 'count', 'vproduct']

    @staticmethod
    def get_product(obj):
        if obj.product.is_variability:
            return obj.product.name_product_ru
        else:
            return ProductRuListCustomerSerializer(obj.product, read_only=True).data


class BasketDetailWholesalerSerializer(serializers.ModelSerializer, BasketDetailWholesalerBase):
    product = serializers.SerializerMethodField()
    vproduct = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ['product', 'count', 'vproduct']

    @staticmethod
    def get_product(obj):
        if obj.product.is_variability:
            return obj.product.name_product
        else:
            return ProductListWholesalerSerializer(obj.product, read_only=True).data


class BasketDetailUkWholesalerSerializer(serializers.ModelSerializer, BasketDetailWholesalerBase):
    product = serializers.SerializerMethodField()
    vproduct = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ['product', 'count', 'vproduct']

    @staticmethod
    def get_product(obj):
        if obj.product.is_variability:
            return obj.product.name_product_uk
        else:
            return ProductUkListWholesalerSerializer(obj.product, read_only=True).data


class BasketDetailRuWholesalerSerializer(serializers.ModelSerializer, BasketDetailWholesalerBase):
    product = serializers.SerializerMethodField()
    vproduct = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ['product', 'count', 'vproduct']

    @staticmethod
    def get_product(obj):
        if obj.product.is_variability:
            return obj.product.name_product_ru
        else:
            return ProductRuListWholesalerSerializer(obj.product, read_only=True).data


class BasketDetailRetailWholesalerSerializer(serializers.ModelSerializer, BasketDetailRetailWholesalerBase):
    product = serializers.SerializerMethodField()
    vproduct = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ['product', 'count', 'vproduct']

    @staticmethod
    def get_product(obj):
        if obj.product.is_variability:
            return obj.product.name_product
        else:
            return ProductListRetailWholesalerSerializer(obj.product, read_only=True).data


class BasketDetailUkRetailWholesalerSerializer(serializers.ModelSerializer, BasketDetailRetailWholesalerBase):
    product = serializers.SerializerMethodField()
    vproduct = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ['product', 'count', 'vproduct']

    @staticmethod
    def get_product(obj):
        if obj.product.is_variability:
            return obj.product.name_product_uk
        else:
            return ProductUkListRetailWholesalerSerializer(obj.product, read_only=True).data


class BasketDetailRuRetailWholesalerSerializer(serializers.ModelSerializer, BasketDetailRetailWholesalerBase):
    product = serializers.SerializerMethodField()
    vproduct = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ['product', 'count', 'vproduct']

    @staticmethod
    def get_product(obj):
        if obj.product.is_variability:
            return obj.product.name_product_ru
        else:
            return ProductRuListRetailWholesalerSerializer(obj.product, read_only=True).data


class BasketDetailDropshipperSerializer(serializers.ModelSerializer, BasketDetailDropshipperSerializerBase):
    product = serializers.SerializerMethodField()
    vproduct = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ['product', 'count', 'vproduct']

    @staticmethod
    def get_product(obj):
        if obj.product.is_variability:
            return obj.product.name_product
        else:
            return ProductListDropshipperSerializer(obj.product, read_only=True).data


class BasketDetailUkDropshipperSerializer(serializers.ModelSerializer, BasketDetailDropshipperSerializerBase):
    product = serializers.SerializerMethodField()
    vproduct = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ['product', 'count', 'vproduct']

    @staticmethod
    def get_product(obj):
        if obj.product.is_variability:
            return obj.product.name_product_uk
        else:
            return ProductUkListDropshipperSerializer(obj.product, read_only=True).data


class BasketDetailRuDropshipperSerializer(serializers.ModelSerializer, BasketDetailDropshipperSerializerBase):
    product = serializers.SerializerMethodField()
    vproduct = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ['product', 'count', 'vproduct']

    @staticmethod
    def get_product(obj):
        if obj.product.is_variability:
            return obj.product.name_product_ru
        else:
            return ProductRuListDropshipperSerializer(obj.product, read_only=True).data
# Кінець деталей по кошику


# Замовлення
class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['number_order', 'basket', 'user', 'type_payment']


class OrderCreateUkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['number_order', 'basket', 'user', 'type_payment_uk']


class OrderCreateRuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['number_order', 'basket', 'user', 'type_payment_ru']


class OrderSerializer(serializers.ModelSerializer):

    basket = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    @staticmethod
    def get_basket(obj):
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
# Класи для обрахунку
class OrderDetailCustomBase:
    @staticmethod
    def get_grand_total(obj):
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


class OrderDetailWholesalerBase:
    @staticmethod
    def get_grand_total(obj):
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


class OrderDetailRetailWholesalerBase:
    @staticmethod
    def get_grand_total(obj):
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


class OrderDetailDropshipperBase:
    @staticmethod
    def get_grand_total(obj):
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
# Кінець класыв для обрахунку


class OrderDetailCustomerSerializer(serializers.ModelSerializer, OrderDetailCustomBase):

    basket = BasketDetailCustomerSerializer(many=True, read_only=False)
    grand_total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('basket', 'number_order', 'status', 'date_create', 'date_update', 'type_payment',
                  'user', 'sale', 'grand_total')


class OrderDetailCustomerUkSerializer(serializers.ModelSerializer, OrderDetailCustomBase):

    basket = BasketDetailUkCustomerSerializer(many=True, read_only=False)
    grand_total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('basket', 'number_order', 'status_uk', 'date_create', 'date_update', 'type_payment_uk',
                  'user', 'sale', 'grand_total')


class OrderDetailCustomerRuSerializer(serializers.ModelSerializer, OrderDetailCustomBase):

    basket = BasketDetailRuCustomerSerializer(many=True, read_only=False)
    grand_total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('basket', 'number_order', 'status_ru', 'date_create', 'date_update', 'type_payment_ru',
                  'user', 'sale', 'grand_total')


class OrderDetailWholesalerSerializer(serializers.ModelSerializer, OrderDetailWholesalerBase):

    basket = BasketDetailWholesalerSerializer(many=True, read_only=True)
    grand_total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('basket', 'number_order', 'status', 'date_create', 'date_update', 'type_payment',
                  'user', 'sale', 'grand_total')


class OrderDetailWholesalerUkSerializer(serializers.ModelSerializer, OrderDetailWholesalerBase):

    basket = BasketDetailUkWholesalerSerializer(many=True, read_only=True)
    grand_total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('basket', 'number_order', 'status_uk', 'date_create', 'date_update', 'type_payment_uk',
                  'user', 'sale', 'grand_total')


class OrderDetailWholesalerRuSerializer(serializers.ModelSerializer, OrderDetailWholesalerBase):

    basket = BasketDetailRuWholesalerSerializer(many=True, read_only=True)
    grand_total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('basket', 'number_order', 'status_ru', 'date_create', 'date_update', 'type_payment_ru',
                  'user', 'sale', 'grand_total')


class OrderDetailRetailWholesalerSerializer(serializers.ModelSerializer, OrderDetailRetailWholesalerBase):

    basket = BasketDetailRetailWholesalerSerializer(many=True, read_only=True)
    grand_total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('basket', 'number_order', 'status', 'date_create', 'date_update', 'type_payment',
                  'user', 'sale', 'grand_total')


class OrderDetailRetailWholesalerUkSerializer(serializers.ModelSerializer, OrderDetailRetailWholesalerBase):

    basket = BasketDetailUkRetailWholesalerSerializer(many=True, read_only=True)
    grand_total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('basket', 'number_order', 'status_uk', 'date_create', 'date_update', 'type_payment_uk',
                  'user', 'sale', 'grand_total')


class OrderDetailRetailWholesalerRuSerializer(serializers.ModelSerializer, OrderDetailRetailWholesalerBase):

    basket = BasketDetailRuRetailWholesalerSerializer(many=True, read_only=True)
    grand_total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('basket', 'number_order', 'status_ru', 'date_create', 'date_update', 'type_payment_ru',
                  'user', 'sale', 'grand_total')


class OrderDetailDropshipperSerializer(serializers.ModelSerializer, OrderDetailDropshipperBase):

    basket = BasketDetailDropshipperSerializer(many=True, read_only=True)
    grand_total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('basket', 'number_order', 'status', 'date_create', 'date_update', 'type_payment',
                  'user', 'sale', 'grand_total')


class OrderDetailDropshipperUkSerializer(serializers.ModelSerializer, OrderDetailDropshipperBase):

    basket = BasketDetailUkDropshipperSerializer(many=True, read_only=True)
    grand_total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('basket', 'number_order', 'status_uk', 'date_create', 'date_update', 'type_payment_uk',
                  'user', 'sale', 'grand_total')


class OrderDetailDropshipperRuSerializer(serializers.ModelSerializer, OrderDetailDropshipperBase):

    basket = BasketDetailRuDropshipperSerializer(many=True, read_only=True)
    grand_total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('basket', 'number_order', 'status_ru', 'date_create', 'date_update', 'type_payment_ru',
                  'user', 'sale', 'grand_total')
# Кінець


# Додавання в улюблені товари
class SelectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionListSerializer(serializers.ModelSerializer, BasketBaseSerializer, SelectionEnBase):
    article = serializers.SerializerMethodField()
    product = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionListUkSerializer(serializers.ModelSerializer, BasketBaseSerializer, SelectionUkBase):
    article = serializers.SerializerMethodField()
    product = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionListRuSerializer(serializers.ModelSerializer, BasketBaseSerializer, SelectionRuBase):
    article = serializers.SerializerMethodField()
    product = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()

    class Meta:
        model = Selection
        fields = '__all__'
