import flask

blueprint = flask.Blueprint('docker', __name__)

@blueprint.route('/docker', methods=[ 'GET'])
def get_docker():

    context = {
        'page' : 'docker'
    }

    return flask.render_template('docker.html', context=context)
    
