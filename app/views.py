from app import app
from flask import render_template, request, redirect, url_for
	

@app.route('/')
def index():
	return render_template('/index.html')


@app.route('/login', methods=['POST'])
def login():
	username = request.values.get('user')
	password = request.values.get('pass')
	return username


@app.route('/create_account', methods=['GET', 'POST'])
def create():
	if request.method == 'GET': # Account Form
		return render_template('/account.html')
	elif request.method == 'POST': # Account Creating

		return redirect(url_for("index"))