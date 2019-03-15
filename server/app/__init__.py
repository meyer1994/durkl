from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes, models

# add simple URL to database
with app.app_context():
    db.create_all()
    url = models.URL(id=1, url='https://example.org')
    db.session.add(url)
    db.session.commit()
