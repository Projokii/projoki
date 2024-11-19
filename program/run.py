import asyncio
import sys
import os

# Menambahkan folder modul ke sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modul'))

# Impor fungsi dari proxy_handler yang ada di folder modul
from proxy_handler import main

async def main_script():
    try:
        with open('userid.txt', 'r') as f:
            user_id = f.read().strip()  # Membaca user_id dari file
    except FileNotFoundError:
        print("File 'userid.txt' tidak ditemukan.")
        return

    await main('proxy_1.txt', user_id)  # Menggunakan proxy_1.txt untuk skrip 1.py

if __name__ == "__main__":
    asyncio.run(main_script())
