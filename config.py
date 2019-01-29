#Imports
import os

#Define path to database (for database configuration)
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	#Configure secret key
	SECRET_KEY = os.environ.get('SECRET_KEY')
	#Configure database
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False