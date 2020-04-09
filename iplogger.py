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

print("IP :", values.get('query'))
print("STATUS :",  values.get('status'))
print("COUNTRY :", values.get('country'))
print("COUNTRY CODE :", values.get('countryCode'))
print("REGION :", values.get('region'))
print("CITY :", values.get('city'))
print("ZIP :", values.get('zip'))
print("LAT :", str(values.get('lat')))
print("LON :", str(values.get('lon')))
print("TIMEZONE :", values.get('timezone'))
print("ISP NAME :", values.get('isp'))

