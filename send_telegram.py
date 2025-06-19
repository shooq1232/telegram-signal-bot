import requests

BOT_TOKEN = '7690624543:AAHMukzxEfMRbb4LK94zkOxNO8AEAN4G3J4'
CHAT_ID = '168259494'

# نقرأ التوصية من ملف تم توليده
with open("signal.txt", "r") as f:
    message = f.read()

def send_telegram():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    res = requests.post(url, data=data)
    print("✅ تم الإرسال" if res.ok else f"❌ خطأ: {res.text}")

send_telegram()
