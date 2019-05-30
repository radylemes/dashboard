import flask

blueprint = flask.Blueprint('jenkins', __name__)

@blueprint.route('/jenkins', methods=[ 'GET'])
def get_jenkins():

    context = {
        'page' : 'jenkins'
    }

    return flask.render_template('jenkins.html', context=context)
    
    
