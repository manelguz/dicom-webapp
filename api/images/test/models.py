from django.test import TestCase
from images.models import Images, user_directory_path


class TestDirectoryPathCreation(TestCase):
    def test_directory_without_extension(self):
        path = user_directory_path("", "test_img")
        self.assertEqual(path, "images/test_img.dcm")

    def test_directory_with_extension(self):
        path = user_directory_path("", "test_img.dcm")
        self.assertEqual(path, "images/test_img.dcm")
