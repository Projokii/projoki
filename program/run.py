import asyncio
from modul.proxy_handler import main

async def main_script():
    # Membaca user_id dari file data/userid.txt
    with open('data/userid.txt', 'r') as f:
        user_id = f.read().strip()

    # Menjalankan main dengan path proxy di folder bahan
    await main('bahan/proxy_1.txt', user_id)

if __name__ == "__main__":
    asyncio.run(main_script())
