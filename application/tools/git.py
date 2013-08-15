import os, random 

from dulwich.repo import Repo

REPO_DIR = '/tmp/gitnote'

def generate_id():
    id = '%05d' % random.randint(1, 99999)
#    if id in repos:
#        return generate_id():
    return id

def new_repo():
    repo_id = generate_id()
    repo_path = os.path.join(REPO_DIR, generate_id())

    os.makedirs(repo_path)
    repo = Repo.init_bare(repo_path)

    return repo_id

