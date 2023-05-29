from Src.Services.Proxy import db_proxy
from Src.Models.Building import Building
from Src.Models.Checker import Checker
from Src.Models.Constructor import Constructor
from Src.Models.Status import Status
from Src.Models.Company import Company
from Src.Models.Act import Act

import json

def test_connect_database():
    proxy = db_proxy()
    
    proxy.create()
    print(proxy.error_text)
    assert proxy.error_text == ""
    assert proxy.is_error == False
    
def test_json_convert():
    company = Company("Рога и копыта")
    building = Building("Школа", "г. Иркутск")
    constructor = Constructor("Стройка", company, [building])
    checker = Checker("Проверяющий А. А.", company)
    status = Status("Good")
    act = Act(checker, constructor, object, status, 4, "Плохо")
    json_act = act.toJSON()
    
    assert json.load(json_act)['mark'] is not None
    