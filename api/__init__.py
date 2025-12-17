from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    from .routes import bp
    app.register_blueprint(bp, url_prefix="/api")

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    return app
