import django_filters
from .models import Author


class AuthorFilterSet(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    nationality = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model=Author
        fields = ['name', 'nationality']