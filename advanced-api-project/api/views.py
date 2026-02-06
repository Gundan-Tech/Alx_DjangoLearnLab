from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters  # Required for Search and Ordering
from django_filters.rest_framework import DjangoFilterBackend  # Required for Filtering
from django_filters import rest_framework as django_filters
from .models import Book
from .serializers import BookSerializer

# BookListView: Handles GET requests to retrieve all books.
# IsAuthenticatedOrReadOnly ensures unauthenticated users have read-only access.
class BookListView(generics.ListAPIView):
    """
    Handles GET requests to retrieve a list of books.
    Supports filtering by title, author, and publication_year.
    Supports searching by title and author.
    Supports ordering by title and publication_year.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    filterset_fields = ['title', 'author__name', 'publication_year']
    
    search_fields = ['title', 'author__name']
    
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

# BookUpdateView: Handles PUT/PATCH requests to modify an existing book.
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# BookDeleteView: Handles DELETE requests to remove a book instance.
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]