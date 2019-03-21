import os
import sqlite3
from .gObj import GV


class Friend(object):

    def __init__(self):
        super(Friend, self).__init__()
        self.name = "None"
        self.path = "None"
        self.iconType = "0"
        self.docType = "0"
        self.isStartup = "0"
        self.star = "0"


_FREF_ATTRS = Friend().__dict__.keys()


class DataBaseTable(object):

    def __init__(self, dtb):
        super(DataBaseTable, self).__init__()
        self.tableName = self.__class__.__name__
        self.heads = []
        self.sq = dtb.sq

    def create_table_if_not_exists(self, keys):
        self.heads = keys
        command = "CREATE TABLE IF NOT EXISTS %s(" % self.tableName
        command = command + ", ".join(['%s TEXT' % x for x in keys]) + ");"
        self.sq.execute(command)
        self.sq.commit()


class Cacher(DataBaseTable):

    def __init__(self, dtb):
        super(Cacher, self).__init__(dtb)
        self.create_table_if_not_exists(_FREF_ATTRS)

    def update(self):
        self.sq.execute("DELETE FROM " + self.tableName)
        self.sq.commit()
        founds = []
        for each in iter(os.listdir(GV.assetPath)):
            cPath = '%s/%s' % (GV.assetPath, each)
            if os.path.isfile(cPath + "/main.py"):
                newItem = Friend()
                newItem.name = each
                newItem.path = cPath.replace("\\", "/")
                if os.path.isfile(cPath + "/icon.png"):
                    newItem.iconType = "1"
                if os.path.isfile(cPath + "/doc/index.txt"):
                    newItem.docType = "1"
                elif os.path.isfile(cPath + "/doc/index.html"):
                    newItem.docType = "2"
                if os.path.isfile(cPath + "/startup.py"):
                    newItem.isStartup = "1"
                command = 'INSERT INTO %s (%s) VALUES (%s)' % (
                    self.tableName,
                    ", ".join(_FREF_ATTRS),
                    ", ".join(['"%s"' % x for x in newItem.__dict__.values()])
                    )
                self.sq.execute(command)
        self.sq.commit()

    def list_all(self, filterStr=None):
        command = "SELECT * FROM %s" % self.tableName
        if filterStr:
            command += " WHERE %s" % filterStr
        cu = self.sq.execute(command)
        ret = []
        for each in cu:
            newItem = Friend()
            for i, k in enumerate(_FREF_ATTRS):
                newItem.__setattr__(k, each[i])
            ret.append(newItem)
        print ret
        print [x.__dict__ for x in ret]
        return ret


class Dictionary(DataBaseTable):

    def __init__(self, dtb):
        super(Dictionary, self).__init__(dtb)
        self.create_table_if_not_exists(["key", "value"])


class Data(object):
    DATA_FILE = GV.tempPath + "/data.db"

    def __init__(self):
        super(Data, self).__init__()
        print(self.DATA_FILE)
        self.sq = sqlite3.connect(self.DATA_FILE)
        self.cacher = Cacher(self)
        self.dict = Dictionary(self)

    def __del__(self):
        self.sq.commit()
        self.sq.close()
        super(Cacher, self).__del__()


SQ = Data()
GV.table = SQ.cacher
GV.dbOther = SQ.dict
