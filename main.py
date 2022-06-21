from flask import Flask, render_template

from bp_api.views import bp_api
from bp_posts.views import bp_posts
import logger
from exceptions.data_exceptions import DataSourceError


def create_and_config_app(config_path):
    app = Flask(__name__)
    app.register_blueprint(bp_api, url_prefix='/api')
    app.register_blueprint(bp_posts)
    app.config.from_pyfile(config_path)
    logger.config(app)
    return app


app = create_and_config_app('config.py')


@app.errorhandler(404)
def page_error_404(error):
    return 'Такой страницы нет', 404


@app.errorhandler(500)
def page_error_500(error):
    return f'На сервере произошла ошибка - {error}', 404


@app.errorhandler(DataSourceError)
def page_error_data_source_error(error):
    return f'Ошибка данных на сайте {error}', 500


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
