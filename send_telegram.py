name: Daily Telegram Signal

on:
  schedule:
    - cron: '0 13 * * *'  # يوميًا الساعة 4 العصر بتوقيت السعودية
  workflow_dispatch:  # لتشغيله يدوي إذا احتجت

jobs:
  run-signal:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: pip install pandas requests

      - name: Generate signal
        run: python generate_signal.py

      - name: Send signal to Telegram
        run: python send_telegram.py
