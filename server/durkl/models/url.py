from datetime import datetime

from durkl import db


class URL(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    url = db.Column(db.Text(), index=True, nullable=False, unique=True)
    date = db.Column(db.Date(), default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return 'URL(id=%s, url=%s, date=%s)' % (self.id, self.url, self.date)

    def __iter__(self):
        yield 'id', self.id
        yield 'url', self.url
        yield 'date', self.date
