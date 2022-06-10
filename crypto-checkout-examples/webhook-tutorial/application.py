from flask_cors import CORS
from helpers.crossdomain import *
from flask import Flask
from flask_restful import Api
from endpoints.webhook import Webhook


def set_up_flask_and_api():

    app = Flask(__name__, template_folder="template", static_folder="static", static_url_path='/static')
    app.url_map.strict_slashes = False
    app.config['PROPAGATE_EXCEPTIONS'] = True

    CORS(app, expose_headers='Authorization')

    api_ = Api(app, decorators=[crossdomain(origin="*")])

    endpoint_class = Webhook
    path = 'v1/crypto-payments/webhook'

    api_.add_resource(
        endpoint_class,
        f'/{path}',
        endpoint=f'/{path}'
    )

    return app, api_


application, api = set_up_flask_and_api()


@application.route("/", endpoint="/", methods=["GET", "HEAD"])
def home():
    return """
    <html>
    <body>
    <div><p>Welcome to my App</p></div>
    </body>
    </html>
    """


def main():
    application.run(host='0.0.0.0', port=8080, debug=False)


if __name__ == '__main__':
    main()
