import json

class Company:
    __name = None
    __id = None
    
    def __init__(self, name: str):
        __name = name
    
    def toJSON(self):
        return json.dumps({"name": self.__name})