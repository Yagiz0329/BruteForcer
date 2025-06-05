import argparse
from brute_ssh import ssh_bruteforce
from brute_ftp import ftp_bruteforce
from brute_http import http_bruteforce

def main():
    parser = argparse.ArgumentParser(description="BruteForce Aracı")
    parser.add_argument("-m", "--mode", required=True, choices=["ssh", "ftp", "http"], help="BruteForce modu")
    parser.add_argument("-t", "--target", required=True, help="Hedef IP veya domain")
    parser.add_argument("-u", "--username", required=True, help="Kullanıcı adı")
    parser.add_argument("-w", "--wordlist", required=True, help="Parola wordlist dosyası")
    args = parser.parse_args()

    if args.mode == "ssh":
        ssh_bruteforce(args.target, args.username, args.wordlist)
    elif args.mode == "ftp":
        ftp_bruteforce(args.target, args.username, args.wordlist)
    elif args.mode == "http":
        http_bruteforce(args.target, args.username, args.wordlist)

if __name__ == "__main__":
    main()
