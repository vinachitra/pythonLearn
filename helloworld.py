print ("Hello World")

print ("Selamat Belajar")

# ini untuk membuat komentar
print ("Hello") # komentar di ujung

# untuk membuat angka tidak perlu menggunakan "", karena hanya digunakan untuk jenis data String/Text
print (44)
print (4.24)
print ("44") #ini menjadi text dan tidak bisa digunakan untuk operasi matematika

# Operasi matematika

# Tambah
print (23 + 45)

# Kurang
print (19909 - 6753)

# Kali
print (87 * 70)

# Bagi
print (90 / 5)

# Sisa Bagi
print (55 % 2)

# Membuat variable, jangan membuat variable yang sama dengan intruksi dari phyton (contohnya print)
hello = "Hello World" # variable

print (hello)
print (hello)

hello = "Hello Phyton" #untuk merubah data di banyak intstruksi, cukup dengan merubah variable
print (hello)
print (hello)
print (hello)

# Belajar String

nama = "Sezer Furkan Kirpitci"
kota = 'Istanbul'
alamat = 'Umraniye'

nama_depan = "Sezer"
nama_tengah = "FUrkan"
nama_belakang = "Kirpitci"
nama_lengkap = nama_depan + " " + nama_tengah + " " + nama_belakang

print (nama_lengkap)

# String-Format

#sapa = "Halo " + nama_depan + " " + nama_tengah + " " + nama_belakang #String Biasa
1#sapa = f"Halo {nama_depan} {nama_tengah} {nama_belakang}" #Strimg Format (gunakan huruf f di depan text)

#print (sapa)

# Belajar Input Data

# print ("Silakan Inputkan Nama : ")
#nama = input ()

#print (f"Hello {nama}. Selamat Datang")

# Belajar Input Number

print ("Angka Pertama : ")
#a = input () #input jenis ini membuat data yang diinput menjadi string, jadi operasi matematika tidak bisa berjalan
a = int (input ()) # jika ingin input angka, harus menggunakan integer 

print ("Angka Kedua : ")
#b = input ()
b = int (input ())

hasil = a + b
print (f"{a} + {b}  = {hasil}")

# Tipe Data Boolean (cuma 2 nilai : benar/true atau salah/false)

menikah = False
jomblo = True

print (menikah)
print (jomblo)

# Operator Logika (digunakan  untuk tipe data Boolean)
# Ada 2 jenis : dan (and) & atau (or)

print (True and True)
print (True and False)
print (False and True)
print (False and False)

print (True or True)
print (True or False)
print (False or True)
print (False or False)



