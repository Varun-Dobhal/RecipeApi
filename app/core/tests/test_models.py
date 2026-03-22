"""
    Tests for Models.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model #this provides features for Authentication.

class ModelTests(TestCase):
    def test_create_use_with_email_sucessful(self):
        email='test@example.com'
        password='test123'
        user=get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test normalizze for new users"""
        sample_emails=[
            ['test1@EXAMPLE.com',"test1@example.com"],
            ['Test2@Example.com',"Test2@example.com"],
            ['TEST3@EXAMPLE.COM',"TEST3@example.com"],
            ['test4@EXAMPLE.COM',"test4@example.com"],
        ]
        for email,expected in sample_emails:
            user=get_user_model().objects.create_user(email,'123')
            self.assertEqual(user.email,expected)

    def test_new_user_without_email_raise_error(self):
        """Checking if email input is blank or not"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('','123')

    def test_new_SuperUser(self):
        """Creatingg SuperUser"""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)