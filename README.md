# miniproject2
# Profil
Nama : Nanda Pesona Putri

NIM : 2409116101

Kelas : C

Tema : Pemesanan Tiket Kereta

# Menu Awal

![image](https://github.com/user-attachments/assets/dbe30519-1afd-40d8-96f6-38c4c761762a)

Pada gambar di atas adalah menu awal dari program jika pertama kali dijalankan, terdapat 3 menu yang bisa dipilih

# Penjelasan Menu

1. Proses pemesanan

Jika angka 1 dipilih maka user akan masuk ke menu pembeli, menu untuk role pembeli dapat menampilkan kota tujuan, tanggal pemesanan, jumlah tiket yang akan dibeli, dan ringkasan pemesanan tiket

2. Admin

Jika angka 2 dipilih maka user akan masuk ke menu admin, menu untuk role admin ini membutuhkan password untuk akses ke menu nya, setelah memasukan password yang valid maka user akan di lihatkan menu admin yang berisi 1. Tampilkan Daftar Pemesanan
2. Ubah Harga Tiket,
3. Tambah Tujuan,
4. Hapus Tujuan,
5. Keluar

3. Keluar

Jika angka 3 dipilih maka user akan keluar dari program dengan ucapan terima kasih

4. Angka Selain 1 - 3

Jika angka yang dimasukkan adalah selain 1, 2 dan 3 maka status akan bertuliskan "pilihan tidak valid"

# Proses Pemesanan 


![image](https://github.com/user-attachments/assets/a0572ba5-35fb-4681-90f5-664cd28a33aa)

Proses pemesanan akan ditampilkan jika user memilih 1 pada menu

User dapat memesan tiket dengan menentukan Kota yang akan di tuju dengan cara memilih kota yang telah ditandai dengan angka yang ada pada aftar


![image](https://github.com/user-attachments/assets/5db233fa-4b22-408a-93a5-ba46cc72c71a)

Misal user memilih angka 2 dengan tujuan Samarinda, Selanjutnya User diharapkan untuk memasukan format tanggal, bulan dan tahun. Bagian ini harus diisi sesuai dengan tanggal di masa depan, pembeli tidak dapat meengisi bagian ini dengan tanggal di masa lalu.


![image](https://github.com/user-attachments/assets/4843d524-76ca-4511-a498-e5e9509e9be4)

Selanjutnya pembeli di harapkan memasukkan Jumlah tiket yang ingin dibeli.


![image](https://github.com/user-attachments/assets/a493693d-8dba-4567-a348-7616a1ef2724)

Pada gambar di atas, di lihatkan, setelah kita mengisi format yang telah di berikan maka akan muncul ringkasan pemesanan. Pemesan Tiket perlu mengkonfirmasi apakah Tiket yang di pesan sudah benar atau belum dengan memilih di anatara y/n, bila sudah benar maka pilih y dan anda akan di arahkan ke step selanjutnya dan jika masih salah maka pilih n dan anda akan kembali ke menu awal.


![image](https://github.com/user-attachments/assets/bf316cae-4fef-4175-9501-a6565b8b1783)

Selanjutnya program akan mengucapkan terimakasih karena sudah melakukan transaksi dan anda akan di arahkan ke menu awal.

# Menu Admin

![image](https://github.com/user-attachments/assets/0973c1e9-38be-4e76-9094-8d9620892079)

Pada menu admin, kita akan diminta untuk mengisi password terlebih dahulu, jika password tidak valid maka user di harapkan mengisi ulang hingga 3 kali percobaan jika password valid maka user akan di arahkan ke step selnajutnya.


![image](https://github.com/user-attachments/assets/9a8d4add-05b4-4597-a151-228de532ff7a)

Ini adalah menu admin dan berikut adalah penjelasan dari daftar menu yang ditampilkan

1. Tampilkan Daftar Pemesanan

Pada step ini program akan menampilkan tiket tiket yang sudah terpesan, admin juga dapat memantau jumlah tiket tiket yang terpesan. setelah melihat tiket tiket yang sudah terpesan, user akan diarahkan kembali ke menu admin.

2. Ubah Harga Tiket

![image](https://github.com/user-attachments/assets/15506b44-6d61-4cb5-bcf3-e534a3f8fb64)

Pada step ini admin dapat mengubah harga berdasarkan kota tujuan yang sudah tersedia di dalam program, Admin dapat memilih tiket kota tujuan dan mengubah harganya dengan memasukkan angka yang valid, setelah selesai admin akan di arahkan kembali ke menu admin

3. Menambah Kota Tujuan

![image](https://github.com/user-attachments/assets/eafd75c5-87a5-4375-ab15-e30eb8325ad3)

Seperti gambar di atas admin dapat menambahkan opsi kota tujuan baru serta memberi harga untuk tiketnya, misalnya Saya menambahkan Kota Berau dengan hargatiket 30,000 Maka Opsi Tujuan Kota Berau akan muncul pada program sebagai pilihan ketika pemesan tiket ingin memesan tiket.

![image](https://github.com/user-attachments/assets/7b379acb-f26b-4899-aa9c-be091298f6fd)

Setelah selesai Admin akan diarahkan kembali ke menu admin.

4. Hapus Tujuan

![image](https://github.com/user-attachments/assets/16910fa2-e9f6-4d36-adc2-a5fec5ab9d03)

Seperti gambar di atas, admin dapat menghapus opsi kota tujuan yang ada pada program, dengan cara mengklik angka yang bertaut dengan kota tujuan yang ingin di hapus, setelah berhasil, admin akan di arahkan kembali ke menu admin

5. Keluar

![image](https://github.com/user-attachments/assets/d66ba03d-2039-4dc6-9476-dcb276fefc3d)

Bila Admin memilih opsi 5, maka admin akan di arahkan ke menu awal.

6. angka selain 1 - 5

![image](https://github.com/user-attachments/assets/a2a1368d-21ef-413f-b8c5-03cf799cda09)

Jika user memasukkan angka selain 1 - 5 maka program akan memberi pesan bahwa pilihan/angka tidak valid

# File Python

import datetime

class SistemPemesananTiket:
    def __init__(self):
        self.tujuan = ["Balikpapan", "Samarinda", "Bontang", "Tenggarong", "Kutai Kartanegara"]
        self.harga = {
            "Balikpapan": 150000, 
            "Samarinda": 130000, 
            "Bontang": 120000, 
            "Tenggarong": 110000, 
            "Kutai Kartanegara": 140000
        }
        self.pemesanan = []

    def tampilkan_tujuan(self):
        print("Tujuan yang tersedia:")
        for i, kota in enumerate(self.tujuan, 1):
            print(f"{i}. {kota}")

    def pilih_tujuan(self):
        while True:
            self.tampilkan_tujuan()
            pilihan = input("Pilih nomor tujuan Anda: ")
            try:
                index = int(pilihan) - 1
                if 0 <= index < len(self.tujuan):
                    return self.tujuan[index]
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
            except ValueError:
                print("Masukkan nomor yang valid.")

    def pilih_tanggal(self):
        while True:
            tanggal_str = input("Masukkan tanggal keberangkatan (format: DD-MM-YYYY): ")
            try:
                tanggal = datetime.datetime.strptime(tanggal_str, "%d-%m-%Y")
                if tanggal.date() >= datetime.date.today():
                    return tanggal.strftime("%d-%m-%Y")
                else:
                    print("Tanggal harus di masa depan. Silakan coba lagi.")
            except ValueError:
                print("Format tanggal tidak valid. Gunakan format DD-MM-YYYY.")

    def pilih_jumlah_tiket(self):
        while True:
            try:
                jumlah = int(input("Masukkan jumlah tiket yang ingin dipesan: "))
                if jumlah > 0:
                    return jumlah
                else:
                    print("Jumlah tiket harus lebih dari 0.")
            except ValueError:
                print("Masukkan angka yang valid.")

    def hitung_total(self, tujuan, jumlah_tiket):
        return self.harga[tujuan] * jumlah_tiket

    def proses_pemesanan(self):
        print("Selamat datang di Sistem Pemesanan Tiket Kereta!")
        tujuan = self.pilih_tujuan()
        tanggal = self.pilih_tanggal()
        jumlah_tiket = self.pilih_jumlah_tiket()
        total_harga = self.hitung_total(tujuan, jumlah_tiket)

        pemesanan_baru = {
            "Tujuan": tujuan,
            "Tanggal": tanggal,
            "Jumlah Tiket": jumlah_tiket,
            "Total Harga": total_harga
        }
        self.pemesanan.append(pemesanan_baru)

        print("\nRincian Pemesanan:")
        print(f"Tujuan: {tujuan}")
        print(f"Tanggal: {tanggal}")
        print(f"Jumlah Tiket: {jumlah_tiket}")
        print(f"Total Harga: Rp {total_harga:,}")

        konfirmasi = input("\nApakah Anda ingin melanjutkan pemesanan? (y/n): ")
        if konfirmasi.lower() == 'y':
            print("Pemesanan berhasil! Terima kasih telah menggunakan layanan kami.")
        else:
            print("Pemesanan dibatalkan.")

    def tampilkan_pemesanan(self):




































