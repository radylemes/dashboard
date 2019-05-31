import flask

import docker

connection = docker.DockerClient()

blueprint = flask.Blueprint('docker', __name__)

@blueprint.route('/docker', methods=[ 'GET'])
def get_docker():

    context = {
        'page' : 'docker',
        'containers': connection.containers.list()
    }

    return flask.render_template('docker.html', context=context)
    
