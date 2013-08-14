from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
app = Flask(__name__)


def request_wants_json():
	best = request.accept_mimetypes.best_match(['application/json', 'text/html'])
	return best == 'application/json' and request.accept_mimetypes[best] > request.accept_mimetypes['text/html']

# GET HEAD POST PUT DELETE OPTIONS 
@app.route('/')
def hello_world():
	if request_wants_json():
		return 'jsonify hello world'
	return 'html wello world'

@app.route('/', methods = ['POST'])
def hello_world_post():
	if request_wants_json():
		return 'jsonify POST hello world'
	return 'html POST wello world'

@app.route('/login', methods=['POST', 'GET'])
def login():
	error = None
	if request.method == 'POST':
		if valid_login(request.form['username'],request.form['password']):
			return log_the_user_in(request.form['username'])
		else:
			error = 'Invalid username/password'
	return render_template('login.html', error=error)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)

