from geopy import geocoders
import json
import random
import sys

keys = ['sperigo1', 'sperigo2', 'sperigo3', 'sperigo4', 'sperigo5']

text = ["Over [X] of [Y] companies are based in [Z].", "[Z] is home to [X] of [Y] startups.", "With [X] of companies located here, [Z] is a leader in the [Y] industry."]

def generate_text(info):
    template = random.choice(text)
    city = info["city"].split(",")[0]
    percent = "{:.2%}".format(info["percent"])
    industry = info["category"].lower()
    result = template.replace("[X]", percent).replace("[Y]", industry).replace("[Z]", city)
    return result

with open('data.json') as f:
    data = json.load(f)
    for i in data:
        if "coordinates" not in i:
            try:
                location = geocoders.GeoNames(username=random.choice(keys)).geocode(i["city"])
                if location == None:
                    continue
                i["coordinates"] = [location.longitude, location.latitude]
            except:
                print i["city"]
        if "text" not in i:
            i["text"] = generate_text(i)

    with open('clean.json', 'w') as outfile:
        json.dump(data, outfile)
