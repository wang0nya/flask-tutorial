from flask import Flask, jsonify


def create_app(config=None):
    app = Flask(__name__)

    # See http://flask.pocoo.org/docs/latest/config/
    app.config.update(dict(DEBUG=True))
    app.config.update(config or {})

    @app.route("/")
    def hello_world():
        return "Hello World"

    @app.route("/foo/<some_id>")
    def foo_url_arg(some_id):
        return jsonify({"echo": some_id})

    return app


if __name__ == "__main__":
    app = create_app()
