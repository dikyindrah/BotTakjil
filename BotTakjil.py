from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

'''
list takjil mendefinisikan nama dan harga takjil 
yang akan di jual. Baris pertama mendefinisikan nama takjil
dan baris kedua mendefinisikan harga takjil.
'''
takjil = [
    ['Kurma (1 mika, isi 12 butir kurma)',
     'Kue Bolu Karamel (1 mika, isi 5 lapis kue bolu)',
     'Kue Bolu Coklat (1 mika, isi 5 lapis kue bolu)',
     'Kue Donat Toping Coklat Meses, Coklat Kacang, Stroberi, dan Bluberi  (1 Kotak, isi 4)',
     'Kue Lapis + Kue Naga Sari (1 mika, isi 4)',
     'Risol (1 Mika, isi 5)',
     'Bakwan Jagung (1 pcs)',
     'Tahu Bunting (1 pcs)',
     'Pisang Goreng (1 pcs)',
     'Kolak Pisang + Kolang Kaling',
     'Es Pisang Ijo',
     'Es Cendol',
     'Es Cincau',
     'Es Kelapa Muda',
     'Es Teh'],
    [7500,
     5000,
     5000,
     10000,
     4000,
     5000,
     1000,
     1000,
     1000,
     8000,
     8000,
     5000,
     5000,
     6000,
     2000]
]

takjil_pesanan = [[], []]

huruf_kecil = True

sudah_pesan_takjil = False
lagi = True

rute_nama = False
nama_pelanggan = ''

rute_alamat = False
alamat_pelanggan = ''

rute_pembayaran = False
biaya_antar = 2000
status_pesanan = 'Belum dibayar'

@app.route('/chat', methods=['POST'])
def chat():
    '''
    fungsi chat() mendefinisikan url '/chat' yang akan digunakan untuk 
    menghubungkan program bot dengan api whatsapp dari twillio.
    '''
    pesan = request.form.get('Body')
    return respon(pesan=pesan)

def respon(pesan):
    '''
    Fungsi respon() digunakan untuk menyeleksi perintah yang 
    diberikan pelanggan kepada program bot. Program bot akan
    menyeleksi dan memberikan tanggapan sesuai dengan perintah
    yang diberikan.
    '''
    global sudah_pesan_takjil

    perintah = ''
    if huruf_kecil == True:
        # Menghubah seluruh perintah menjadi huruf kecil
        perintah = pesan.lower()
    else:
        # Menghubah seluruh perintah menjadi huruf normal
        perintah = pesan

    if perintah == '#menu':
        return menu()
    elif perintah == '#daftartakjil':
        return daftar_takjil()
    elif perintah == '#pesantakjil':
        sudah_pesan_takjil = True
        return pesan_takjil()
    elif perintah == '#infowarung':
        return info_warung()
    elif perintah == '#batal' or perintah == '#Batal':
        return membatalkan_pesanan()
    elif perintah.isdigit() and lagi == True:
        if sudah_pesan_takjil == True:
            nomor = int(perintah)
            return pilih_takjil(nomor)
        else:
            return perintah_tidak_diketahui()
    elif perintah.isdigit() and lagi == False:
        return perintah_lagi_belum_diberikan()
    elif perintah == '#lagi' or perintah == '#cukup':
        if sudah_pesan_takjil == True:
            return pesan_takjil_lagi_atau_cukup(perintah)
        else:
            return perintah_tidak_diketahui()
    elif rute_nama == True:
        return nama_penerima(perintah)
    elif rute_alamat == True:
        return alamat_penerima(perintah)
    elif rute_pembayaran == True:
        return pembayaran()
    else:
        return perintah_tidak_diketahui()

def menu():
    '''
    Fungsi menu() digunakan untuk menampilkan menu utama.
    '''
    balas = MessagingResponse()

    balas.message(
        '*Layanan Delivery Takjil Warung XYZ*\n\n'+
        '*Menu Utama.*\n\n'+
        'Assalamu’alaikum Wr. Wb.\n\n'+
        'Selamat datang di layanan delivery kami, anda bisa memesan takjil lewat layanan ini, dan kami akan mengantarnya ke alamat anda.\n\n'+
        'Kami menyediakan aneka takjil seperti kurma, kue manis, gorengan, minuman segar, dan masih banyak lagi yang bisa anda pilih untuk menemani buka puasa anda...\n\n'+
        'Silahkan pilih *#Menu* untuk ke menu utama, pilih *#PesanTakjil* untuk memsan takjil, pilih *#DaftarTakjil* untuk melihat informasi takjil yang tersedia, pilih *#InfoWarung* untuk melihat informasi warung takjil XYZ, dan pilih *#Batal* untuk mangakhiri percakapan.\n\n'+
        '*#Menu* *#PesanTakjil* *#DaftarTakjil* *#InfoWarung* *#Batal*'
    )

    return str(balas)

