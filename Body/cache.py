import os, sqlite3
from .gObj import GV


class Friend(object):

    def __init__(self):
        super(Friend, self).__init__()
        self.name = "None"
        self.path = "None"
        self.iconType = "0"
        self.docType = "0"
        self.isStartup = "0"
        self.isEnable = "1"


class DataBaseTable(object):

    def __init__(self, dtb):
        super(DataBaseTable, self).__init__()
        self.heads = []
        self.sq = dtb.sq
    
    def create_table_if_not_exists(self, keys):
        self.heads = keys
        command = "CREATE TABLE IF NOT EXISTS %s(" % self.__class__.__name__
        command = command + ", ".join(['%s TEXT' % x for x in keys]) + ");"
        self.sq.execute(command)


class Cacher(DataBaseTable):

    def __init__(self, dtb):
        super(Cacher, self).__init__(dtb)
        self.create_table_if_not_exists(Friend().__dict__.keys())
    
    def update(self):
        print("Update cacher")
        print(os.listdir(GV.assetPath))


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
