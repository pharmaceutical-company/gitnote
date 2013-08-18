import re

from flask import Blueprint, g, render_template, redirect, url_for, request

from application.model import Note
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
    note_name = 'gitnote'
    file_list = []
    for key in request.form:
        if not re.match(r'^gitnote\/(.*)', key):
            continue
        name = re.findall(r'^gitnote\/(.*)', key)[0]
        name = name.strip()
        data = str(request.form[key])
        if note_name is 'gitnote' and name:
            note_name = name
        if name or data:
            #file_list.append((name, data))
            file_list.append((name or 'gitnote%d' % len(file_list), data))
    if not len(file_list):
        return render_template('editor.html')

    note = Note(name=note_name, description='')
    with g.session.begin():
        g.session.add(note)

    repo = git.new_repo(note.id)
    for name, data in file_list:
        repo.stage_data(name, data)
    commit_id = repo.do_commit('Gitnote',
                                committer='gitnote <gitnote@gitnote.com>')
            
    return redirect('/%d/view' % note.id)

@app.route('/<int:id>/view')
def view(id):
    return render_template('editor.html', note=note)

@app.route('/edit')
def edit():
    return render_template('editor.html')

