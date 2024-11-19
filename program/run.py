import asyncio
import os
from modul.proxy_handler import main  # Import fungsi utama

async def main_script():
    # Gunakan path absolut untuk file userid.txt
    user_id_path = os.path.abspath('../data/userid.txt')
    if not os.path.exists(user_id_path):
        print(f"File {user_id_path} tidak ditemukan.")
        return

    with open(user_id_path, 'r') as f:
        user_id = f.read().strip()  # Membaca user_id dari file userid.txt

    # Menjalankan fungsi main dengan user_id
    await main('bahan/proxy_1.txt', user_id)  # Pastikan path proxy benar

if __name__ == "__main__":
    asyncio.run(main_script())
