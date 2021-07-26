from rest_framework import serializers
from basket.models import Basket, Order, Selection
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

    def get_summa(self, obj):
        if obj.user.role == 3:
            if obj.product.sale_price is None:
                return obj.product.price * obj.count
            else:
                return obj.product.sale_price * obj.count
        if obj.user.role == 4:
            return obj.product.opt_price * obj.count
        if obj.user.role == 5:
            return obj.product.small_opt_price * obj.count
        if obj.user.role == 6:
            return obj.product.drop_price * obj.count


class BasketSerializer(serializers.ModelSerializer, BasketBaseSerializer):
    product = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    summa = serializers.SerializerMethodField()
    article = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()
    user = CustomUserListSerializer(read_only=True)

    class Meta:
        model = Basket
        fields = '__all__'


class BasketCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = ['product', 'user']


class BasketDetailSerializer(serializers.ModelSerializer, BasketBaseSerializer):
    article = serializers.SerializerMethodField()
    summa = serializers.SerializerMethodField()
    product = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ['product', 'article', 'count', 'summa', 'price', 'photo']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    basket = BasketDetailSerializer(many=True, read_only=True)
    grand_total = serializers.DecimalField(max_digits=12, decimal_places=2, default=0)

    class Meta:
        model = Order
        fields = '__all__'


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
