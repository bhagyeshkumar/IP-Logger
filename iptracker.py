import os
from urllib.request import urlopen
import json

while True: 
    ip = input("Enter Your Target IP:")
    #ip = input("123.201.225.43");
    url = "http://ip-api.com/json/"
    response = urlopen(url + ip)
    data = response.read()
    values = json.loads(data)
    print("IP :" + values['query'])
    print("STATUS :" + values['status'])
    print("COUNTRY :" + values['country'])
    print("COUNTRY CODE :" + values['countryCode'])
    print("REGION :" + values['region'])
    print("CITY :" + values['city'])
    print("ZIP :" + values['zip'])
    print("LAT :" + str(values['lat']))
    print("LON :" + str(values['lon']))
    print("TIMEZONE :" + values['timezone'])
    print("ISP NAME :" + values['isp'])
    break
