import os
from flask import Flask

def create_app(config=None):
	app = Flask(__name__)
	if config is None:
		config = 'production.cfg'

	config = os.path.join(app.root_path, config)
	print config
	app.config.from_pyfile(config)

	@app.route('/')
	def index():
		return 'Hello, %(name)s!' % {'name' : app.config['HELLO']} 

	return app