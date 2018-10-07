from flask import Flask
from flask_restplus import Api

from auth.views import auth_namespace
from accounts.views import accounts_namespace

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    },
    'oauth2': {
        'type': 'oauth2',
        'flow': 'accessCode',
        'tokenUrl': 'https://oauth.example.com/token',
        'scopes': {
            'read': 'Grant read-only access',
            'write': 'Grant read-write access',
        }
    }
}
app = Flask(__name__)
SWAGGER_DOC = True
api = Api(app, authorizations=authorizations, security=['apikey', {'oauth2': 'read'}], version='dev',
          title='Awesome Flask APIs',
          doc="/" if SWAGGER_DOC is True else False,
          description='Awesome RESTful APIs, written in Flask', )

if __name__ == '__main__':
    api.add_namespace(accounts_namespace)
    api.add_namespace(auth_namespace)
    app.run()
