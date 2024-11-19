import asyncio
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
