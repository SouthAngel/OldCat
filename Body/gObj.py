import os


def makeTrueDir(ipath):
    if not os.path.isdir(ipath):
        os.makedirs(ipath)


class GlobalObject(object):

    def __init__(self):
        super(GlobalObject, self).__init__()
        self.tempPath = os.getenv("TEMP").replace("\\", "/") + "/OldCatTemp"
        makeTrueDir(self.tempPath)
        self.workPath = None
        self.assetPath = os.path.dirname(os.path.dirname(__file__)).replace("\\", "/") + "/Friends"
        self.table = None
        self.dbOther = None
        self.tempValues = {}

    def set_workPath(self, ipath):
        self.workPath = ipath.replace("\\", "/")

    def clean_tempValues(self):
        self.tempValues = {}


GV = GlobalObject()
