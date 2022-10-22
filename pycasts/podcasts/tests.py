from django.test import TestCase
from .models import Episode
from django.utils import timezone


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
