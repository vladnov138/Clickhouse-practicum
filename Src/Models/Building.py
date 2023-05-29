from Src.Models.Constructor import Constructor

import json

class Building:
    __name = None
    __location = None
    
    def __init__(self, name: str, location: str):
        self.__name = name
        self.__location = location
        
    def toJSON(self):
        res = {
            "name": self.__name,
            "location": self.__location
        }
        return json.dumps(res)