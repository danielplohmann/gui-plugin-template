class ApiProxy(object):
    
    def __init__(self):
        pass

    def get_filepath(self) -> str:
        raise NotImplementedError

    def get_md5(self) -> str:
        raise NotImplementedError

    def jump_to(self, addr):
        raise NotImplementedError
