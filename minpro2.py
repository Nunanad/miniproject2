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
        if not self.pemesanan:
            print("\nBelum ada pemesanan.")
        else:
            print("\nDaftar Pemesanan:")
            for idx, pemesanan in enumerate(self.pemesanan, 1):
                print(f"\n{idx}. Tujuan: {pemesanan['Tujuan']}, Tanggal: {pemesanan['Tanggal']}, Jumlah Tiket: {pemesanan['Jumlah Tiket']}, Total Harga: Rp {pemesanan['Total Harga']:,}")

    def ubah_harga(self):
        print("\nMengubah Harga Tiket")
        self.tampilkan_tujuan()
        pilihan = input("Pilih nomor tujuan yang harganya ingin diubah: ")
        try:
            index = int(pilihan) - 1
            if 0 <= index < len(self.tujuan):
                kota = self.tujuan[index]
                harga_baru = int(input(f"Masukkan harga baru untuk {kota}: Rp "))
                self.harga[kota] = harga_baru
                print(f"Harga tiket untuk {kota} berhasil diubah menjadi Rp {harga_baru:,}.")
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("Masukkan nomor yang valid.")

    def tambah_tujuan(self):
        tujuan_baru = input("\nMasukkan nama kota tujuan baru: ")
        harga_baru = int(input(f"Masukkan harga tiket untuk {tujuan_baru}: Rp "))
        self.tujuan.append(tujuan_baru)
        self.harga[tujuan_baru] = harga_baru
        print(f"Tujuan {tujuan_baru} berhasil ditambahkan dengan harga Rp {harga_baru:,}.")

    def hapus_tujuan(self):
        self.tampilkan_tujuan()
        pilihan = input("\nPilih nomor tujuan yang ingin dihapus: ")
        try:
            index = int(pilihan) - 1
            if 0 <= index < len(self.tujuan):
                kota = self.tujuan.pop(index)
                del self.harga[kota]
                print(f"Tujuan {kota} berhasil dihapus.")
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("Masukkan nomor yang valid.")

    def menu_admin(self):
        while True:
            print("\nMenu Admin:")
            print("1. Tampilkan Daftar Pemesanan")
            print("2. Ubah Harga Tiket")
            print("3. Tambah Tujuan")
            print("4. Hapus Tujuan")
            print("5. Keluar")

            pilihan = input("Pilih menu (1-5): ")

            if pilihan == "1":
                self.tampilkan_pemesanan()
            elif pilihan == "2":
                self.ubah_harga()
            elif pilihan == "3":
                self.tambah_tujuan()
            elif pilihan == "4":
                self.hapus_tujuan()
            elif pilihan == "5":
                print("Keluar dari menu admin.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    sistem = SistemPemesananTiket()
    while True:
        print("\nMenu Pengguna:")
        print("1. Proses Pemesanan")
        print("2. Menu Admin (Masukkan admin mode)")
        print("3. Keluar")

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            sistem.proses_pemesanan()
        elif pilihan == "2":
            admin_password = input("Masukkan password admin: ")
            if admin_password == "admin123": 
                sistem.menu_admin()
            else:
                print("Password salah. Akses ke menu admin ditolak.")
        elif pilihan == "3":
            print("Terima kasih telah menggunakan layanan kami!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
