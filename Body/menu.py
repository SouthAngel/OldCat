from maya import cmds


MENU_ROOT = ("IDOldCatMenu", "Cat")
MENU_DATA = (
    ("Open", "print('Open')"),
    ("Favorite", None),
    ("Settings", None),
    ("Document", None),
    ("About...", None),
)


class Menu(object):
    def __init__(self):
        super(Menu, self).__init__()
        self.name = "Old cat plugin"
        self.parent = None
        self.command = None
        self.childern = list()
    
    def create(self):
        argv = {
            "label" : self.name
        }
        if self.command:
            argv["command"] = self.command
        if self.childern:
            argv["tearOff"] = True
            argv["subMenu"] = True
        if self.parent:
            argv["parent"] = self.parent
        self.name = cmds.menuItem(**argv)


def createAppendMenuBar():
    print("Create menu UI")
    if cmds.menu(MENU_ROOT[0], q=1, ex=1):
        cmds.deleteUI(MENU_ROOT[0])
    cmds.setParent('MayaWindow')
    cmds.menu(MENU_ROOT[0], l=MENU_ROOT[1], to=1)
    cmds.menuItem(c='print(\'Test Print\')', l='TestButton')
    for each in iter(MENU_DATA):
        mi = Menu()
        mi.name = each[0]
        if each[1]:
            mi.command = each[1]
        mi.create()