import re

from flask import Blueprint, render_template, redirect, url_for, request

from application.tools import git

app = Blueprint('main', __name__)

@app.route('/')
def index():
    return redirect(url_for('main.list'))

@app.route('/list')
def list():
    return render_template('list.html')

@app.route('/new', methods=['GET'])
def new():
    return render_template('editor.html')

@app.route('/new', methods=['POST'])
def new_post():
    repo = git.new_repo() 
    file_list = []
    for key in request.form:
        if not re.match(r'^gitnote\/(.*)', key):
            continue
        name = re.findall(r'^gitnote\/(.*)', key)[0]
        data = str(request.form[key])
        repo.stage_data(name, data)
    commit_id = repo.do_commit('Gitnote',
                                committer='gitnote <gitnote@gitnote.com>')
            
    return render_template('editor.html')

@app.route('/edit')
def edit():
    return render_template('editor.html')

@app.route('/view')
def view():
    return render_template('view.html')

