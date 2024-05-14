# Inisialisasi daftar belanjaan dan harga
daftar_belanjaan = []
daftar_harga = {}

# Fungsi untuk menambahkan item ke daftar belanjaan
# Putra Strata Tandika Setyawan (2311104050)
def tambah_item(items):
    new_items = items.split(",")  # Pisahkan item yang dimasukkan dengan koma
    for item in new_items:
        item = item.strip().capitalize()  # Hilangkan spasi di awal dan akhir item dan kapitalisasi huruf pertama
        if item:
            harga = input_ulang(f"Masukkan harga untuk {item}: ")
            while not harga.isdigit():
                print("Harga harus berupa angka. Silakan coba lagi.")
                harga = input_ulang(f"Masukkan harga untuk {item}: ")
            daftar_belanjaan.append(item)
            daftar_harga[item] = int(harga)
            print(f"{item} telah ditambahkan ke daftar belanjaan dengan harga {harga}.")
    sortir_belanjaan()

# Fungsi untuk mencari item dalam daftar belanjaan
# Aulia Jasifa BR Ginting (2311104060)
def cari_item(item):
    item = item.capitalize()  # Kapitalisasi huruf pertama
    if item in daftar_belanjaan:
        print(f"{item} ada dalam daftar belanjaan dengan harga {daftar_harga[item]}.")
    else:
        print(f"{item} tidak ada dalam daftar belanjaan.")

# Fungsi untuk menghapus item dari daftar belanjaan
# Alya Rabani (2311104076)
def hapus_item(item):
    item = item.capitalize()  # Kapitalisasi huruf pertama
    if item in daftar_belanjaan:
        daftar_belanjaan.remove(item)
        del daftar_harga[item]
        print(f"{item} telah dihapus dari daftar belanjaan.")
    else:
        print(f"{item} tidak ada dalam daftar belanjaan.")

# Fungsi untuk menghapus semua item dari daftar belanjaan
# Zhafir Zaidan Avail (2311104059)
def hapus_semua_item():
    daftar_belanjaan.clear()
    daftar_harga.clear()
    print("Semua item telah dihapus dari daftar belanjaan.")

# Fungsi untuk menampilkan daftar belanjaan
# Zhafir Zaidan Avail (2311104059)
def tampilkan_daftar():
    if not daftar_belanjaan:
        print("Daftar belanjaan kosong.")
    else:
        print("Daftar Belanjaan:")
        for item in daftar_belanjaan:
            print(f"- {item}: {daftar_harga[item]}")

# Fungsi untuk menyortir daftar belanjaan
# Zhafir Zaidan Avail (2311104059)
def sortir_belanjaan():
    daftar_belanjaan.sort()

# Dimastian Aji Wibowo (2311104058)
# Fungsi untuk menghitung jumlah total item dalam daftar belanjaan
def hitung_jumlah_item():
    jumlah_item = len(daftar_belanjaan)
    print(f"Jumlah total item dalam daftar belanjaan adalah {jumlah_item}.")

# Fungsi untuk menghitung total harga semua item dalam daftar belanjaan
# Dimastian Aji Wibowo (2311104058)
def hitung_total_harga():
    total_harga = sum(daftar_harga[item] for item in daftar_belanjaan)
    print(f"Total harga semua item dalam daftar belanjaan adalah {total_harga}.")

# Fungsi untuk meminta input ulang jika input salah
# Dimastian Aji Wibowo (2311104058)
def input_ulang(prompt):
    while True:
        data = input(prompt)
        if data.strip():  # Memastikan input tidak kosong
            return data
        else:
            print("Input tidak valid. Silakan coba lagi.")

# Fungsi utama
# Putra Strata Tandika Setyawan (2311104050)
def main():
    while True:
        print("\nPilihan:")
        print("1. Tambah item")
        print("2. Hapus item")
        print("3. Cari item")
        print("4. Tampilkan daftar belanjaan")
        print("5. Hapus semua item dari daftar belanjaan")
        print("6. Hitung jumlah total item")
        print("7. Hitung total harga")
        print("8. Keluar")

        pilihan = input_ulang("Masukkan pilihan Anda: ")

        if pilihan == "1":
            items = input_ulang("Masukkan nama item (pisahkan dengan koma untuk menambahkan beberapa item sekaligus): ")
            tambah_item(items)
        elif pilihan == "2":
            item = input_ulang("Masukkan nama item yang ingin dihapus: ")
            hapus_item(item)
        elif pilihan == "3":
            item = input_ulang("Masukkan nama item yang ingin dicari: ")
            cari_item(item)
        elif pilihan == "4":
            tampilkan_daftar()
        elif pilihan == "5":
            hapus_semua_item()
        elif pilihan == "6":
            hitung_jumlah_item()
        elif pilihan == "7":
            hitung_total_harga()
        elif pilihan == "8":
            print("Terima kasih, sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program utama
if _name_ == "_main_":
    main()



