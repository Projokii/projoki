import asyncio
import sys
import os

# Menambahkan path modul ke sys.path agar Python dapat menemukan file proxy_handler.py
sys.path.append(os.path.join(os.path.dirname(__file__), '../modul'))

# Mengimpor fungsi main dari proxy_handler
from proxy_handler import main

async def main_script():
    try:
        # Membaca user_id dari file userid.txt yang ada di folder 'data'
        with open('../data/userid.txt', 'r') as f:
            user_id = f.read().strip()  # Menghapus spasi atau karakter tak terlihat
    except FileNotFoundError:
        print("File 'userid.txt' tidak ditemukan.")
        return

    # Menjalankan fungsi main dari proxy_handler dan memberikan proxy_1.txt serta user_id sebagai parameter
    await main('../bahan/proxy_1.txt', user_id)

# Menjalankan skrip utama
if __name__ == "__main__":
    asyncio.run(main_script())
