#!/usr/bin/env python3.6
import os
from flask import Flask
from flask import render_template

app = Flask(__name__)


class PrefixMiddleware(object):
    """
    Class to enable serving the app from a prefix
    """

    def __init__(self, app, prefix=''):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):
        if environ['PATH_INFO'].startswith(self.prefix):
            environ['PATH_INFO'] = environ['PATH_INFO'][len(self.prefix):]
            environ['SCRIPT_NAME'] = self.prefix
            return self.app(environ, start_response)
        else:
            start_response('404', [('Content-Type', 'text/plain')])
            return ["This url does not belong to the app.".encode()]

app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/basic_flask_template')

@app.route("/")
def index():
	message = "Hello from basic_flask_template"
	return render_template('index.html', message=message)


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=1024, debug=True)

