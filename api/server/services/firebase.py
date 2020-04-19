import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class Firebase:

    def __init__(self, cert, db_url):
        self.cred = credentials.Certificate(cert)
        self.default_app = firebase_admin.initialize_app(self.cred, {'databaseURL': db_url})

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

    def delete(self, ref, id):
        obj_ref = self.db.reference(ref).child(id)
        obj_ref.delete()