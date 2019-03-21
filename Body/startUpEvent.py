import importlib, os
from .gObj import GV


def main():
    GV.table.update()
    for each in GV.table.list_all('isStartup = "1"'):
        if os.path.isdir(each.path):
            print('Import module - %s' % each.name)
            mod = importlib.import_module(each.name + ".startup")
            mod.main()
        else:
            GV.table.update()
            main()
            break
