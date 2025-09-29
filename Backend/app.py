from flask import Flask
from flask_cors import CORS
from db import init_db
from routes.job_routes import job_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    init_db(app)
    app.register_blueprint(job_bp, url_prefix="/")
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
