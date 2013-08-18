import os, random, time

from dulwich.repo import Repo
from dulwich.objects import Blob

REPO_DIR = '/tmp/gitnote'

class NoteRepo(Repo):
    def stage_data(self, name, data):
        from dulwich.index import index_entry_from_stat
        index = self.open_index()

        blob = Blob()
        blob.data = data
        self.object_store.add_object(blob)

        time_now = int(time.time())
        index[name] = (time_now, time_now, 0,
                        0, 0644, 0,
                        0, len(data), blob.id, 0)
        #index[name] = (stat_val.st_ctime, stat_val.st_mtime, stat_val.st_dev,
        #                stat_val.st_ino, 0644, stat_val.st_uid,
        #                stat_val.st_gid, stat_val.st_size, blob.id, 0)
        index.write()

def new_repo(id):
    repo_id = '%d' % id
    repo_path = os.path.join(REPO_DIR, '%s.git' % repo_id)

    os.makedirs(repo_path)
    repo = NoteRepo.init(repo_path)

    return repo

