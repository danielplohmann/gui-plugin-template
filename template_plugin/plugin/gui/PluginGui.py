import traceback
from sys import modules


if "idaapi" in modules:
    # We are running inside IDA
    from PyQt5 import QtWidgets
else:
    # We are running inside Cutter, Binary Ninja or Ghidra
    try:
        import PySide2.QtWidgets as QtWidgets
    except:
        import PySide6.QtWidgets as QtWidgets


class PluginGui():

    def __init__(self, api_proxy) -> None:
        self.layout = QtWidgets.QVBoxLayout()
        self.api_proxy = api_proxy
        # just a single label showing the MD5 as demo
        md5_string = "Could't get MD5, probably a permissions issue"
        try:
            md5_string = f"The current binary has MD5: {self.api_proxy.get_md5()}"
        except Exception:
            print("While trying to obtain the MD5 through ApiProxy, we caught this exception:")
            traceback.print_exc()
        self.layout.addWidget(QtWidgets.QLabel(md5_string))
