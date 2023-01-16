import requests
from db import CreateRecord
from NHL import N2_API
from config import NHL_ACCESS_KEY


if __name__=="__main__":
    print("start process!")

#    print(NHL_ACCESS_KEY+"conferences")
    conf_list=[""]
#
    for x in conf_list:
        nhl_conf = N2_API().get(x)

        CreateRecord().conferences(
            #id=nhl_conf['id'],
            name=nhl_conf['name'],
            link=nhl_conf['link'],
            abbreviation=nhl_conf['abbreviation'],
            shortname=nhl_conf['shortname'],
            active=nhl_conf['active']
            )
    print("DONE!")
