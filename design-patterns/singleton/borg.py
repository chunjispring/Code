

class Borg:
    """Only apply to classic classes"""
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
    
