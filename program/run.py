import asyncio
import sys
import os

# Menambahkan path ke folder utama "projoki" agar modul dapat ditemukan
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modul.proxy_handler import main

async def main_script():
    try:
        with open('../data/userid.txt', 'r') as f:
            user_id = f.read().strip()
    except FileNotFoundError:
        print("File 'userid.txt' tidak ditemukan.")
        return

    await main('../data/proxy_1.txt', user_id)

if __name__ == "__main__":
    asyncio.run(main_script())
