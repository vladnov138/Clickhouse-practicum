class Status:
    __status = None
    
    def __init__(self, status: str) -> None:
        self.__status = status
        
    def toJSON(self):
        return self.__status
    