from flask import Blueprint, jsonify, request, redirect
from werkzeug.urls import url_fix

from app import db
from app.models import URL


def error(status_code, message):
    ''' Simple error object creation '''
    response = jsonify({
        'message': message,
        'status_code': status_code
    })
    response.status_code = status_code
    return response


api_bp = Blueprint('api', __name__)


@api_bp.route('/urls/<int:key>', methods=['GET'])
def get_url(key):
    ''' Gets URL from database '''
    url = URL.query.get(key)
    if url is None:
        return error(404, 'Id %d not found' % key)
    return jsonify(dict(url))


@api_bp.route('/urls', methods=['GET'])
def get_urls():
    ''' Gets all URLs from database '''
    urls = [dict(u) for u in URL.query.all()]
    return jsonify(urls)


@api_bp.route('/urls', methods=['POST'])
def post_url():
    ''' Insert URL to database if it is not there already '''
    # Invalid request
    if not request.is_json:
        return error(400, 'Request must be of json type')

    if 'url' not in request.json:
        return error(400, 'Json object must have "url" key')

    url = url_fix(request.json['url'])

    # URL in database
    stored_url = URL.query.filter_by(url=url).first()
    if stored_url is not None:
        return jsonify(dict(stored_url))

    # New URL
    try:
        new_url = URL(url=url)
    except ValueError:
        return error(400, 'Invalid URL "%s"' % url)

    db.session.add(new_url)
    db.session.commit()
    return jsonify(dict(new_url))


redirect_bp = Blueprint('redirect', __name__)


@redirect_bp.route('/<int:key>', methods=['GET'])
def redirect_to(key):
    ''' Redirects to the URL '''
    url = URL.query.get(key)
    if url is None:
        return error(404, 'Id %d not found' % key)
    return redirect(url.url)
