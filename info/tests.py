from django.test import TestCase
from info.models import Course, User, Student, Teacher,Class
from django.test.client import Client

# Create your tests here.
class InfoTest(TestCase):
    def create_user(self, username='testuser', password='project123'):
        self.client = Client()
        return User.objects.create(username=username, password=password)

