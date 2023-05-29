from Src.Models.Building import Building
from Src.Models.Checker import Checker
from Src.Models.Constructor import Constructor
from Src.Models.Status import Status
from Src.Models.Company import Company
from Src.Services.Helper import Helper
import json

class Act:
    __checker = None
    __constructor = None
    __object = None
    __status = None
    __mark = None
    __comment = None
    
    def __init__(self, checker: Checker, constructor: Constructor, object: Building, status: Status, 
                 mark: int, comment: str) -> None:
        self.__checker = checker
        self.__constructor = constructor
        self.__object = object
        self.__status = status
        self.__mark = mark
        self.__comment = comment
        
    def toJSON(self):
        res = {
            "checker": self.__checker.toJSON(),
            "constructor": self.__constructor.toJSON(),
            "object": self.__object.toJSON(),
            "status": self.__status.toJSON(),
            "mark": self.__mark,
            "comment": self.__comment
        }
                
        return json.dumps(res)

co = Company("test")
obj = [Building("school", "Irkutsk")]
a = Act(Checker("Vasya", co), Constructor("Ivan", co, obj), obj[0], Status("norm"), 5, "good")
print(a.toJSON())