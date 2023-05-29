from Src.Models.Company import Company

import json

class Constructor:
    __name = None
    __id = None
    __company = None
    __objects = []
    
    def __init__(self, name: str, company: Company, objects: list):
        self.__name = name
        self.__company = company
        self.__objects = objects[:]
        
    def toJSON(self):
        res = {
            "name": self.__name,
            "company": self.__company.toJSON(),
            "objects": [obj.toJSON() for obj in self.__objects]
        }
        return json.dumps(res)
        
    
    
    