def mengubah_data_menjadi_teks(data):
    '''Fungsi mengubah_data_menjadi_teks() digunakan untuk mengubah
    data dari list ke bentuk teks'''
    praproses = []
    for i in range(1):
        for j in range(len(data[0])):
            tmp = '{}. {} Rp.{},-\n'.format(j+1, data[0][j], data[1][j])
            praproses.append(tmp)

    teks = ''
    for i in range(len(praproses)):
        tmp = praproses[i]
        teks = teks + '\n' + tmp

    return teks

def daftar_takjil():
    '''Fungsi daftar_takjil() digunakan untuk menampilkan daftar
    takjil yang tersedia'''
    balas = MessagingResponse()

    daftar_takjil_yang_tersedia = mengubah_data_menjadi_teks(takjil)

    balas.message(
        '*Layanan Delivery Takjil Warung XYZ*\n\n'+
        '*Daftar Takjil.*\n'+
        daftar_takjil_yang_tersedia+'\n\n'+
        'Silahkan pilih *#Menu* untuk ke menu utama, pilih *#PesanTakjil* untuk memsan takjil, pilih *#DaftarTakjil* untuk melihat informasi takjil yang tersedia, pilih *#InfoWarung* untuk melihat informasi warung takjil XYZ , dan pilih *#Batal* untuk mangakhiri percakapan.\n\n'+
        '*#Menu* *#PesanTakjil* *#DaftarTakjil* *#InfoWarung* *#Batal*'
    )

    return str(balas)   

def pesan_takjil():
    '''Fungsi pesan_takjil() digunakan untuk menginstruksikan pelanggan
    agar memilih nomor takjil yang ingin dipesan'''
    balas = MessagingResponse()

    daftar_takjil_yang_tersedia = mengubah_data_menjadi_teks(takjil)

    balas.message(
        '*Layanan Delivery Takjil Warung XYZ*\n\n'+
        '*Pesan Takjil.*\n'+
        daftar_takjil_yang_tersedia+'\n\n'+
        'Silahkan pilih *nomor takjil* untuk memilih takjil yang ingin anda pesan dan pilih *#Batal* untuk membatalkan pesanan.\n\n'+
        '*#Menu* *#PesanTakjil* *#DaftarTakjil* *#InfoWarung* *#Batal*'
    )

    return str(balas)

def pilih_takjil(nomor):
    '''Fungsi pilih_takjil() digunakan untuk menyeleksi pesanan takjil 
    berdasarkan nomor takjil yang dipilih oleh pelanggan'''
    global lagi

    if (nomor == 1 or nomor == 2 or nomor == 3 or
        nomor == 4 or nomor == 5 or nomor == 6 or
        nomor == 7 or nomor == 8 or nomor == 9 or
        nomor == 10 or nomor == 11 or nomor == 12 or
        nomor == 13 or nomor == 14 or nomor == 15):
        lagi = False
        return memproses_takjil_pesanan(nomor)
    else:
        return perintah_tidak_diketahui()

def memproses_takjil_pesanan(nomor_takjil):
    '''Fungsi memproses_takjil_pesanan() digunakan untuk menampilkan
    pesanan takjil yang sudah dipilih'''
    balas = MessagingResponse()

    takjil_pesanan[0].append(takjil[0][nomor_takjil-1])
    takjil_pesanan[1].append(takjil[1][nomor_takjil-1])
    daftar_takjil_yang_dipesan = mengubah_data_menjadi_teks(takjil_pesanan)

    balas.message(
        '*Layanan Delivery Takjil Warung XYZ*\n\n'+
        '*Pesan Takjil.*\n\n'+
        'Pesanan anda:\n'+
        daftar_takjil_yang_dipesan+'\n\n'+
        'Pilih *#Lagi* untuk memesan takjil lagi, pilih *#Cukup* jika tidak ada yang dipesan lagi, dan pilih *#Batal* untuk membatalkan pesanan.\n\n'
    )

    return str(balas)

def pesan_takjil_lagi_atau_cukup(perintah):
    '''Fungsi pesan_takjil_lagi_atau_cukup() digunakan untuk memeriksa 
    apakah pelanggan ingin memesan takjil lagi atau cukup dengan 
    pesanan takjil yang telah di pilih'''
    global lagi, rute_nama, huruf_kecil

    if perintah == '#lagi':
        lagi = True
        return pesan_takjil()
    elif perintah == '#cukup':
        huruf_kecil = False
        rute_nama = True
        return hitung_pesanan()
    else:
        return perintah_tidak_diketahui()

