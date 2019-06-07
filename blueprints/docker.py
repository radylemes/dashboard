import logging

import flask

import docker

import services.auth

connection = docker.DockerClient()

blueprint = flask.Blueprint('docker', __name__)

@blueprint.route('/docker', methods=[ 'GET'])
@services.auth.login_required
def get_docker():


    context = {
        'page' : 'docker',
        'containers': connection.containers.list(all=True)
    }

    email = flask.session.get('email')
    logging.debug('{} acessou rota docker'. format(email))

    return flask.render_template('docker.html', context=context)
    
@blueprint.route('/docker/start/<string:containerid>', methods=[ 'GET'])
def start_container(containerid):

    container = connection.containers.get(containerid)
    if container:
        container.start()

    return flask.redirect('/docker')

@blueprint.route('/docker/stop/<string:containerid>', methods=[ 'GET'])
def stop_container(containerid):

    container = connection.containers.get(containerid)
    if container:
        container.stop()

    return flask.redirect('/docker')

