import os
import logging
import json

import flask

from reviews.views import reviews
from roles.views import roles
from spots.views import spots
from users.views import users


def create_app():
    app = flask.Flask(__name__)

    # Select config
    try:
        env = os.environ['APP_ENV']
    except KeyError:
        logging.error('Unknown environment key, defaulting to Development')
        env = 'DevelopmentConfig'
        app.config.from_object('config.%s' % env)

    app.register_blueprint(reviews, url_prefix='/reviews')
    app.register_blueprint(roles, url_prefix='/roles')
    app.register_blueprint(spots, url_prefix='/spots')
    app.register_blueprint(users, url_prefix='/users')
    
    return app


if __name__ == '__main__':
    create_app().run()
