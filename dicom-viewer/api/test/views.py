import tempfile

from django.test import TestCase
from django import http


class TestUploadImage(TestCase):
    def test_post_new_image(self):
        with tempfile.NamedTemporaryFile() as f:
            form = {
                "file": f,
                "name": "test1",
            }
            response = self.client.post('/api/', data=form)
        self.assertEqual(response.status_code, 200)

    def test_post_repeated_image(self):
        with tempfile.NamedTemporaryFile() as f:
            form = {
                "file": f,
                "name": "test1",
            }
            self.client.post('/api/',  data=form)
            response = self.client.post('/api/', data=form)
        self.assertEqual(response.status_code, 400)


class TestListAllImages(TestCase):

    def setUp(self):
        with tempfile.NamedTemporaryFile() as f:
            form = {
                "file": f,
                "name": "test1",
            }
            self.client.post('/api/', data=form)

    def test_list_all_image(self):

        response = self.client.get('/api/list')
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, http.JsonResponse)
        self.assertIn("test1", data["all_images"] )


class TestDeleteImages(TestCase):

    def setUp(self):
        with tempfile.NamedTemporaryFile() as f:
            form = {
                "file": f,
                "name": "test1",
            }
            self.client.post('/api/', data=form)

    def test_delete_one_image(self):
        response = self.client.delete('/api/id/test1')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, http.HttpResponse)

    def test_delete_non_existing_image(self):
        response = self.client.delete('/api/id/test2')
        self.assertEqual(response.status_code, 404)
        self.assertIsInstance(response, http.HttpResponse)


class TestGetImages(TestCase):

    def setUp(self):
        with tempfile.NamedTemporaryFile() as f:
            form = {
                "file": f,
                "name": "test1",
            }
            self.client.post('/api/', data=form)

    def test_get_one_image(self):

        response = self.client.get('/api/id/test1')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, http.JsonResponse)
