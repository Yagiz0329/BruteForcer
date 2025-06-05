# 🔓 Bruteforcer - Şifre Kırma ve Zayıf Parola Tespiti Aracı


# 📑 İçindekiler

- [Giriş ve Amaç](#giriş-ve-amaç)
- [Kullanılan Teknolojiler](#kullanılan-teknolojiler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Proje Yapısı](#proje-yapısı)
- [Modüllerin Detaylı Açıklamaları](#modüllerin-detaylı-açıklamaları)
- [Tespit Edilen Güvenlik Açıkları](#tespit-edilen-güvenlik-açıkları)
- [Etik Kullanım Uyarısı](#etik-kullanım-uyarısı)
- [Gelecek Geliştirmeler](#gelecek-geliştirmeler)
- [Katkıda Bulunma](#katkıda-bulunma)
- [Lisans](#lisans)

## 🎯 Giriş Ve Amaç

Bu proje, Python diliyle geliştirilmiş, çeşitli servisler (FTP, SSH, HTTP vs.) üzerinde brute-force saldırıları gerçekleştirerek zayıf parolaları tespit edebilen bir güvenlik test aracıdır.

**Hedef:**
- Parola güvenliğini test etme
- Zayıf parola kullanımını tespit etme
- Eğitim ve araştırma amaçlı kullanımlar

**Hedef Kitle:**

- Siber güvenliğe ilgi duyanlar
- Penetrasyon testi yapanlar
- Python ile güvenlik araçları geliştirmek isteyenler

________________________________________________________

## 💻 Kullanılan Teknolojiler

- Python 3.x
- socket, paramiko, requests (Standart ve 3. parti kütüphaneler)
- argparse
- threading

## 🛠️ Kurulum

________________________________________________________

### Gerekli sistem araçlarını güncelle (Linux için)

```
sudo apt update && sudo apt install python3 python3-pip git -y

```
### Projeyi GitHub'dan klonla
```
git clone https://github.com/Yagiz0329/Bruteforcer-Tool.git

cd Bruteforcer-Tool

```
### Python kütüphanelerini yükle
```
pip install -r requirements.txt
```
________________________________________________________

## 🛠️🛠️ Kullanım Örneği

### SSH brute-force örneği:
```
python3 main.py -m ssh -t 192.168.1.10 -u root -w wordlist.txt
```
### FTP brute-force örneği:
```
python3 main.py -m ftp -t 192.168.1.10 -u anonymous -w wordlist.txt
```
### HTTP form brute-force örneği:
```
python3 main.py -m http -t http://192.168.1.10/login.php -u admin -w wordlist.txt
```
________________________________________________________

### 📂 Proje Yapısı

<pre>
📁 Bruteforcer-Tool
├── brute_ftp.py
├── brute.http.py
├── brurte.ssh.py
├── main.py
├── utils.py
├── requirements.txt
├── LICENSE
└── README.md
</pre>

________________________________________________________


### 📄 Modüllerin Açıklamaları

- `main.py`: Komut satırı argümanlarını alır ve uygun brute-force modülünü çalıştırır.
- `brute_ftp.py`: FTP servislerine brute-force saldırısı yapar.
- `brute.http.py`: HTTP Basic Auth korumalı web sayfalarına karşı brute-force saldırısı yapar.
- `brute_ssh.py`: SSH servislerine brute-force saldırısı yapar.
- `utils.py`: Loglama ve yardımcı araçları barındırır.
- `requirements.txt`: Python kütüphane bağımlılıkları.
- `LICENSE`: Yazılım lisans bilgisi.
- `README.md`: Projenin açıklama ve dökümantasyon dosyası.

________________________________________________________

### 🛡️ Tespit Edilen Güvenlik Açıkları

- Zayıf Parola Kullanımı
- SSH Servislerinde Brute-Force'a Açıklık
- FTP Sunucularında Yetkisiz Erişim Riski
- HTTP Basic Authentication Zayıflığı
- Servis Yanıtlarına Göre Kullanıcı Bilgisi Sızması

________________________________________________________







