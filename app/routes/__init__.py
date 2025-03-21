from app.routes.graphql import graphql_bp
from app.routes.index import index_bp

def init_routes(app):
    app.register_blueprint(graphql_bp, url_prefix='/api')
    app.register_blueprint(index_bp)
