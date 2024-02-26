import binascii
import hashlib

import java.io

from .ApiProxy import ApiProxy


from ghidra.program.util import DefinedDataIterator
from ghidra.util import MD5Utilities

class GhidraApi(ApiProxy):
    def __init__(self):
        super(GhidraApi, self).__init__()

    def get_filepath(self) -> str:
        filepath = getState().getCurrentProgram().getExecutablePath()
        return filepath[1:]

    def get_md5(self) -> str:
        return MD5Utilities.getMD5Hash(java.io.File(self.get_filepath()))

    def jump_to(self, addr):
        goTo(toAddr(addr))