from flask import Flask

def create_app():
    # appの設定
    app = Flask(__name__, static_folder="static/",instance_relative_config=True)
    app.config.from_pyfile('config.py')

    # Blueprintの登録
    from flask_app.views.index import bp_index
    app.register_blueprint(bp_index)

    return app
