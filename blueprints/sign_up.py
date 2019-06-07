import hashlib
import flask
import ldap3

blueprint = flask.Blueprint('sign_up', __name__)

@blueprint.route('/sign-up', methods=[ 'GET'])
def get_sign_up():

    context = {
        'page': 'sign-up',
        'isPublic': True
    }

    return flask.render_template('sign-up.html', context=context)


@blueprint.route('/sign-up', methods=[ 'POST'])
def post_sign_up():

    server = ldap3.Server('ldap://127.0.0.1:389')
    connection = ldap3.Connection(
        server,
        'cn=admin,dc=dexter,dc=com,dc=br',
        '4linux'
    )

    try:
        connection.bind()
    except:
        return flask.redirect('/sign-up')
    
    first_name = flask.request.form[ 'first_name']
    last_name = flask.request.form[ 'last_name']
    email = flask.request.form[ 'email']
    password = flask.request.form[ 'password']
    uid = email.split('@')[0]

    user = {
        'cn': first_name,
        'sn': last_name,
        'mail': email,
        'uid': uid,
        'userpassword': hashlib.sha256(password.encode()).hexdigest()
    }

    objectClass = [
        'top',
        'person',
        'organizationalPerson',
        'inetOrgPerson',
    ]

    cn = 'uid={},dc=dexter,dc=com,dc=br'.format(email)

    if connection.add(cn, objectClass, user):
        return flask.redirect('/sign-in')
    return flask.redirect('/sign-up')