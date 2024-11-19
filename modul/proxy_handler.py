# proxy_handler.py
import requests

def check_proxy(proxy):
    try:
        response = requests.get("http://example.com", proxies={"http": proxy, "https": proxy}, timeout=5)
        return response.status_code == 200
    except:
        return False

