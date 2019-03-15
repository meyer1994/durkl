from datetime import datetime
from unittest import TestCase

from app.models import URL


class TestURLModel(TestCase):
    def test_repr(self):
        ''' Returns representation of URL model '''
        time = datetime.utcnow()
        url = URL(id=1, url='https://example.org', date=time)
        expected = 'URL(id=1, url=https://example.org, date=%s)' % time
        self.assertEqual(repr(url), expected)

    def test_dict(self):
        ''' Converts itself to dict using dict() '''
        time = datetime.utcnow()
        url = URL(id=1, url='https://example.org', date=time)
        expected = {'id': 1, 'url': 'https://example.org', 'date': time}
        self.assertEqual(dict(url), expected)
