# main.py
import argparse
from utils import print_banner
import sys

# Modül importları (try-catch ile hata önleme)
try:
    from brute_ssh import ssh_brute_force
    from brute_ftp import ftp_brute_force
    from brute_http import http_brute_force
except ImportError as e:
    print(f"[!] Modül hatası: {e}")
    sys.exit(1)

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="🔐 BruteForcer Tool - Gelişmiş şifre kırma aracı (SSH, FTP, HTTP)"
    )
    parser.add_argument("-m", "--mode", required=True, help="Brute-force modu: ssh / ftp / http")
    parser.add_argument("-t", "--target", required=True, help="Hedef IP adresi veya URL")
    parser.add_argument("-u", "--username", required=True, help="Kullanıcı adı")
    parser.add_argument("-w", "--wordlist", required=True, help="Wordlist dosyasının yolu")
    parser.add_argument("-p", "--port", type=int, help="Opsiyonel özel port (varsayılan servise göre atanır)")
    
    return parser.parse_args()

def main():
    print_banner()
    args = parse_arguments()
    
    mode = args.mode.lower()
    target = args.target
    username = args.username
    wordlist = args.wordlist
    port = args.port

    print(f"[>] Mod: {mode.upper()}, Hedef: {target}, Kullanıcı: {username}")
    
    if mode == "ssh":
        ssh_brute_force(target, username, wordlist, port or 22)
    elif mode == "ftp":
        ftp_brute_force(target, username, wordlist, port or 21)
    elif mode == "http":
        http_brute_force(target, username, wordlist)
    else:
        print("[!] Geçersiz mod. Geçerli değerler: ssh, ftp, http")
        sys.exit(1)

if __name__ == "__main__":
    main()