def hitung_pesanan():
    '''Fungsi hitung_pesanan() digunakan untuk menampilkan informasi
    pesanan takjil terkait jumlah takjil dan total biaya yang harus 
    dibayar.'''
    balas = MessagingResponse()
    
    daftar_takjil_yang_dipesan = mengubah_data_menjadi_teks(takjil_pesanan)

    total_pesanan = jumlah_takjil_pesanan(takjil_pesanan)
    total_harga = jumlah_harga_pesanan(takjil_pesanan)

    balas.message(
        '*Layanan Delivery Takjil Warung XYZ*\n\n'+
        '*Pesan Takjil.*\n\n'+
        'Pesanan anda:\n'+
        daftar_takjil_yang_dipesan+'\n\n'+
        'Jumlah         : {}\n'.format(total_pesanan)+
        'Total Harga : Rp.{},-\n'.format(total_harga)+
        'Biaya Antar : Rp.{},-\n'.format(biaya_antar)+
        'Total Harga + Antar : Rp.{},-\n'.format(total_harga+biaya_antar)+
        'Nama            : \n\n'+
        'Siapa nama anda?...\n\n'+
        'Silahkan balas chat ini dengan *nama penerima* takjil.\n\nPilih *#Batal* untuk membatalkan pesanan.'
    )
    
    return str(balas)

def jumlah_takjil_pesanan(takjil_pesanan):
    '''Fungsi jumlah_takjil_pesanan() digunakan untuk menghitung jumlah
    takjil pesanan'''
    jumlah_takjil = 0
    i = 0
    while i < len(takjil_pesanan[0]):
        jumlah_takjil = jumlah_takjil + 1
        i = i + 1

    return jumlah_takjil

def jumlah_harga_pesanan(takjil_pesanan):
    '''Fungsi jumlah_takjil_pesanan() digunakan untuk menghitung jumlah 
    harga takjil pesanan'''
    total_harga = 0
    for i in range(1):
        for j in range(len(takjil_pesanan[1])):
            total_harga = total_harga + takjil_pesanan[1][j]

    return total_harga

def nama_penerima(nama):
    '''Fungsi nama_penerima() digunakan untuk memproses nama
    pelanggan yang akan menerima takjil'''
    global rute_nama, nama_pelanggan, huruf_kecil, rute_alamat
    nama_pelanggan = nama

    balas = MessagingResponse()

    daftar_takjil_yang_dipesan = mengubah_data_menjadi_teks(takjil_pesanan)

    total_pesanan = jumlah_takjil_pesanan(takjil_pesanan)
    total_harga = jumlah_harga_pesanan(takjil_pesanan)

    balas.message(
        '*Layanan Delivery Takjil Warung XYZ*\n\n'+
        '*Pesan Takjil.*\n\n'+
        'Pesanan anda:\n'+
        daftar_takjil_yang_dipesan+'\n\n'+
        'Jumlah         : {}\n'.format(total_pesanan)+
        'Total Harga : Rp.{},-\n'.format(total_harga)+
        'Biaya Antar : Rp.{},-\n'.format(biaya_antar)+
        'Total Harga + Antar : Rp.{},-\n'.format(total_harga+biaya_antar)+
        'Nama            : {}\n'.format(nama_pelanggan)+
        'Alamat          : \n\n'+
        'Dimana alamat anda?...\n\n'+
        'Silahkan balas chat ini dengan *alamat* atau *lokasi* anda, agar kami bisa mengantar takjil pesanaan anda.\n\nPilih *#Batal* untuk membatalkan pesanan.'
    )

    rute_nama = False
    rute_alamat = True

    return str(balas)

def alamat_penerima(alamat):
    '''Fungsi alamat_penerima() digunakan untuk memproses alamat
    pelanggan yang akan menerima takjil'''
    global rute_alamat, alamat_pelanggan, huruf_kecil, rute_pembayaran
    alamat_pelanggan = alamat

    balas = MessagingResponse()

    daftar_takjil_yang_dipesan = mengubah_data_menjadi_teks(takjil_pesanan)

    total_pesanan = jumlah_takjil_pesanan(takjil_pesanan)
    total_harga = jumlah_harga_pesanan(takjil_pesanan)

    balas.message(
        '*Layanan Delivery Takjil Warung XYZ*\n\n'+
        '*Pesan Takjil.*\n\n'+
        'Pesanan anda:\n'+
        daftar_takjil_yang_dipesan+'\n\n'+
        'Jumlah         : {}\n'.format(total_pesanan)+
        'Total Harga : Rp.{},-\n'.format(total_harga)+
        'Biaya Antar : Rp.{},-\n'.format(biaya_antar)+
        'Total Harga + Antar : Rp.{},-\n'.format(total_harga+biaya_antar)+
        'Nama            : {}\n'.format(nama_pelanggan)+
        'Alamat          : {}\n'.format(alamat_pelanggan)+
        'Status           : {}\n\n'.format(status_pesanan)+
        'Silahkan lakukan pembayaran melalui salah satu rekening kami dibawah ini, dan kirim bukti pembayaran anda ke akun whatsapp kami.\n\n'+
        'Bank BRI : 12312-36485-55531\n'+
        'Gopay      : 898082181177026\n'+
        'Dana        : 707082181177026\n'+
        'OVO         : 555082181177026\n\n'+
        'Pilih *#Batal* untuk membatalkan pesanan.'
    )

    huruf_kecil = False
    rute_alamat = False
    rute_pembayaran = True

    return str(balas)

