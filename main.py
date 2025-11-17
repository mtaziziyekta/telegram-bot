import time
import requests

TOKEN = "8537291990:AAGLZNHBNcWt8_hZOM_GLOs3xDko81f5_yE"
CHAT_ID = "-1003370854323"
MESSAGE = "یا حسین"

def send_message():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": MESSAGE}
    response = requests.post(url, data=data)
    print("Status:", response.status_code, response.text)

while True:
    send_message()
    time.sleep(360)