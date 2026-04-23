import django_filters
from books.models import Book

class BookFilterSet(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains')
    publisher = django_filters.CharFilter(field_name='publisher__name', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher']