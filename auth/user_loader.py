
"""Bulk upload users from CSV file.

To bulk upload users, you first need to run "./adhoc/export_users.py <sqllite3-database>". Then from <app-directory> do::

    python2.5 ./appcfg.py upload_data --config_file auth/user_loader.py --filename=./users.csv --kind=User --url http://localhost:8000/remote_api <app-directory>

NOTE: the appcfg.py to use is the one in the project directory, not your 
global one.

"""

import datetime
from google.appengine.ext import db
from google.appengine.tools import bulkloader
from google.appengine.api import datastore_types
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from auth import models, views

#    email:4,first_name:2,last_name:3,password,is_active:7,is_superuser:8
#    last_login:9,date_joined:10,roles

class UserLoader(bulkloader.Loader):
    def __init__(self):
        bulkloader.Loader.__init__(self, 'User',
                                   [('email', lambda e: datastore_types.Email(e.lower())),
                                    ('first_name', str),
                                    ('last_name', str),
                                    ('password', str),
                                    ('is_active', bool),
                                    ('is_superuser', bool),
                                    ('date_joined',lambda x: datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')),
                                    ('roles', str.split)
                                   ])   
    
    def handle_entity(self, entity):
        q = db.GqlQuery("select * from User where email = :1", entity.email)
        if q.fetch(1):
            return None
        else:
            views._reindex(entity)
            print "adding: " + entity.email
            return entity

loaders = [UserLoader]