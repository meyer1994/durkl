from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def create_app(config):
    ''' Creates app '''
    app = Flask(__name__)
    app.config.from_object(config)

    # Database
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Migration
    migrate.init_app(app, db)

    # API
    from app.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    # Redirect
    from app.routes import redirect_bp
    app.register_blueprint(redirect_bp, url_prefix='/')

    return app


from app import routes, models
