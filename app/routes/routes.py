from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_graphql import GraphQLView
from app.schema import schema  # Import your GraphQL schema

# Blueprints for index, GraphQL, login, register, and logout
index_bp = Blueprint('index', __name__, template_folder='templates')
graphql_bp = Blueprint('graphql', __name__)

# Home Route for docs.html
@index_bp.route('/')
def home():
    return render_template('docs.html')  # Serve docs.html on the root route ('/')

# GraphQL view setup for API endpoints
graphql_bp.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

# Helper function to execute GraphQL mutations
def execute_graphql_mutation(mutation, variables):
    query = f"""
    mutation {{
        {mutation}(input: {variables}) {{
            success
            message
            token
        }}
    }}
    """

    try:
        result = schema.execute(query)
        if result.errors:
            # Log GraphQL errors (this helps to see what went wrong in the mutation)
            print(f"GraphQL errors: {result.errors}")
        return result.data[mutation]  # Return the result of the mutation
    except Exception as e:
        print(f"Error executing GraphQL mutation: {str(e)}")  # Log the error
        return {"success": False, "message": "An error occurred during the mutation."}

# Login Route (using GraphQL Mutation)
@index_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Construct the mutation variables
        variables = f'{{ email: "{email}", password: "{password}" }}'

        # Execute the GraphQL Login Mutation
        result = execute_graphql_mutation('login', variables)

        if result['success']:
            return redirect(url_for('index.index'))  # Redirect to home page on success
        else:
            return render_template('login.html', message=result['message'])  # Show error message
    return render_template('login.html')

# Register Route (using GraphQL Mutation)
@index_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        role_id = request.form['role_id']

        # Construct the mutation variables
        variables = f'{{ email: "{email}", password: "{password}", roleId: "{role_id}" }}'

        # Execute the GraphQL Register Mutation
        result = execute_graphql_mutation('register', variables)

        if result['success']:
            return redirect(url_for('index.login'))  # Redirect to login page on success
        else:
            return render_template('register.html', message=result['message'])  # Show error message
    return render_template('register.html')

# Logout Route (using GraphQL Mutation)
@index_bp.route('/logout')
def logout():
    # Execute the GraphQL Logout Mutation (not requiring variables)
    result = execute_graphql_mutation('logout', '{}')

    if result['success']:
        return redirect(url_for('index.index'))  # Redirect to home page on success
    else:
        return jsonify({"message": "Error logging out"}), 400  # Handle logout failure

# Initialize routes for the app
def init_routes(app):
    # Register GraphQL blueprint with a '/api' prefix for API endpoints
    app.register_blueprint(graphql_bp, url_prefix='/api')

    # Register index blueprint (with login, register, logout routes)
    app.register_blueprint(index_bp)
