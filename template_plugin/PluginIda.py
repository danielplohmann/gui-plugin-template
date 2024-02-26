from plugin.apis.IdaApi import IdaApi
from plugin.gui.PluginGui import PluginGui

import ida_kernwin
import idaapi


class Plugin_action_handler_t(idaapi.action_handler_t):
    def __init__(self, dummy_arg):
        idaapi.action_handler_t.__init__(self)
        return

    def activate(self, ctx):
        # some action
        return 1

    def update(self, ctx):
        return idaapi.AST_ENABLE_ALWAYS


class Hooks(ida_kernwin.UI_Hooks):
    def __init__(self):
        ida_kernwin.UI_Hooks.__init__(self)

    def finish_populating_widget_popup(self, widget, popup):
        ida_kernwin.attach_action_to_popup(widget, popup, "TODO_IDA_ACTION_NAME", None)


class PluginWidget(ida_kernwin.PluginForm):

    def OnCreate(self, form):
        self.parent = self.FormToPyQtWidget(form)
        self.api_proxy = IdaApi()
        self.plugin_gui = PluginGui(self.api_proxy)
        self.parent.setLayout(self.plugin_gui.layout)

        # context menu extensions / actions need to be registered here
        idaapi.register_action(
            ida_kernwin.action_desc_t(
                "TODO_IDA_ACTION_NAME",
                "TODO_ACTION_DESCRIPTION",
                Plugin_action_handler_t("DummyArg"),
                "Ctrl+Shift+S",
                "TODO_ACTION_DESCRIPTION",
            )
        ),

    def OnClose(self, form):
        idaapi.unregister_action("TODO_IDA_ACTION_NAME")
        hooks.unhook()


class TemplatePlugin(idaapi.plugin_t):
    # https://www.hex-rays.com/products/ida/support/sdkdoc/group___p_l_u_g_i_n__.html
    flags = idaapi.PLUGIN_UNL
    comment = "TODO_PLUGIN_DESCRIPTION"
    help = "help"
    wanted_name = "TODO_PLUGIN_NAME"
    wanted_hotkey = "Ctrl+Shift+Y"

    def init(self):
        global hooks
        hooks = Hooks()
        hooks.hook()
        return idaapi.PLUGIN_OK

    def run(self, arg):
        plg = PluginWidget()
        plg.Show("TODO_PLUGIN_NAME")

        try:
            widget_a = ida_kernwin.find_widget("IDA View-A")
            widget_template_plugin = ida_kernwin.find_widget("TODO_PLUGIN_NAME")
            if widget_template_plugin and widget_a:
                ida_kernwin.set_dock_pos("TODO_PLUGIN_NAME", "IDA View-A", ida_kernwin.DP_RIGHT)
        except:
            print("find_widget option is available version 7.0 or later")

    def term(self):
        pass


def PLUGIN_ENTRY():
    return TemplatePlugin()
