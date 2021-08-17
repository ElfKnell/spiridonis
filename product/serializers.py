from rest_framework import serializers
from .models import Product
from attibutes.serializers import AttributeValueCustomerListSerializer, \
    AttributeValueWholesalerListSerializer, AttributeValueRetailWholesalerListSerializer, \
    AttributeValueDropshipperListSerializer, AttributeValueListSerializer, AttributeValueAllListSerializer, \
    AttributeValueCustomerUkListSerializer, AttributeValueCustomerRuListSerializer, AttributeValueUkListSerializer, \
    AttributeValueRuListSerializer, AttributeValueWholesalerUkListSerializer, AttributeValueWholesalerRuListSerializer, \
    AttributeValueRetailWholesalerUkListSerializer, AttributeValueRetailWholesalerRuListSerializer, \
    AttributeValueDropshipperRuListSerializer, AttributeValueDropshipperUkListSerializer
from rating.serializers import RatingListSerializer


class ProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


# Відображення каталога товарів
class ProductListSerializer(serializers.ModelSerializer):
    attributes = AttributeValueAllListSerializer(many=True)
    rating = RatingListSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


# Винесення спільного методу для списку продуктів
class ProductBase:
    def get_middle_star(self, obj):
        value_star = obj.rating.all().values_list('star', flat=True)
        count_star = obj.rating.count()
        if count_star:
            return round(sum(list(value_star))/count_star)
        return obj.rating.count()


class ProductListCustomerSerializer(serializers.ModelSerializer, ProductBase):
    attributes = AttributeValueCustomerListSerializer(many=True)
    middle_star = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name_product', 'article', 'photo', 'price',
                  'sale_price', 'attributes', 'middle_star', 'slug')


class ProductUkListCustomerSerializer(serializers.ModelSerializer, ProductBase):
    attributes = AttributeValueCustomerUkListSerializer(many=True)
    middle_star = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name_product_uk', 'article', 'photo', 'price',
                  'sale_price', 'attributes', 'middle_star', 'slug')


class ProductRuListCustomerSerializer(serializers.ModelSerializer, ProductBase):
    attributes = AttributeValueCustomerRuListSerializer(many=True)
    middle_star = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name_product_ru', 'article', 'photo', 'price',
                  'sale_price', 'attributes', 'middle_star', 'slug')


class ProductListWholesalerSerializer(serializers.ModelSerializer, ProductBase):
    attributes = AttributeValueListSerializer(many=True)
    middle_star = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name_product', 'article', 'photo', 'opt_price',
                  'attributes', 'middle_star', 'slug')


class ProductUkListWholesalerSerializer(serializers.ModelSerializer, ProductBase):
    attributes = AttributeValueUkListSerializer(many=True)
    middle_star = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name_product_uk', 'article', 'photo', 'opt_price',
                  'attributes', 'middle_star', 'slug')


class ProductRuListWholesalerSerializer(serializers.ModelSerializer, ProductBase):
    attributes = AttributeValueRuListSerializer(many=True)
    middle_star = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name_product_ru', 'article', 'photo', 'opt_price',
                  'attributes', 'middle_star', 'slug')


class ProductListRetailWholesalerSerializer(serializers.ModelSerializer, ProductBase):
    attributes = AttributeValueListSerializer(many=True)
    middle_star = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name_product', 'article', 'photo', 'small_opt_price',
                  'attributes', 'middle_star', 'slug')


class ProductUkListRetailWholesalerSerializer(serializers.ModelSerializer, ProductBase):
    attributes = AttributeValueUkListSerializer(many=True)
    middle_star = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name_product_uk', 'article', 'photo', 'small_opt_price',
                  'attributes', 'middle_star', 'slug')


class ProductRuListRetailWholesalerSerializer(serializers.ModelSerializer, ProductBase):
    attributes = AttributeValueRuListSerializer(many=True)
    middle_star = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name_product_ru', 'article', 'photo', 'small_opt_price',
                  'attributes', 'middle_star', 'slug')


class ProductListDropshipperSerializer(serializers.ModelSerializer, ProductBase):
    attributes = AttributeValueListSerializer(many=True)
    middle_star = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name_product', 'article', 'photo',
                  'drop_price', 'attributes', 'middle_star', 'slug')


class ProductUkListDropshipperSerializer(serializers.ModelSerializer, ProductBase):
    attributes = AttributeValueUkListSerializer(many=True)
    middle_star = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name_product_uk', 'article', 'photo',
                  'drop_price', 'attributes', 'middle_star', 'slug')


class ProductRuListDropshipperSerializer(serializers.ModelSerializer, ProductBase):
    attributes = AttributeValueRuListSerializer(many=True)
    middle_star = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name_product_ru', 'article', 'photo',
                  'drop_price', 'attributes', 'middle_star', 'slug')
# Кінець відображення каталогу товарів


# Відображення окремого товару
class ProductDetailSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ('date_create', 'updated_on')


class ProductDetailCustomerSerializers(serializers.ModelSerializer):
    attributes = AttributeValueCustomerListSerializer(many=True)
    middle_star = serializers.IntegerField(default=0)

    class Meta:
        model = Product
        fields = ('name_product', 'title', 'article', 'description', 'meta_description', 'photo',
                  'price', 'sale_price', 'is_sale', 'sex', 'status', 'related_products', 'manufacturer',
                  'category', 'attributes', 'middle_star')


