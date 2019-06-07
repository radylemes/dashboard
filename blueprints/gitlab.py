import flask
import requests
import services.auth

ACCESS_TOKEN = '_zxjndwab2ifAqm56mzR'

PROJECTS_URL = 'https://gitlab.com/api/v4/projects?owned=true&private_token={}'.format(ACCESS_TOKEN)
PROJECTS_COMMITS = 'https://gitlab.com/api/v4/projects/12680269/repository/commits?owned=true&private_token={}'.format(ACCESS_TOKEN)

blueprint = flask.Blueprint('gitlab', __name__)

@blueprint.route('/gitlab', methods=[ 'GET' ])
@services.auth.login_required
def get_gitlab():
	
	context = {
		'page' : 'gitlab',
		'projects': requests.get(PROJECTS_URL).json(),
		'commits': requests.get(PROJECTS_COMMITS).json(),
	}

	return flask.render_template('gitlab.html', context=context)
	
@blueprint.route('/gitlab/commits/<string:commit_id>', methods=[ 'GET' ])
def get_commits(commit_id):

	PROJECTS_COMMITS = 'https://gitlab.com/api/v4/projects/{}/repository/commits?owned=true&private_token={}'.format(commit_id, ACCESS_TOKEN)

	context = {
		'page' : 'commits',
		'commits': requests.get(PROJECTS_COMMITS).json(),
	}

	return flask.render_template('/commits.html', context=context)