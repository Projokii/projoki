import sys
import os
import asyncio

# Tambahkan jalur induk dari folder `program` ke sys.path untuk memastikan modul lain dapat ditemukan
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import modul utama setelah sys.path diperbarui
try:
    from modul.proxy_handler import main
except ModuleNotFoundError:
    print("Folder `modul` atau file `proxy_handler.py` tidak ditemukan di dalam `modul`.")
    sys.exit(1)

async def main_script():
    # Path ke file user_id dan proxy
    user_id_path = '../data/userid.txt'
    proxy_file_path = '../bahan/proxy_1.txt'

    # Baca user_id dari file data/userid.txt
    try:
        if not os.path.exists(user_id_path):
            print(f"File {user_id_path} tidak ditemukan.")
            return

        with open(user_id_path, 'r') as f:
            user_id = f.read().strip()
            if not user_id:
                print("File userid.txt kosong. Harap masukkan user_id yang valid.")
                return

    except Exception as e:
        print(f"Terjadi kesalahan saat membaca user_id: {e}")
        return

    # Pastikan file proxy ada
    if not os.path.exists(proxy_file_path):
        print(f"File proxy {proxy_file_path} tidak ditemukan. Pastikan file tersebut ada di folder bahan.")
        return

    # Jalankan fungsi main dengan user_id dan path proxy yang valid
    try:
        await main(proxy_file_path, user_id)
    except FileNotFoundError as e:
        print(f"Kesalahan file: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan saat menjalankan main: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main_script())
    except Exception as e:
        print(f"Kesalahan umum: {e}")
