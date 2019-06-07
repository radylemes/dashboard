import os

import sys

import logging

import flask

import blueprints.docker

import blueprints.gitlab

import blueprints.jenkins

import blueprints.sign_in

import blueprints.sign_up


logging.basicConfig(
    filename = 'app.log',
    level = logging.DEBUG,
    format = '%(asctime)s [%(levelname)s] ' + '[%(funcName)s] [%(filename)s, %(message)s ]',
    datefmt = '[%d/%m/%Y %H:%M:%S]'
)

app = flask.Flask(__name__)

app.secret_key = 'secret'

app.register_blueprint(blueprints.docker.blueprint)

app.register_blueprint(blueprints.gitlab.blueprint)

app.register_blueprint(blueprints.jenkins.blueprint)

app.register_blueprint(blueprints.sign_in.blueprint)

app.register_blueprint(blueprints.sign_up.blueprint)


@app.route('/', methods=[ 'GET'])
def index():
    return flask.redirect('/docker')
    
if __name__ == '__main__':
    
    current_module = os.path.dirname(os.path.curdir)
    sys.path.append(current_module)

    os.environ['FLASK_APP'] = 'app.py'
    os.environ['FLASK_ENV'] = 'development'

    app.run( host='0.0.0.0')
