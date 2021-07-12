from django_filters import Filter, FilterSet
from .models import AttributesValue


class ListFilter(Filter):

    def filter(self, qs, value):
        if not value:
            return qs

        self.lookup_type = 'in'
        values = value.split(',')
        return super(ListFilter, self).filter(qs, values)


class UserFilter(FilterSet):

    class Meta:
        model = AttributesValue
        fields = ['name_attribute']
