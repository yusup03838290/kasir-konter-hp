# Aplikasi Kasir Konter HP - by yusup03838290
# Untuk konter HP di Tangerang

stok = []

def tambah_barang():
    nama = input("Nama barang (HP/Case/Charger): ")
    harga = int(input("Harga jual: "))
    stok.append({"nama": nama, "harga": harga})
    print(f"{nama} berhasil ditambah!")

def lihat_laporan():
    total = sum([b['harga'] for b in stok])
    print("\n=== LAPORAN KONTER HARI INI ===")
    for b in stok:
        print(f"- {b['nama']}: Rp{b['harga']}")
    print(f"Total Omzet: Rp{total}")
    print("================================")

while True:
    print("\n1. Tambah Barang")
    print("2. Lihat Laporan")
    print("3. Keluar")
    pilih = input("Pilih: ")
    if pilih == "1":
        tambah_barang()
    elif pilih == "2":
        lihat_laporan()
    elif pilih == "3":
        print("Terima kasih!")
        break
