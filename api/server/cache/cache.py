import json
import os

class Cache(object):


    def __init__(self):
        pass

    def has(self, _id) -> bool:

        return os.path.exists(f'{_id}.eac')

    def write_record(self, _id, obj):
        
        with open(f'obj_{_id}.eac', 'w') as fp:
            try:
                json.dump(obj, fp)
            except Exception as e:
                print(e)

    def read_record(self, _id) -> object:
        
        with open(f'obj_{_id}.eac', 'r') as fp:
            try:
                obj = json.load(fp)
                return obj
            except Exception as e:
                print(e)

    def write_img(self, _id, content):

        with open(f'img_{_id}.eac', 'wb') as fp:
            try:
                fp.write(content) 
            except Exception as e:
                print(e)


    def read_img(self, _id) -> bytes:

        with open(f'img_{_id}.eac', 'rb') as fp:
            try:
                img = fp.read()
                return img
            except Exception as e:
                print(e)

    def push(self):

        '''
            Pushes all serialized objects to persistent data store.

        '''

        pass