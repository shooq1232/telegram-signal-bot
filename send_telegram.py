import requests

BOT_TOKEN = 'توكن البوت هنا'
CHAT_ID = 'رقم الشات ID'

# قراءة التوصية من الملف
with open("signal.txt", "r") as file:
    message = file.read()

# إرسال التوصية إلى تيليجرام
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": message
}

response = requests.post(url, data=payload)

# طباعة الحالة
print("تم الإرسال بنجاح ✅" if response.status_code == 200 else f"فشل الإرسال ❌ {response.text}")
