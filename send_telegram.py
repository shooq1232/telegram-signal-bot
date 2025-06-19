import requests

BOT_TOKEN = '7690624543:AAHMukzxEfMRbb4LK94zkOxNO8AEAN4G3J4'
CHAT_ID = '168259494'

message = """
🚀 توصية اليوم | من شاتشت شخصيًا

📈 السهم: KLTO
• الدخول: 1.62
• وقف الخسارة: 1.55
• الهدف الأول: 1.80
• الهدف الثاني: 1.95
• التقييم: 🔥🔥🔥
• الشرعية: ✅ متوافق مع الشريعة (فلتر مبدئي)

📡 تنبيه تجريبي للتأكد إن البوت شغال.
"""

def send_telegram():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    res = requests.post(url, data=data)
    print("✅ تم الإرسال" if res.ok else f"❌ خطأ: {res.text}")

send_telegram()
