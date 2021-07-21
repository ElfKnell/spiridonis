from django_filters import rest_framework as filters

from product.models import Product


class PriceFilter(filters.FilterSet):
    price = filters.RangeFilter()
    sale_price = filters.RangeFilter()
    opt_price = filters.RangeFilter()
    small_opt_price = filters.RangeFilter()
    drop_price = filters.RangeFilter()

    class Meta:
        model = Product
        fields = ['price', 'is_new', 'is_sale', 'sex', 'manufacturer', 'status', 'attributes',
                  'sale_price', ]