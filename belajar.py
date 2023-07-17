print("Hello")

# Operator Perbandingan : hasilnya dalam bentuk Boolean (True or False)
#
# > lebih dari
# < kurang dari
# >= lebih dari sama dengan
# <= kurang dari sama dengan
# == sama dengan
# != tidak sama dengan

print (3 > 5)
print (3 < 5)
print (3 >= 5)
print (3 <=  5)
print (3 == 3)
print (3 != 5)

print ("Sezer" != "Onur")
print ("Chitra" == "Chitra")

# Belajar If-Statement

orang = 100
zombi = 100

if orang < zombi :
    print ("Kabur, dunia mau kiamat")

if orang > zombi :
    print ("Mari basmi Zombi")

if orang == zombi :
    print ("Mari bersiap berperang") 

#Belajar If Else

menang = False

if menang == True :
    print ("Selamat")

else :
    print ("Silakan Coba Lagi")

# Belajar Elif : program yang menerima input dari user (input ()) dan menampilkan hasil yang sesuai dengan data yang diinput user

menu_pilihan = input ("Silakan pilih menu [1-3] : ")

if menu_pilihan == "1" :
    print ("Anda memilih menu 1")
elif menu_pilihan == "2" : # penggunaan elif bertujuan untuk tidak dieksekusinya pilihan sebelumnya
    print ("Anda memilih menu 2")
elif menu_pilihan == "3" :
    print ("Anda memilih menu 3")
else :
    print ("Menu Tidak Tersedia")

if menu_pilihan == "x" : # jika dibuat if yang baru, akan melanjutkan perintah baru
    print ("Program Gagal")


