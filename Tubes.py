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
