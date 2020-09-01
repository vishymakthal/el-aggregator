import json
import os

class Cache(object):


    def __init__(self):
        pass

    def record_exists_for(self, _id):

        return os.path.exists(f'{_id}.json')

    def write_record(self, _id, obj):
        
        with open(f'{_id}.json', 'w') as fp:
            try:
                json.dump(obj, fp)
            except Exception as e:
                print(e)

    def read_record(self, _id):
        
        with open(f'{_id}.json', 'r') as fp:
            try:
                obj = json.load(fp)
                return obj
            except Exception as e:
                print(e)

    def push(self):

        '''
            Pushes all serialized objects to persistent data store.

        '''

        pass