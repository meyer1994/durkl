from flask import jsonify

from app import app
from app.models import URL


@app.route('/')
def hello():
    return 'hello world'


@app.route('/<int:key>')
def get(key):
    urls = [dict(u) for u in URL.query.all()]
    return jsonify(urls)
