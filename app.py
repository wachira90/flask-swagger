from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Swagger UI configuration
SWAGGER_URL = '/swagger'  # URL for Swagger UI
API_URL = '/static/swagger.json'  # Location of OpenAPI Spec

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Flask API with Swagger UI"
    }
)

# Register Swagger UI blueprint
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


# Example API routes
@app.route('/api/greet/<name>', methods=['GET'])
def greet_user(name):
    """Greet the user by name."""
    return jsonify({"message": f"Hello, {name}!"})


if __name__ == '__main__':
    app.run(debug=True)