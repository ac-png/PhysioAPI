from app.db import create_app
from app.seed import seed_data
from flask_graphql import GraphQLView
from app.schema import schema

app = create_app()

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == "__main__":
    with app.app_context():
        seed_data()
    app.run(debug=True)
