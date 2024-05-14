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


