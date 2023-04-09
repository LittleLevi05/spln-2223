import shelve
from shelve import Shelf
import os
import copy
class Archiver:
    def __init__(self):
        self.path: str = os.path.dirname(__file__) + "/db/archive"

    def addStory(self, title: str, bookObj : dict):
        db: Shelf = shelve.open(self.path)
        if db[title]:
            copyDict : dict = copy.deepcopy(db[title])
            copyDict.update(bookObj)
            db[title] = copyDict
        else:
            db[title] = bookObj
        db.close()

    def getStory(self, title: str) -> dict:
        db: Shelf = shelve.open(self.path)
        bookObj = copy.deepcopy(db[title])
        db.close()
        return bookObj
