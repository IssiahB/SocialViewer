from flask import Flask
from app import app, login_manager


if __name__ == '__main__':
	login_manager.init_app(app)
	app.run(debug=True);
