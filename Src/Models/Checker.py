from Src.Models.Company import Company

import json

class Checker:
    __name = None
    __company = None
    
    def __init__(self, name: str, company: Company) -> None:
        self.__name = name
        self.__company = company
        
    def toJSON(self):
        res = {
            "name": self.__name,
            "company": self.__company.toJSON()
        }
        return json.dumps(res)