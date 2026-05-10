from flask import Flask
from flask_cors import CORS
from app.config.db import get_connection
from app.routes.auth_routes import auth

app = Flask(__name__)

CORS(app)

app.register_blueprint(auth)

@app.route('/test')
def test():

    try:

        connection = get_connection()

        return {
            "success": True,
            "message": "Backend y SQL Server funcionando"
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }

if __name__ == '__main__':
    app.run(debug=True)