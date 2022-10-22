from django.test import TestCase
from django.urls.base import reverse
from django.utils import timezone

from datetime import datetime

from .models import Episode


# Create your tests here.

class PodCastsTests(TestCase):
    def setUp(self):
        self.episode = Episode.objects.create(
            title='Test Title',
            description='Test Description',
            pub_date=timezone.now(),
            link='https://www.google.com',
            image='https://www.google.com',
            podcast_name='Test Podcast',
            guid='12345678-1234-1234-1234-123456789012',
        )

    def test_episode_content(self):
        self.assertEqual(self.episode.title, 'Test Title')
        self.assertEqual(self.episode.description, 'Test Description')
        self.assertEqual(self.episode.podcast_name, 'Test Podcast')
        self.assertEqual(self.episode.guid, '12345678-1234-1234-1234-123456789012')

    def test_episode_str_representation(self):
        self.assertEqual(str(self.episode), 'Test Podcast - Test Title')

    def test_homepage_should_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_should_uses_correct_template(self):
        response = self.client.get(reverse('homepage'))
        self.assertTemplateUsed(response, 'homepage.html')

    def test_homepage_should_lists_contents(self):
        response = self.client.get(reverse('homepage'))
        self.assertContains(response, 'Test Title')