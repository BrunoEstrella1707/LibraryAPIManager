from django.urls import path
from books.views import BookCreateListView, BookRetrieveUpdateDestroyView, BooksByAuthor, BooksByPubliser, BookStatsView, BookReviewsView


urlpatterns = [
    path('books/', BookCreateListView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail-view'),
    path('books/by-author/<int:author_id>/', BooksByAuthor.as_view(), name='book-by-author-list-detail'),
    path('books/by-publisher/<int:publisher_id>/', BooksByPubliser.as_view(), name='book-by-publisher-list-detail'),
    path('books/stats/', BookStatsView.as_view(), name='book-stats-view'),
    path('books/<int:pk>/reviews/', BookReviewsView.as_view(), name='book-review-view'),
]