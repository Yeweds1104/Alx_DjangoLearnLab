from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.author = Author.objects.create(name='Test Author')
        
        self.book1 = Book.objects.create(title='Django Unchained', publication_year=2012, author=self.author)
        self.book2 = Book.objects.create(title='Python 101', publication_year=2015, author=self.author)
        
        self.book_create_url = reverse('book-create')
        self.book_list_url = reverse('book-list')
        self.book_detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        self.book_update_url = reverse('book-update', kwargs={'pk': self.book1.pk})
        self.book_delete_url = reverse('book-delete', kwargs={'pk': self.book1.pk})
        
    def test_list_books(self):
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        
    def test_retrieve_book(self):
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)
        
    def test_create_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "title": "New Book",
            "publication_year": 2020,
            "author": self.author.id
        }
        response = self.client.post(self.book_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        
    def test_create_book_unauthenticated(self):
        data = {
            "title": "Should Not Work",
            "publication_year": 2020,
            "author": self.author.id
        }
        respone = self.client.post(self.book_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_update_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "title": "Updated Book",
            "publication_year": 2018,
            "author": self.author.id
        }
        response = self.client.put(self.book_update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")
        
    def test_delete_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.book_delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book1.pk).exists())
        
    def test_filter_books_by_year(self):
        response = self.client.get(self.book_list_url, {'publication_year': 2012})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Django Unchained')
        
    def test_search_books_by_title(self):
        response = self.client.get(self.book_list_url, {'search': 'Python'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Python 101')
        
    def test_order_books_by_year_desc(self):
        response = self.client.get(self.book_list_url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Python 101')
        self.assertEqual(response.data[1]['title'], 'Django Unchained')
        
    def test_create_book_with_future_year_should_fail(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "title": "Future Book",
            "publication_year": 2025,
            "author": self.author.id
        }
        response = self.client.post(self.book_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Publication year cannot be in the future", str(response.data).lower)