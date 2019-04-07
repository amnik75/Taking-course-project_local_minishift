import datetime

from django.test import TestCase

from .models import Student

from login.api.views import isExist,isRepeating

class LoginTests(TestCase):

    def test_isExist(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        data = {'student_number':9427243,'id_number':2980854042}
        self.assertIs(isExist(data), False)

    def test_isRepeating(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        data = {'student_number':9427243,'id_number':2980854042}
        self.assertIs(isRepeating(data), False)