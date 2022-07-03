
from timeit import default_timer as timer
from datetime import timedelta
from mordecai import Geoparser
import json
geo = Geoparser()

print("Enging Started ... \n")

stat = True

while stat:

    user_input = input("\n\n Ask about any thing include cities name to see Result(send 0 >> close the app) \n\n >>>")
    start = timer()

    if user_input == "0":
        stat = False

    result = geo.geoparse(user_input)

    print("\n")

    if len(result) == 0:
        print("include City name isn't valid")

    for i in result:
        try:
            print(i["word"])
            print(f"country predicted:{i['country_predicted']}")
            print(f"Country name: {i['geo']['admin1']}")
            print(f"cordinate: {i['geo']['lat']}X{i['geo']['lon']}")
            print(f"Place name: {i['geo']['place_name']}")
            print("\n\n")
        except KeyError:
            print(i)



    end = timer()
    print(timedelta(seconds=end-start))
    


# You can see more advanced technology in Tehran in comparison with Kabul
# Berlin is the largest city in Germany by population and area.
# It's just a five minute flight between Kinshasa and Brazzaville, which border the Congo River.
