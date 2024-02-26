import idc
import idautils
import ida_nalt

from .ApiProxy import ApiProxy

class IdaApi(ApiProxy):
    
    def __init__(self):
        pass

    def get_filepath(self) -> str:
        return ida_nalt.get_input_file_path()

    def get_md5(self) -> str:
        return idautils.GetInputFileMD5().hex()

    def jump_to(self, addr):
        idc.jumpto(addr)
