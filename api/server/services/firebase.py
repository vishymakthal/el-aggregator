import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

import json
import glob

class Firebase:

    def __init__(self, cert, db_url, storage_url):
        self.cred = credentials.Certificate(cert)
        self.default_app = firebase_admin.initialize_app(self.cred, {'databaseURL': db_url, 'storageBucket' : storage_url})

    # creates a new entry. will overwrite an entry if it already exists
    def update(self, ref, id, obj=None):
        if not obj:
            return

        obj_ref = self.db.reference(ref).child(id)
        obj_ref.set(obj)

    def read(self, ref, id):
        res = db.reference(ref).child(id).get()
        if res is None:
            return {}
        return res

    def query_by_club(self, ref, club):
        res = db.reference(ref).order_by_child('club').equal_to(club).get()
        if res is None:
            return 404
        return res

    def query_by_name(self, ref, query):
        res = db.reference(ref).order_by_child('short_name').equal_to(query + "\uf8ff").get()
        if res is None:
            return 404
        return res

    def delete(self, ref, id):
        obj_ref = self.db.reference(ref).child(id)
        obj_ref.delete()

    def save_to_storage(self):

        print('pushing to store')
        bucket = storage.bucket()

        for f in glob.glob('./*.eac'):
            blob = bucket.blob(f)
            blob.upload_from_filename(f)

    def read_from_storage(self):

        print('pulling from store')
        bucket = storage.bucket()

        for blob in bucket.list_blobs():
           blob.download_to_filename(blob.name) 
