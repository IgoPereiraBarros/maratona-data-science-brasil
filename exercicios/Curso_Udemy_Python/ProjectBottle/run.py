from app import app

from os import environ
from bottle import TEMPLATE_PATH

if __name__ == '__main__':
	TEMPLATE_PATH.insert(0, 'app/views/')
	if environ.get('APP_LOCATION') == 'heroku':
		app.run(host='0.0.0.0', port=int(environ.get('PORT', 5000)))
	else:
		app.run(host='localhost', port=8080, debug=True, reloader=True)