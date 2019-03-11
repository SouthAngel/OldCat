import sys, os, cPickle
import SuperReload.startup as st

def main():
    if os.path.isfile(st.DATA_FILE_PATH):
        with open(st.DATA_FILE_PATH, "rb") as opf:
            ks = cPickle.load(opf)
        for k in iter(ks):
            del sys.modules[k]
