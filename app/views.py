from app import app
from flask import render_template, request
	

@app.route('/')
def index():
	return render_template('/index.html')


@app.route('/login', methods=['POST'])
def login():
	username = request.values.get('user')
	password = request.values.get('pass')
	return username