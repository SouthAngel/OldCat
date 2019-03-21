from maya import cmds
from OldCat import Db


## -- Window
class WindowList(object):
    WIN_ID = "IDW_OLDCAT_LIST_ALL_WIN"
    MAX_ITEM_COUNT = 10

    def __init__(self):
        self._ui_items = [None] * self.MAX_ITEM_COUNT
        self._items = []
        self._item_layout = None

        self.destroy()
        if not cmds.window(self.WIN_ID, q=1, ex=1):
            self.WIN_ID = cmds.window(self.WIN_ID)
            self._item_layout = cmds.columnLayout(adj=1)
            for i in xrange(self.MAX_ITEM_COUNT):
                self._ui_items[i] = cmds.button(vis=0)
            self.update_context()
        cmds.showWindow(self.WIN_ID)

    def update_context(self):
        self._items = Db.list_all()
        cNum = len(self._items)
        for i in xrange(self.MAX_ITEM_COUNT):
            buttonId = self._ui_items[i]
            if i < cNum:
                pluginName = self._items[i].name
                cmds.button(buttonId, e=1,
                            l=pluginName, c='import {m}.main\n{m}.main.main()'.format(m=pluginName), vis=1)
            else:
                cmds.button(self._ui_items[i], e=1, vis=0)

    def destroy(self):
        if cmds.window(self.WIN_ID, q=1, ex=1):
            cmds.deleteUI(self.WIN_ID)

    def show(self):
        cmds.showWindow(self.WIN_ID)


def main():
    WindowList().show()
