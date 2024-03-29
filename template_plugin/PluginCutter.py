from apis.CutterApi import CutterApi
from gui.PluginGui import PluginGui

import PySide2.QtWidgets as QtWidgets
import cutter


class PluginWidget(cutter.CutterDockWidget):
    def __init__(self, parent):
        super(PluginWidget, self).__init__(parent)
        self.main = parent
        self.setObjectName("TODO_PLUGIN_NAME")
        self.setWindowTitle("TODO_PLUGIN_NAME")

        self.api_proxy = CutterApi()
        self.plugin_gui = PluginGui(self.api_proxy)
        content = QtWidgets.QWidget()
        self.setWidget(content)
        content.setLayout(self.plugin_gui.layout)


class HyaraPlugin(cutter.CutterPlugin):
    name = "TODO_PLUGIN_NAME"
    description = "TODO_PLUGIN_DESCRIPTION"
    version = "TODO_PLUGIN_VERSION"
    author = "TODO_AUTHOR"
    plugin_widget = None

    def setupPlugin(self):
        pass

    def nop(self):
        return

    def setupActions(self):
        self.dummyAction = QtWidgets.QAction("Dummy Action")

        # context menu extensions / actions need to be registered here
        menu = self.plugin_widget.main.getContextMenuExtensions(
            cutter.MainWindow.ContextMenuType.Disassembly
        )
        menu.addSeparator()
        menu.addAction(self.dummyAction)
        self.startAddrAction.triggered.connect(self.nop)

    def setupInterface(self, main):
        self.plugin_widget = PluginWidget(main)
        self.setupActions()
        main.addPluginDockWidget(self.plugin_widget)

    def terminate(self):
        pass
