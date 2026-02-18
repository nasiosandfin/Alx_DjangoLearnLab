from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from api.models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="password123")
        self.client.login(username="tester", password="password123")
        self.book = Book.objects.create(title="Test Book", author="Author A", publication_year=2024)

    def test_create_book(self):
        url = reverse("book-list")
        data = {"title": "New Book", "author": "Author B", "publication_year": 2025}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_get_books(self):
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_update_book(self):
        url = reverse("book-detail", args=[self.book.id])
        data = {"title": "Updated Title"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_delete_book(self):
        url = reverse("book-detail", args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_permission_denied_without_auth(self):
        self.client.logout()
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_filter_books(self):
        url = reverse("book-list") + "?title=Test Book"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Test Book")

    def test_search_books(self):
        url = reverse("book-list") + "?search=Test"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Test" in b["title"] for b in response.data))

    def test_order_books(self):
        Book.objects.create(title="Another Book", author="Author C", publication_year=2023)
        url = reverse("book-list") + "?ordering=publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [b["publication_year"] for b in response.data]
        self.assertEqual(years, sorted(years))
