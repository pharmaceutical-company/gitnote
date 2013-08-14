from flask import Blueprint, render_template, redirect, url_for

app = Blueprint('main', __name__)

@app.route('/')
def index():
    return redirect(url_for('main.list'))

@app.route('/list')
def list():
    return render_template('list.html')

@app.route('/new')
def new():
    return render_template('editor.html')

@app.route('/edit')
def edit():
    return render_template('editor.html')

@app.route('/view')
def view():
    return render_template('view.html')

