# -*- coding:utf-8 -*-
import sys


def __run_from(*args):
    if args:
        if args[0] not in sys.path:
            sys.path.insert(0, args[0])
    import OldCat.Awake.main as brun
    brun.main()
