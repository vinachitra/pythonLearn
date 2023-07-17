# Belajar Membuat Method / Function

nama = []

# Terjadi pengulangan code

nama.append ("Adam")
print ("================")
for data in nama:
    print (data)

nama.append ("Noah")
print ("================")
for data in nama:
    print (data)

nama.append ("Levine")
print ("================")
for data in nama:
    print (data)

# Jika terjadi pengulangan code, maka kita bisa menggunakan method untuk mengefisienkan code

def print_nama(headerName):
    print("=========" + headerName +  "==========")
    for data in nama:
        print(data)

print_nama("Name List")

# nama.append ("Mehmet")
print_nama("Second Name list")

# nama.append ("Karaca")
print_nama("Third Name List")
