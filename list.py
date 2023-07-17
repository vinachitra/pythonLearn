# Belajar List

#nama = []

nama = ["Reva", "Sandra", "Monika", "Reo", "Hendi", "Krisna"]
# atau
nama.append ("Revina") # append digunakan untuk penambahan data
nama.append ("Chitra")
nama.append ("Sagita")
nama.append ("Sezer")
nama.append ("Furkan")
nama.append ("Kirpitci")
        
print (nama)

# bisa juga memanggil dengan menggunakan indeks seperti array

print (nama [0])
print (nama [3])
print (nama [5])
print (nama [8])

# untuk mengecek berapa banyak data yang ada disini, dengan menggunakan len

print(len (nama))

# untuk menghapus data, kita bisa menggunakan perintah remove

# nama.remove ("masukkan data yang ingin diremove")

# Belajar Tuple : untuk menyimpan data lebih dari 1, beda dengan list, ini menggunakan ()
# Tuple digunakan untuk data yang tidak bisa berubah, tidak bisa dihapus 

pelanggan = ("Reditya", "Ariseno")

print (pelanggan)

# dengan indeks

print (pelanggan [0])
print (pelanggan [1])

# Belajar set : kegunaannya untuk menyimpan data lebih dari 1

# list []
# tuple ()
# set {} : data harus unik, jika ada data yang sama, maka akan dihapus (cocok untuk data yang tidak ada duplikat)
# posisi indeksnya bisa berubah dan hanya bisa digunakan untuk for loop
# untuk menambah data bisa digunakan add

nama = {"Chitra", "Sagita", "Chitra", "Sagita", "Revina"}
nama.add ("Sezer")
nama.add ("Furkan")
nama.add ("Kirpitci")

for data in nama:
    print (data)

# nama.remove ("nama yang akan dihapus")

print (nama)



