<h1 align="center"><img alt="bot takjil" src="https://raw.githubusercontent.com/dikyindrah/BotTakjil/main/img/bot_takjil.png" width="250"></h1>

<h3 align="center"><b>WhatsApp Chatbot Untuk Layanan Delivery Takjil</b></h3>

<p align="center">
  <img alt="build with" src="https://img.shields.io/badge/build%20with-python%2C%20flask%2C%20twilio-blue">
  <img alt="code size" src="https://img.shields.io/github/languages/code-size/dikyindrah/BotTakjil">
  <img alt="license" src="https://img.shields.io/badge/license-MIT-brightgreen">
  <img alt="documentation" src="https://img.shields.io/badge/documentation-README-brightgreen">
  <img alt="repo stars" src="https://img.shields.io/github/stars/dikyindrah/BotTakjil?style=social">
  <img alt="repo forks" src="https://img.shields.io/github/forks/dikyindrah/BotTakjil?style=social">
</p>

### Deskripsi
Ini adalah whatsapp chatbot sederhana yang dibuat dengan python, flask, dan twilio untuk layanan delivery takjil. Aplikasi ini sudah di deploy ke [Heroku](https://www.heroku.com) dan sudah siap digunakan untuk kebutuhan prototype ([Demo](Demo)). 
> **Note:** Saat mencoba demo. Harap memberikan perintah secara berulang jika perintah yang diberikan tidak direspon atau sudah memberikan perintah dengan benar namun tidak mendapat balasan yang sesuai.

### ✅ Fitur
- [x] Merespon sesuai perintah yang diberikan
- [x] Menghitung jumlah pesanan
- [x] Menghitung total harga pesanan
- [x] Validasi bukti pembayaran

### 👨‍💻 Penggunaan
**Localhost:**
1. Install python-3.8.0
2. Install Flask dengan perintah `pip install Flask` 
3. Install Twilio dengan perintah `pip intall twilio`
4. Download [ngrok](https://ngrok.com/download)
5. Daftar akun [twilio](https://www.twilio.com/try-twilio)
6. Buka dan jalankan kode program
7. Buka ngrok dan aktifkan HTTP Server dengan perintah `ngrok http 5000`
8. Copy url Forwarding dari HTTP Server, biasanya seperti ini `https://bbd9c73972fc.ngrok.io` tambahkan `/chat` pada bagian akhir url tersebut dan pastikan sudah menjadi seperti ini `https://bbd9c73972fc.ngrok.io/chat`
10. Masuk dan buka pengaturan [sandbox](https://www.twilio.com/console/sms/whatsapp/sandbox) pada website twilio
11. Paste url yang telah di copy ke bagian **WHEN A MESSAGE COMES IN**
12. Save pengaturan sandbox pada twilio
13. Buka whatsapp kirim pesan sandbox `join made-hunt` ke nomor **[+14155238886](https://wa.me/14155238886?text=join%20made-hunt)**
14. Selanjutnya kirim pesan berupa perintah `#menu` 

**Demo:**
1. Kirim pesan sandbox `join made-hunt` ke nomor **[+14155238886](https://wa.me/14155238886?text=join%20made-hunt)**
2. Selanjutnya kirim pesan berupa perintah `#menu` 

### 📝 Perintah
Perintah | Keterangan
---|---
`join made-hunt` | Sandbox
`#menu`  | Menampilkan menu utama
`#PesanTakjil` | Memesan takjil
`#Lagi` | Jika ingin memesan takjil lagi
`#Cukup` | Jika tidak ingin memesan takjil lagi
`#DaftarTakjil` | Melihat daftar takjil yang tersedia
`#InfoWarung` | Melihat informasi warung
`#Batal` | Membatalkan pesanan
`1-15` | Nomor takjil

### 📷 Screnshots
<img alt="menu" src="https://raw.githubusercontent.com/dikyindrah/BotTakjil/main/img/menu.png" width="150"> <img alt="daftar_takjil" src="https://raw.githubusercontent.com/dikyindrah/BotTakjil/main/img/daftar_takjil.png" width="150">
<img alt="info_warung" src="https://raw.githubusercontent.com/dikyindrah/BotTakjil/main/img/info_warung.png" width="150">
<img alt="batal" src="https://raw.githubusercontent.com/dikyindrah/BotTakjil/main/img/batal.png" width="150">
<img alt="pesan_takjil1" src="https://github.com/dikyindrah/BotTakjil/blob/main/img/pesan_takjil1.png" width="150">
<img alt="pesan_takjil2" src="https://github.com/dikyindrah/BotTakjil/blob/main/img/pesan_takjil2.png" width="150">
