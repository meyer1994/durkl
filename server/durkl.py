from app import create_app
from app.config import ProductionConfig, DevelopmentConfig

app = create_app(DevelopmentConfig)
