from unittest import TestCase

from app import create_app, db
from app.models import URL
from app.config import TestConfig


class TestFlask(TestCase):
    ''' Base class for testing flask '''

    TEST_URLS = [
        'https://example.org',
        'https://gnu.org',
        'https://duckduckgo.com'
    ]

    def setUp(self):
        ''' Create app and add the URLS to it '''
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()
        with self.app.app_context():
            urls = [URL(url=u) for u in TestFlask.TEST_URLS]
            db.session.add_all(urls)
            db.session.commit()
        self.db = db

    def tearDown(self):
        ''' Drop all table items '''
        with self.app.app_context():
            db.drop_all()
