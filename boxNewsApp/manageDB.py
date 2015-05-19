__author__ = 'A.Hosseini'

import sqlite3
from boxNews.settings import BASE_DIR


class controlDb:

    def __init__(self):
        self.pathDb = BASE_DIR + '\db.sqlite3'
        self.db = sqlite3.connect(self.pathDb)


class controlData:

    def __init__(self):
        self.pathDb = BASE_DIR + '\data.db'
        self.db = sqlite3.connect(self.pathDb)


