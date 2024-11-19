import asyncio
from modul.proxy_handler import main  # Impor sesuai folder

async def main_script():
    try:
        with open('data/userid.txt', 'r') as f:
            user_id = f.read().strip()  # Membaca user_id dari file
    except FileNotFoundError:
        print("File 'data/userid.txt' tidak ditemukan.")
        return

    # Memulai fungsi main dari proxy_handler.py, menggunakan file proxy_1.txt
    await main('bahan/proxy_1.txt', user_id)

if __name__ == "__main__":
    asyncio.run(main_script())
