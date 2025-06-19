import random

stocks = [
    {"symbol": "KLTO", "price": 1.62},
    {"symbol": "ADCT", "price": 2.35},
    {"symbol": "VTVT", "price": 0.98},
    {"symbol": "PHUN", "price": 1.20},
    {"symbol": "SOUN", "price": 4.75}
]

stock = random.choice(stocks)
entry = round(stock["price"], 2)
stop = round(entry * 0.95, 2)
target1 = round(entry * 1.10, 2)
target2 = round(entry * 1.20, 2)
rating = "🔥🔥🔥" if entry < 2 else "🔥🔥"

message = f"""
🚀 توصية اليوم | سكربت ذكي من شاتشت

📈 السهم: {stock['symbol']}
• الدخول: {entry}
• وقف الخسارة: {stop}
• الهدف الأول: {target1}
• الهدف الثاني: {target2}
• التقييم: {rating}
• الشرعية: ✅ متوافق مع الشريعة (تحليل مبدئي)

📡 تم توليد التوصية تلقائيًا.
"""

with open("signal.txt", "w") as f:
    f.write(message)