class ProductUkDetailCustomerSerializers(serializers.ModelSerializer):
    attributes = AttributeValueCustomerUkListSerializer(many=True)
    middle_star = serializers.IntegerField(default=0)

    class Meta:
        model = Product
        fields = ('name_product_uk', 'title', 'article', 'description_uk', 'meta_description', 'photo',
                  'price', 'sale_price', 'is_sale', 'sex_uk', 'status_uk', 'related_products', 'manufacturer',
                  'category', 'attributes', 'middle_star')


class ProductRuDetailCustomerSerializers(serializers.ModelSerializer):
    attributes = AttributeValueCustomerRuListSerializer(many=True)
    middle_star = serializers.IntegerField(default=0)

    class Meta:
        model = Product
        fields = ('name_product_ru', 'title', 'article', 'description_ru', 'meta_description', 'photo',
                  'price', 'sale_price', 'is_sale', 'sex_ru', 'status_ru', 'related_products', 'manufacturer',
                  'category', 'attributes', 'middle_star')


class ProductDetailWholesalerSerializer(serializers.ModelSerializer):
    attributes = AttributeValueWholesalerListSerializer(many=True)
    middle_star = serializers.IntegerField(default=0)

    class Meta:
        model = Product
        fields = ('name_product', 'title', 'article', 'description', 'meta_description', 'photo',
                  'opt_price', 'sex', 'status', 'related_products', 'manufacturer',
                  'category', 'attributes', 'middle_star')


class ProductUkDetailWholesalerSerializer(serializers.ModelSerializer):
    attributes = AttributeValueWholesalerUkListSerializer(many=True)
    middle_star = serializers.IntegerField(default=0)

    class Meta:
        model = Product
        fields = ('name_product_uk', 'title', 'article', 'description_uk', 'meta_description', 'photo',
                  'opt_price', 'sex_uk', 'status_uk', 'related_products', 'manufacturer',
                  'category', 'attributes', 'middle_star')


class ProductRuDetailWholesalerSerializer(serializers.ModelSerializer):
    attributes = AttributeValueWholesalerRuListSerializer(many=True)
    middle_star = serializers.IntegerField(default=0)

    class Meta:
        model = Product
        fields = ('name_product_ru', 'title', 'article', 'description_ru', 'meta_description', 'photo',
                  'opt_price', 'sex_ru', 'status_ru', 'related_products', 'manufacturer',
                  'category', 'attributes', 'middle_star')


class ProductDetailRetailWholesalerSerializer(serializers.ModelSerializer):
    attributes = AttributeValueRetailWholesalerListSerializer(many=True)
    middle_star = serializers.IntegerField(default=0)

    class Meta:
        model = Product
        fields = ('name_product', 'title', 'article', 'description', 'meta_description', 'photo',
                  'small_opt_price', 'sex', 'status', 'related_products', 'manufacturer',
                  'category', 'attributes', 'middle_star')


class ProductUkDetailRetailWholesalerSerializer(serializers.ModelSerializer):
    attributes = AttributeValueRetailWholesalerUkListSerializer(many=True)
    middle_star = serializers.IntegerField(default=0)

    class Meta:
        model = Product
        fields = ('name_product_uk', 'title', 'article', 'description_uk', 'meta_description', 'photo',
                  'small_opt_price', 'sex_uk', 'status_uk', 'related_products', 'manufacturer',
                  'category', 'attributes', 'middle_star')


class ProductRuDetailRetailWholesalerSerializer(serializers.ModelSerializer):
    attributes = AttributeValueRetailWholesalerRuListSerializer(many=True)
    middle_star = serializers.IntegerField(default=0)

    class Meta:
        model = Product
        fields = ('name_product_ru', 'title', 'article', 'description_ru', 'meta_description', 'photo',
                  'small_opt_price', 'sex_ru', 'status_ru', 'related_products', 'manufacturer',
                  'category', 'attributes', 'middle_star')


class ProductDetailDropshipperSerializer(serializers.ModelSerializer):
    attributes = AttributeValueDropshipperListSerializer(many=True)
    middle_star = serializers.IntegerField(default=0)

    class Meta:
        model = Product
        fields = ('name_product', 'title', 'article', 'description', 'meta_description', 'photo',
                  'drop_price', 'sex', 'status', 'related_products', 'manufacturer',
                  'category', 'attributes', 'middle_star')


class ProductUkDetailDropshipperSerializer(serializers.ModelSerializer):
    attributes = AttributeValueDropshipperUkListSerializer(many=True)
    middle_star = serializers.IntegerField(default=0)

    class Meta:
        model = Product
        fields = ('name_product_uk', 'title', 'article', 'description_uk', 'meta_description', 'photo',
                  'drop_price', 'sex_uk', 'status_uk', 'related_products', 'manufacturer',
                  'category', 'attributes', 'middle_star')


class ProductRuDetailDropshipperSerializer(serializers.ModelSerializer):
    attributes = AttributeValueDropshipperRuListSerializer(many=True)
    middle_star = serializers.IntegerField(default=0)

    class Meta:
        model = Product
        fields = ('name_product_ru', 'title', 'article', 'description_ru', 'meta_description', 'photo',
                  'drop_price', 'sex_ru', 'status_ru', 'related_products', 'manufacturer',
                  'category', 'attributes', 'middle_star')
# Кінець відображення окремого товару
