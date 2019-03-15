import re
from datetime import datetime

from flask_sqlalchemy import orm

from app import db

# Copied from:
#   https://stackoverflow.com/a/7160778/5092038
URL_REGEX = re.compile(
    r'^(?:http|ftp)s?://'                               # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+'
    r'(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'              # domain...
    r'localhost|'                                       # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'              # ...or ip
    r'(?::\d+)?'                                        # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)


class URL(db.Model):
    id = db.Column(db.Integer(), primary_key=True, auto_increment=True)
    url = db.Column(db.Text(), index=True, nullable=False, unique=True)
    date = db.Column(db.Date(), default=datetime.utcnow, nullable=False)

    @orm.validates('url')
    def validate_url(self, key, url):
        '''
        Validates the URL.

        Args:
            key: Name of the attribute
            url: URL to be validated

        Returns:
            The url, if valid.

        Raises:
            ValueError when the URL is invalid.
        '''
        if not URL_REGEX.match(url):
            raise ValueError('The URL %s is not valid' % url)
        return url

    def __repr__(self):
        return 'URL(id=%s, url=%s, date=%s)' % (self.id, self.url, self.date)

    def __iter__(self):
        yield 'id', self.id
        yield 'url', self.url
        yield 'date', self.date
