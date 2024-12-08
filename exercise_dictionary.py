Number = [1000, 100, 41, 78, 69, 90, 3]
Number.sort()

lenght = len(Number) - 1
Number[lenght]

print(f"Minimun value {Number[0]}")
print(f"Maximum value {Number[lenght]}")

value = 0
Buah = [
            # ['Apel', 20, 10000],
            # ['Jeruk', 15, 15000],
            # ['Anggur', 15, 20000]
            {
                "Nama" : "Apel",
                "Stok" : 20,
                "Harga" : 10000
            },
            {
                "Nama" : "Jeruk",
                "Stok" : 15,
                "Harga" : 15000
            },
            {
                "Nama" : "Anggur",
                "Stok" : 15,
                "Harga" : 20000
            },
        ]
while value != 5:
    print("""Selamat datang di pasar buah

          Menu List:
            1 : Menampilkan menu buah
            2 : Menambah Buah
            3 : Menghapus Buah
            4 : Membeli Buah
            5 : exit program
          """)
    value = int(input("Masukkan angka yang akan dipilih : "))
    
    if value == 1:
        tampilan = 'Index | Nama | Stock | Harga \n'
        for i in Buah:
            tampilan += f"{Buah.index(i) + 1} "
            for j in i.values():
                tampilan += f"| {j}"
            tampilan += f"\n"
        print(tampilan)
    elif value == 2:
        buah = input("Masukkan nama buah : ")
        stok = input("Masukkan stok buah : ")
        harga = input("Masukkan harga buah : ")
        full_data = dict(Nama=f"{buah}", Stok=f"stok", Harga=f"{harga}")
        Buah.append(full_data)
        print("Tambah Data Berhasil")
    elif value == 3:
        idx = int(input("Masukan nomor index buah yang ingin dihapus : "))
        del Buah[idx - 1] 
        print("Data berhasil terhapus")
    elif value == 4:
        cart = []
        stop = False 
        while stop != True:
            idxbuah = int(input("Masukan nomor index buah yang ingin dibeli : ")) - 1
            stokbuah = int(input("Masukan jumlah stok buah yang ingin dibeli : "))
            value_idx_buah = Buah[idxbuah]
            if stokbuah > int(value_idx_buah['Stok']):
                print(f"Stok tidak cukup, stok {value_idx_buah['Nama']} tinggal {value_idx_buah['Stok']}")
            else:
                # data_dibeli = []
                # data_dibeli.append(value_idx_buah['Nama'])
                # data_dibeli.append(stokbuah)
                # data_dibeli.append(value_idx_buah['Harga'])
                # cart.append(data_dibeli)
                data_pembelian = dict(Nama=f"{value_idx_buah['Nama']}",Stok=f"{stokbuah}",Harga=f"{value_idx_buah['Harga']}")
                cart.append(data_pembelian)

            # print(cart)
            tampilan2 = 'Nama | Qty | Harga \n'
            for i in cart:
                tampilan2 += f"{cart.index(i) + 1} "
                for j in i.values():
                    tampilan2 += f"| {j}"
                tampilan2 += f"\n"
            print(tampilan2)
        
            check_stop = input("Ingin melanjutkan tidak ? (Ya/Tidak) : ")
            if check_stop == "Ya":
                stop = False
            else:
                stop = True
        
        total = 0
        for val in cart:
            # print("val")
            # print(val['Stok'])
            temp_total = int(val["Stok"]) * int(val["Harga"])
            total += temp_total


        print(f"Total belanjaan anda adalah {total}")
        bayar = int(input("Uang yang bayar adalah : "))
        if total > bayar:
            print("Uangmu ga cukup cug!!")
        else:
            sisa = bayar - total
            print(f"Ini uang kembalianmu : {sisa}")
            print("Terima kasih sudah belanja")

            for i in cart:
                for j in Buah:
                    if j["Nama"] == i["Nama"]:
                        sisa_stok = int(j["Stok"]) - int(i["Stok"])
                        j['Stok'] = sisa_stok
                    else:
                        continue

    elif value == 5:
        print("Terima Kasih Sudah Menggunakan Program ini")