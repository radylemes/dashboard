import flask

blueprint = flask.Blueprint('gitlab', __name__)

@blueprint.route('/gitlab', methods=[ 'GET'])
def get_gitlab():
	
	context = {
		'page' : 'gitlab'
	}

	return flask.render_template('gitlab.html', context=context)
	