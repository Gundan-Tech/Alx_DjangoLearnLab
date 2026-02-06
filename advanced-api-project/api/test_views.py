from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):
    """
    Comprehensive tests for Book API endpoints including CRUD, 
    Permissions, Filtering, and Searching.
    """

    def setUp(self):
        # Create a user for authentication tests
        self.user = User.objects.create_user(username='testuser', password='password123')
        
        # Create initial data
        self.author = Author.objects.create(name="George Orwell")
        self.book = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=self.author
        )
        
        # Define URLs
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})
        self.update_url = reverse('book-update', kwargs={'pk': self.book.pk})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book.pk})

    # --- CRUD Tests ---

    def test_create_book_authenticated(self):
        """Test that an authenticated user can create a book."""
        self.client.login(username='testuser', password='password123')
        data = {
            "title": "Animal Farm",
            "publication_year": 1945,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        """Test that an unauthenticated user cannot create a book."""
        data = {"title": "Unauthorized Book", "publication_year": 2000, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_all_books(self):
        """Test retrieving the list of books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_book(self):
        """Test updating a book's title."""
        self.client.login(username='testuser', password='password123')
        data = {"title": "Nineteen Eighty-Four", "publication_year": 1949, "author": self.author.id}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Nineteen Eighty-Four")

    def test_delete_book(self):
        """Test deleting a book."""
        self.client.login(username='testuser', password='password123')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # --- Filtering and Searching Tests ---

    def test_filter_by_title(self):
        """Test filtering books by title."""
        response = self.client.get(f"{self.list_url}?title=1984")
        self.assertEqual(len(response.data), 1)

    def test_search_by_author(self):
        """Test searching for books by author name."""
        response = self.client.get(f"{self.list_url}?search=Orwell")
        self.assertEqual(len(response.data), 1)

    def test_ordering_by_year(self):
        """Test ordering books by publication year."""
        Book.objects.create(title="Later Book", publication_year=2020, author=self.author)
        response = self.client.get(f"{self.list_url}?ordering=publication_year")
        # Ensure the first book in the response is the oldest
        self.assertEqual(response.data[0]['publication_year'], 1949)