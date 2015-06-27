__author__ = 'spedmonkey'
#best commit ever

import json
import datetime
myList=[]
myData = {'This':13, "awww":14, 'time':'24:00'}

#Read data from .json file
try:
    with open('/home/spedmonkey/PycharmProjects/jsonTest/data') as data_file:
        asdf = json.load(data_file)
except:
    pass

#Create list to write
try:
    myList=asdf
    myList.append(myData)
except:
    myList = [myData]

#write data to .json file,,in this case a list of dictionaries.
with open('/home/spedmonkey/PycharmProjects/jsonTest/data', mode='w') as feedsjson:
    json.dump(myList, feedsjson, indent=4)
    feedsjson.write('\n')