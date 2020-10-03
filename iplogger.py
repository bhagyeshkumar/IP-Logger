# Grabbing Banners, Hostname and IP Lookup
import os
import sys
import requests
import socket
import json
import time

def animation():
    animation = "|/-\\"
    for i in range(10):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

os.system('cls')
animation()
if len(sys.argv) < 2:
    print("Usage: " +sys.argv[0]+ " <url>")
    sys.exit(1)

print(""" -----------------------------------
|        IP - L O G G E R           |
 -----------------------------------""")

print("\n\nFetching Headers Info ...")

req = requests.get("http://"+sys.argv[1])
print("\n"+str(req.headers))

ip = socket.gethostbyname(sys.argv[1])
print("\n\nThe IP address of <" +sys.argv[1]+ "> is : [" +ip+ "]\n")

print("\nFetching IP Information ...\n\n")

# response = requests.get("https://ipinfo.io/" +ip+ "/json")
response = requests.get("http://ip-api.com/json/" +ip)
data = response.text
values = json.loads(data)

print("IP :", values.get('query','Not Available'))
print("STATUS :",  values.get('status','Not Available'))
print("COUNTRY :", values.get('country','Not Available'))
print("COUNTRY CODE :", values.get('countryCode','Not Available'))
print("REGION :", values.get('region','Not Available'))
print("CITY :", values.get('city','Not Available'))
print("ZIP :", values.get('zip','Not Available'))
print("LAT :", str(values.get('lat','Not Available')))
print("LON :", str(values.get('lon','Not Available')))
print("TIMEZONE :", values.get('timezone','Not Available'))
print("ISP NAME :", values.get('isp','Not Available'))

