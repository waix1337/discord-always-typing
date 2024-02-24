import requests
import time
from datetime import datetime
import colorama

channel = 1111111111111111111 # Replace this with your channel ID
token = "Your Token" # Replace with your token

colorama.init()

data = {
    "Authorization": token
}

url = f"https://discord.com/api/v9/channels/{channel}/typing"

while True:
    r = requests.post(url, headers=data)
    if r.status_code == 204:
        color = colorama.Fore.GREEN
    else:
        color = colorama.Fore.RED 
    print(colorama.Fore.LIGHTBLACK_EX + str(datetime.now().strftime("%H:%M:%S")) + colorama.Fore.RESET +  " > " + color + str(r.status_code))
    time.sleep(7)