

def main(*args):
    PATH_ADDTIONS = args

    import sys, os

    for p in PATH_ADDTIONS:
        if p not in sys.path:
            sys.path.insert(0, p)
            print('Add env path : %s' % p)

    import OldCat.Awake.main as olm
    olm.main()


if __name__ == "__main__":
    print("Run execFrom")
    main(
        r"\\192.168.3.45\Users\PengCheng\Temp\OldCatDevelop",
    )