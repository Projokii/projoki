import asyncio
from modul.proxy_handler import main  # Import sesuai struktur modul

async def main_script():
    try:
        # Membaca user_id dari file userid.txt yang ada di folder 'data'
        with open('data/userid.txt', 'r') as f:
            user_id = f.read().strip()
    except FileNotFoundError:
        print("File 'data/userid.txt' tidak ditemukan.")
        return

    # Panggil fungsi main() yang ada di proxy_handler.py, dengan file proxy_1.txt dari folder 'bahan'
    await main('bahan/proxy_1.txt', user_id)

if __name__ == "__main__":
    asyncio.run(main_script())