def pembayaran():
    '''Fungsi pembayaran() digunakan untuk memvalidasi bukti bahawa
    pelanggan sudah membayar takjil yang dipesan'''
    
    global status_pesanan, rute_pembayaran
    status_pesanan = 'Sudah dibayar'
    balas = MessagingResponse()
    
    daftar_takjil_yang_dipesan = mengubah_data_menjadi_teks(takjil_pesanan)

    total_pesanan = jumlah_takjil_pesanan(takjil_pesanan)
    total_harga = jumlah_harga_pesanan(takjil_pesanan)

    balas.message(
        '*Layanan Delivery Takjil Warung XYZ*\n\n'+
        '*Pesan Takjil.*\n\n'+
        'Pesanan anda:\n'+
        daftar_takjil_yang_dipesan+'\n\n'+
        'Jumlah         : {}\n'.format(total_pesanan)+
        'Total Harga : Rp.{},-\n'.format(total_harga)+
        'Biaya Antar : Rp.{},-\n'.format(biaya_antar)+
        'Total Harga + Antar : Rp.{},-\n'.format(total_harga+biaya_antar)+
        'Nama            : {}\n'.format(nama_pelanggan)+
        'Alamat          : {}\n'.format(alamat_pelanggan)+
        'Status           : {}\n\n'.format(status_pesanan)+
        'Terimakasih, pesanan anda segera kami antar.'
    )

    rute_pembayaran = False

    return str(balas)    

def info_warung():
    '''Fungsi info_warung() digunakan untuk menampilkan informasi 
    warung takjil'''
    balas = MessagingResponse()

    balas.message(
        '*Layanan Delivery Takjil Warung XYZ*\n\n'+
        '*Info Warung.*\n\n'+
        'Alamat    : Jl. Soekardi Hamdani, Kec. Labuhan Ratu, Kota Bandar Lampung\n\n'+
        'Buka       : 16:00 - 18:00 Wib\n\n'+
        'Kontak   : +14155238886\n\n'+
        'Catatan : Kami tidak melayani jasa antar diluar wilayah kecamatan labuhan ratu.\n\n'+
        'Silahkan pilih *#Menu* untuk ke menu utama, pilih *#PesanTakjil* untuk memsan takjil, pilih *#DaftarTakjil* untuk melihat informasi takjil yang tersedia, pilih *#InfoWarung* untuk melihat informasi warung takjil XYZ , dan pilih *#Batal* untuk mangakhiri percakapan.\n\n'+
        '*#Menu* *#PesanTakjil* *#DaftarTakjil* *#InfoWarung* *#Batal*'
    )    

    return str(balas)

def membatalkan_pesanan():
    '''Fungsi membatalkan_pesanan() digunakan untuk membatalkan pesanan
    pelanggan'''
    balas = MessagingResponse()

    global sudah_pesan_takjil, lagi, huruf_kecil, rute_nama, nama_pelanggan

    takjil_pesanan[0].clear()
    takjil_pesanan[1].clear()

    sudah_pesan_takjil = False
    lagi = True

    huruf_kecil = True

    rute_nama = False
    nama_pelanggan = ''

    rute_alamat = False
    alamat_pelanggan = ''

    rute_pembayaran = False
    status_pesanan = 'Belum dibayar'

    balas.message(
        '*Layanan Delivery Takjil Warung XYZ*\n\n'+
        '*Batal.*\n\n'+
        'Terimakasih sudah mampir di warung kami.\n\n'+
        'Wassalamu’alaikum Wr. Wb.'
    ) 

    return str(balas)

def perintah_lagi_belum_diberikan():
    '''Fungsi perintah_lagi_belum_diberikan() digunakan untuk 
    menampilkan informasi bahwa user harus memberikan perintah 
    #lagi untuk memesan takjil lagi'''
    balas = MessagingResponse()

    balas.message('Anda harus memberikan perintah *#lagi* untuk memesan takjil lagi.')

    return str(balas)

def perintah_tidak_diketahui():
    '''Fungsi perintah_tidak_diketahui() digunakan untuk menampilkan 
    informasi bahwa perintah yang diberikan pelanggan tidak 
    diketahui oleh program bot.'''
    balas = MessagingResponse()

    balas.message('Maaf, perintah yang anda berikan tidak diketahui.')

    return str(balas)

if __name__ == '__main__':
    app.run(debug=True)