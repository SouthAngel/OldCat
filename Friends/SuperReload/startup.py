import sys
import os
import cPickle


DATA_FILE_PATH = os.path.join(os.getenv("TEMP"), "superReload.rd")


def main():
    if not os.path.isfile(DATA_FILE_PATH):
        with open(DATA_FILE_PATH, "wb") as opf:
            cPickle.dump(sys.modules.keys(), opf)