# Flask swagger

Here’s a step-by-step guide to create a Python Flask API with Swagger UI using the `flask-swagger-ui` library:

---

### Step 1: Install Required Libraries

Ensure you have Python installed. Then, install Flask and `flask-swagger-ui` using pip:

```bash
pip install flask flask-swagger-ui
```

---

### Step 2: Create the Flask Application

Create a new Python file (e.g., `app.py`) and write the following code:

#### Code Explanation:

1. Define Flask routes.
2. Provide the OpenAPI specification (YAML or JSON) to configure Swagger UI.
3. Integrate Swagger UI.

```python
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
```

---

### Step 3: Add OpenAPI Specification File

Create a folder named `static` and place an OpenAPI specification file named `swagger.json` inside it. Here's an example of the content:

#### `static/swagger.json`

```json
{
  "swagger": "2.0",
  "info": {
    "version": "1.0.0",
    "title": "Flask API",
    "description": "A simple Flask API with Swagger UI integration"
  },
  "host": "localhost:5000",
  "basePath": "/",
  "schemes": ["http"],
  "paths": {
    "/api/greet/{name}": {
      "get": {
        "summary": "Greet User",
        "description": "Returns a greeting for the given user name",
        "parameters": [
          {
            "name": "name",
            "in": "path",
            "required": true,
            "type": "string"
          }
        ],
        "responses": {
          "200": {
            "description": "A greeting message",
            "schema": {
              "type": "object",
              "properties": {
                "message": {
                  "type": "string"
                }
              }
            }
          }
        }
      }
    }
  }
}
```

---

### Step 4: Run the Application

Start the Flask app:

```bash
python app.py
```

---

### Step 5: Access Swagger UI

1. Open your browser.
2. Navigate to `http://localhost:5000/swagger` to see the Swagger UI.

---

### Explanation of Components:

1. **Flask App (`app.py`)**:
   - The main API server, which serves API routes and integrates the Swagger UI blueprint.

2. **Swagger UI Blueprint**:
   - `flask-swagger-ui` integrates Swagger UI at a specific route (`/swagger`).

3. **OpenAPI Specification (`swagger.json`)**:
   - Defines the API endpoints, parameters, and responses in a structured format.

---

You now have a working Flask API with Swagger UI for interactive API documentation!
