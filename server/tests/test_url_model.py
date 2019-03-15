from unittest import TestCase

from app.models import URL


class TestURLModel(TestCase):
    def test_invalid_url(self):
        ''' Should raise ValueError when URL is invalid '''
        with self.assertRaises(ValueError):
            URL(url='invalid')

    def test_iter(self):
        ''' Converts to dict when using dict() '''
        url = URL(url='http://example.com')
        url = dict(url)
        self.assertIn('id', url)
        self.assertIn('url', url)
        self.assertIn('created_at', url)
        self.assertIn('times_accessed', url)
