from rest_framework.test import APITestCase
from . import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your tests here.

class TestTextbookView(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='cainemerrick', password='learning_platform_123')
        self.intro_to_algos = models.Textbook.objects.create(
            user = self.user,
            title = 'intro to algorithms',
            content = bytes('This is the content of the book', 'utf-8'),
        )
        self.deep_learning = models.Textbook.objects.create(
            user = self.user,
            title = 'Deep learning',
            content = bytes('This is the content of the book', 'utf-8'),
        )
        return super().setUp()
    
    def test_list_textbooks(self):
        textbooks = self.client.get(reverse('textbook-list')).json()
        self.assertEqual(len(textbooks), 2)
        self.assertEqual(textbooks[0]['title'], 'intro to algorithms')
        self.assertTrue('content' not in textbooks[0])

    def test_retrieve_textbook(self):
        deep_learning = self.client.get(reverse('textbook-detail', kwargs={'pk':2})).json()
        print(deep_learning)
        self.assertEqual(deep_learning['title'], 'Deep learning')
        self.assertTrue('content' in deep_learning)


def setUp(self):
        self.user = User.objects.create(username='cainemerrick', password='learning_platform_123')
        self.intro_to_algos = models.Textbook.objects.create(
            user = self.user,
            title = 'intro to algorithms',
            content = bytes('This is the content of the book', 'utf-8'),
        )
        self.e1 = models.Exercise.objects.create(
             textbook=self.intro_to_algos,
        )