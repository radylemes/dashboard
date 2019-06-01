import flask

import jenkins

HOST = 'http://localhost:8080'
USER = '4linux'
PASS = '4linux123'

connection  = jenkins.Jenkins(
    HOST, username=USER, password=PASS
)

blueprint = flask.Blueprint('jenkins', __name__)

@blueprint.route('/jenkins', methods=[ 'GET'])
def get_jenkins():

    context = {
        'page' : 'jenkins',
        'jobs' : connection.get_jobs()
    }

    return flask.render_template('jenkins.html', context=context)

@blueprint.route('/jenkins/build/<string:job>', methods=[ 'GET'])
def start_build(job):
    connection.build_job(job)

    return flask.redirect('/jenkins')

@blueprint.route('/jenkins/update/<string:job>', methods=[ 'GET'])
def update_build(job):

    return connection.get_job_config(job)


    
