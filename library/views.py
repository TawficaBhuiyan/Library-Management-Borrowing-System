from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from django.db import transaction
from django.utils import timezone
from .models import Author, Category, Book, Borrow
from .serializers import AuthorSerializer, CategorySerializer, BookSerializer, BorrowSerializer
from django_filters.rest_framework import DjangoFilterBackend

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAdminUser]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'category']
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

class BorrowBookView(generics.CreateAPIView):
    serializer_class = BorrowSerializer
    permission_classes = [permissions.IsAuthenticated]

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        book_id = request.data.get('book_id')
        try:
            book = Book.objects.select_for_update().get(id=book_id)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=404)

        active_borrows = Borrow.objects.filter(user=request.user, return_date__isnull=True).count()
        if active_borrows >= 3:
            return Response({'error': 'Borrowing limit reached'}, status=400)

        if book.available_copies <= 0:
            return Response({'error': 'No copies available'}, status=400)

        borrow = Borrow.objects.create(user=request.user, book=book, due_date=timezone.now() + timezone.timedelta(days=14))
        book.available_copies -= 1
        book.save()
        return Response(BorrowSerializer(borrow).data, status=201)

class ReturnBookView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        borrow_id = request.data.get('borrow_id')
        try:
            borrow = Borrow.objects.select_for_update().get(id=borrow_id, user=request.user, return_date__isnull=True)
        except Borrow.DoesNotExist:
            return Response({'error': 'Borrow record not found'}, status=404)

        borrow.return_date = timezone.now()
        borrow.save()

        book = borrow.book
        book.available_copies += 1
        book.save()

        if borrow.return_date > borrow.due_date:
            days_late = (borrow.return_date - borrow.due_date).days
            request.user.penalty_points += days_late
            request.user.save()

        return Response({'message': 'Book returned successfully'})
