import asyncio
import os
from modul.proxy_handler import main

async def main_script():
    user_id_path = os.path.abspath('../data/userid.txt')
    try:
        with open(user_id_path, 'r') as f:
            user_id = f.read().strip()
    except FileNotFoundError:
        print(f"File {user_id_path} tidak ditemukan.")
        return

    proxy_file_path = os.path.abspath('../bahan/proxy_1.txt')
    await main(proxy_file_path, user_id)

if __name__ == "__main__":
    asyncio.run(main_script())
