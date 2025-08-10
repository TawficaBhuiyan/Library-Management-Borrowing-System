from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, CategoryViewSet, BookViewSet, BorrowBookView, ReturnBookView

router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('categories', CategoryViewSet)
router.register('books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('borrow/', BorrowBookView.as_view(), name='borrow-book'),
    path('return/', ReturnBookView.as_view(), name='return-book'),
]
