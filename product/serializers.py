from rest_framework import serializers
from .models import Product
from attibutes.serializers import AttributeValueSerializer, AttributeValueListSerializer
from reviews.serializers import ReviewsDetailSerializers
from rating.serializers import RatingSerializer, RatingListSerializer


class ProductSerializers(serializers.ModelSerializer):
    attributes = AttributeValueSerializer(many=True)
    reviews = ReviewsDetailSerializers(many=True)
    rating = RatingSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductDetailSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name_product', 'title', 'model', 'article',
                  'description', 'meta_description', 'photo', 'price',
                  'opt_price', 'small_opt_price', 'sale_price',
                  'count', 'warehouse', 'new', 'related_products',
                  'rating', 'sex', 'updated_on', 'category')


class ProductListSerializer(serializers.ModelSerializer):
    attributes = AttributeValueListSerializer(many=True)
    rating_user = serializers.BooleanField(default=False)
    middle_star = serializers.IntegerField(default=0)
    rating = RatingListSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name_product', 'article', 'photo', 'price', 'opt_price',
                  'small_opt_price', 'sale_price', 'attributes', 'rating_user',
                  'middle_star', 'rating')
