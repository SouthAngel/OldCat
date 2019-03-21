# -*- coding:utf-8 -*-
import os, sys
from ..Body import gObj, cache, startUpEvent


def main():
    print("Run awake main")
    if gObj.GV.assetPath not in sys.path:
        sys.path.insert(0, gObj.GV.assetPath)
    startUpEvent.main()
