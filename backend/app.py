from flask import Flask
from app.routes.auth_routes import auth
from app.routes.document_routes import document
from app.routes.ai_routes import ai

app = Flask(__name__)

# Registrar rutas
app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(document, url_prefix="/api")
app.register_blueprint(ai, url_prefix="/ai")

if __name__ == "__main__":
    app.run(debug=True)