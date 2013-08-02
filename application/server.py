from flask import Blueprint, render_template, redirect, url_for

app = Blueprint('main', __name__)

@app.route('/')
def index():
    return redirect(url_for('main.main'))

@app.route('/main')
def main():
    return render_template('main.html')

