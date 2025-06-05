# 🔓 Bruteforcer - Şifre Kırma ve Zayıf Parola Tespiti Aracı


## 📑 İçindekiler

- [ Giriş ve Amaç](#1-giriş-ve-amaç)
- [ Kullanılan Teknolojiler](#2-kullanılan-teknolojiler)
- [ Kurulum](#3-kurulum)
- [ Kullanım](#4-kullanım)
- [ Proje Yapısı](#5-proje-yapısı)
- [ Modül Açıklamaları](#6-modül-açıklamaları)
- [ Tespit Edilen Güvenlik Açıkları](#7-tespit-edilen-güvenlik-açıkları)
- [ Etik Kullanım Uyarısı](#8-etik-kullanım-uyarısı)
- [ Gelecek Geliştirmeler](#9-gelecek-geliştirmeler)
- [ Katkıda Bulunma](#10-katkıda-bulunma)
- [ Lisans](#11-lisans)
- [👨‍💻 Geliştirici](#-geliştirici)

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

### ⚠️ Etik ve Yasal Kullanım Uyarısı

**Bu araç yalnızca eğitim, araştırma ve yetkili güvenlik testleri amacıyla geliştirilmiştir.**

Kullanım sırasında lütfen aşağıdaki kurallara uyunuz:

- ✅ **Sadece size ait** sistemlerde veya **açık ve yazılı izin alınmış** hedeflerde test yapınız.  
- ❌ İzinsiz olarak üçüncü şahısların sistemlerinde kullanmak **etik dışı** ve birçok ülkede **yasalara aykırıdır**.
- ✅ Siber güvenlik farkındalığı oluşturmak ve zayıf parola politikalarını tespit etmek amacıyla kullanınız.
- ❌ Bu aracı kötüye kullanmanızdan doğacak **hiçbir sorumluluk geliştiriciye ait değildir.**

________________________________________________________

### 🌱 Gelecek Geliştirmeler

Bu proje halen geliştirilmeye açıktır. Aşağıda planlanan bazı özellikler listelenmiştir:

- [ ]  Web arayüzü (Flask ile basit GUI panel)
- [ ]  Zayıf parolaları tahmin etmek için yapay zeka/ML entegrasyonu
- [ ]  Brute-force sonuçları için detaylı loglama ve görselleştirme (grafikler, JSON/CSV çıktılar)
- [ ]  Çoklu hedefler için otomatik tarama (örneğin: IP aralığına karşı SSH brute-force)
- [ ]  Docker desteği ile hızlı kurulum (docker-compose.yml)
- [ ]  IDS/IPS sistemlerine yakalanmamak için zamanlama ve gecikme ayarları (stealth mode)
- [ ]  Tespit edilen zayıf kullanıcı/parola kombinasyonlarını şifreli olarak saklama (örneğin: AES ile)

________________________________________________________

### 🤝 Katkıda Bulunma

Bu projeye katkı sağlamak isteyen herkese kapımız açık! 

Aşağıdaki adımları takip ederek katkıda bulunabilirsin:

1.  Projeyi `fork`la  
2.  Yeni bir `branch` oluştur (`feature-x` gibi)
3.  Gerekli değişiklikleri yap ve commit et (`git commit -m "Açıklayıcı bir mesaj"`)
4.  GitHub üzerinden bir `Pull Request` (PR) oluştur
5.  Herhangi bir hata, öneri veya katkı fikrini `Issues` sekmesinde paylaş

________________________________________________________

## 📄 Lisans
Bu proje MIT lisansı altındadır. Ayrıntılar için LICENSE dosyasına bakabilirsiniz.

---

### 👨‍💻 Geliştirici

**Yağız Yedier**  
🔗 GitHub: [github.com/Yagiz0329](https://github.com/Yagiz0329)







