def penjumlahan():
    x=int(input("nilai 1 = "))
    y=int(input("nilai 2 = "))
    hasil= x+y
    print("hasil = ",hasil)

def pengurangan():
    x = int(input("nilai 1 = "))
    y = int(input("nilai 2 = "))
    hasil = x-y
    print("hasil = ",hasil)

def perkalian():
    x = int(input("nilai 1 = "))
    y = int(input("nilai 2 = "))
    hasil = x*y
    print("hasil = ",hasil)

def pembagian():
    x = int(input("nilai 1 = "))
    y = int(input("nilai 2 = "))
    hasil = x/y
    print("hasil = ",hasil)
    
def perkalian():
    x = int(input("nilai 1 = "))
    y = int(input("nilai 2 = "))
    hasil = x*y
    print("hasil = ",hasil)

def mencaridiameter():
    x = int(input("masukkan jari-jari(r) = "))
    hasil = x*x
    print("hasil = ",hasil)

def mencariluaslingkarankelipatan7():
    x = int(input("masukkan jari-jari 1(r1) = "))
    y = int(input("masukkan jari-jari 2(r2) = "))
    hasil = 22/7 * x * y
    print("hasil = ",hasil)

def mencariluaslingkaranbukankelipatan7():
    x = int(input("masukkan jari-jari 1(r1) = "))
    y = int(input("masukkan jari-jari 2(r2) = "))
    hasil = 3.14 * x * y
    print("hasil = ",hasil)

def mencarijarijari():
    x = int(input("masukkan nilai diameter (d) = "))
    hasil = 1/2 * x
    print("hasil = ",hasil)

def mencarikelilinglingkarankelipatan7():
    x = int(input("masukkan jari-jari(r) = "))
    hasil= 2 * 22/7 * x 
    print("hasil = ",hasil)

def mencarikelilinglingkaranbukankelipatan7():
    x = int(input("masukkan jari-jari(r) = "))
    hasil= 2 * 3.14 * x 
    print("hasil = ",hasil)


print("silahkan pilih ya :D")
print("")
print("1. penjumlahan")
print("2. pengurangan")
print("3. perkalian")
print("4. pembagian")
print("5. mencari diameter")
print("6. mencari luas lingkaran (kelipatan 7)")
print("7. mencari luas lingkaran (bukan kelipatan 7)")
print("8. mencari jari jari")
print("9. mencari keliling lingkaran(kelipatan 7)")
print("10. mencari keliling lingkaran(bukan kelipatan 7)")
print("")


pilihan = int(input("pilihan ="))
if pilihan == 1 :
    penjumlahan()
elif pilihan == 2 :
    pengurangan()
elif pilihan == 3 :
    perkalian ()
elif pilihan == 4 :
    pembagian ()
elif pilihan == 5 :
    mencaridiameter ()
elif pilihan == 6 :
    mencariluaslingkarankelipatan7()
elif pilihan == 7:
    mencariluaslingkaranbukankelipatan7()
elif pilihan == 8 :
    mencarijarijari()
elif pilihan == 9 :
    mencarikelilinglingkarankelipatan7()
elif pilihan == 10 :
    mencarikelilinglingkaranbukankelipatan7()
else:
    print("eror")







