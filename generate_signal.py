import pandas as pd

# بيانات تجريبية (ممكن نربطها ببيانات حقيقية لاحقاً)
stocks = [
    {"رمز": "KLTO", "السعر": 1.62, "RSI": 32, "MACD": -0.01, "متوافق": True},
    {"رمز": "ADCT", "السعر": 2.35, "RSI": 45, "MACD": 0.05, "متوافق": True},
    {"رمز": "PHUN", "السعر": 1.2, "RSI": 25, "MACD": -0.04, "متوافق": True},
    {"رمز": "SOUN", "السعر": 4.8, "RSI": 65, "MACD": 0.12, "متوافق": False},
    {"رمز": "VTVT", "السعر": 0.97, "RSI": 28, "MACD": -0.02, "متوافق": True},
    {"رمز": "CEI", "السعر": 0.55, "RSI": 72, "MACD": 0.15, "متوافق": False},
]

df = pd.DataFrame(stocks)

# فلترة الأسهم حسب معايير فنية وشرعية
filtered = df[
    (df["السعر"] < 5) &
    (df["RSI"] < 35) &
    (df["MACD"] < 0) &
    (df["متوافق"] == True)
]

# اختيار أفضل سهم بناءً على وزن: RSI منخفض + سعر أعلى
def score(row):
    return (35 - row["RSI"]) + (row["السعر"])
filtered["التقييم"] = filtered.apply(score, axis=1)
best = filtered.sort_values(by="التقييم", ascending=False).iloc[0]

# تجهيز التوصية
entry = round(best["السعر"], 2)
stop = round(entry * 0.95, 2)
target1 = round(entry * 1.10, 2)
target2 = round(entry * 1.20, 2)

message = f"""
🚀 توصية ذكية اليوم من شاتشت

📈 السهم: {best['رمز']}
• السعر الحالي: {entry}
• وقف الخسارة: {stop}
• الهدف الأول: {target1}
• الهدف الثاني: {target2}
• RSI: {best['RSI']}
• MACD: {best['MACD']}
• الشرعية: ✅ متوافق مع الشريعة

📡 تم اختيار السهم بناء على تحليل فني تلقائي.
"""

# حفظ التوصية ليرسلها السكربت الثاني
with open("signal.txt", "w") as f:
    f.write(message)
