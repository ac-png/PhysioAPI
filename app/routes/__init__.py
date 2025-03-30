from app.routes.routes import index_bp, graphql_bp

def init_routes(app):
    app.register_blueprint(graphql_bp, url_prefix='/api')
    app.register_blueprint(index_bp)
