# utils.py
from datetime import datetime

def log_success(service, username, password, target):
    with open(f"{service}_success.log", "a") as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] {username}:{password} @ {target}\n")

def print_banner():
    print("="*50)
    print("     🔐 BruteForcer Tool by Yagiz Yedier")
    print("="*50)
