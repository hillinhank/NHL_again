from db import CreateRecord
from NHL import N2_API
from config import NHL_ACCESS_KEY


if __name__=="__main__":
    print("start process!")

#    print(NHL_ACCESS_KEY+"conferences")

#
    for data in nhl_conf_data:
        w_conf_data=N2_API(data)

        CreateRecord().Conferences(
            name=w_conf_data['data']
            )
    print("DONE!")


