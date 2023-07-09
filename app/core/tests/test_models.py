"""
Tests for models.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful."""
        email = 'test@example.com'
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        # cannot do pw = pw. Need check password through hashing system.
        self.assertTrue(user.check_password(password))

    def test_new_user_email_without_email_raises_error(self):
        """Test creating user without email raises error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password="testpass123",
            )
