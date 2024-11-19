import sys
import os
import asyncio
from modul.proxy_handler import main  # Impor modul utama

# Menambahkan jalur proyek ke sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

async def main_script():
    # Coba membaca user_id dari file data/userid.txt
    try:
        with open('data/userid.txt', 'r') as f:
            user_id = f.read().strip()  # Menghapus spasi ekstra atau baris kosong
        if not user_id:
            raise ValueError("user_id kosong di dalam file userid.txt.")
    except FileNotFoundError:
        print("File data/userid.txt tidak ditemukan.")
        return
    except ValueError as ve:
        print(ve)
        return

    # Jalankan fungsi main dengan jalur proxy yang diperbarui di folder bahan
    proxy_file_path = 'bahan/proxy_1.txt'  # Menggunakan file proxy dari folder bahan
    try:
        await main(proxy_file_path, user_id)
    except FileNotFoundError:
        print(f"File proxy {proxy_file_path} tidak ditemukan. Pastikan file tersebut ada di folder bahan.")

if __name__ == "__main__":
    asyncio.run(main_script())
