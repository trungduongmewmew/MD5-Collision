import hashlib
import requests
string1 = "TEXTCOLLBYfGiJUETHQ4hAcKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak"
string2 = "TEXTCOLLBYfGiJUETHQ4hEcKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak"
url = 'http://172.104.49.143:1608/'  
data = {
    'a': string1,
    'b': string2
}
response = requests.post(url, data=data)
if "flag" in response.text:
    print("Flag tìm thấy:", response.text)
