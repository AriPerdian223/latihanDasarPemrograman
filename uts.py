#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Nama : Ari Perdian
#Kelas : J

while (True) :
    print ("=" * 20)
    print ("Kalukator")
    print ("=" * 20 + "\n")
    print ("1. Ruang Datar (Luas & keliling) ")
    print ("2. Ruang Bangun (Volume) ")
    print ("3. EQIT")

    a = int(input("Masukan Pilihan Anda 1/2/3 : "))
    if a==1 :
        print ("=" * 20)
        print ("Ruang Datar")
        print ("=" * 20 + "\n")

        print ("1. Persegi")
        print ("2. Persegi panjang")
        print ("3. Jajar Genjang")
        print ("4. Segitiga")
        print ("5. Belah Ketupat")
        print ("6. Layang - Layang")
        print ("7. Trapesium")
        print ("8. Lingkaran")

        b = int(input("Masukan Pilihan Anda 1/2/3/4/5/6/7/8 : \n"))
        if b == 1 :
            print ("=== Persegi ===")
            c = int(input("Masukan Nilai sisi nya : "))
            d = c*c
            print ("Nilai Luasnya : ", d, "\n" "Nilai Kelilingnya : ", c*4, "\n" )

        elif b == 2 :
            print ("=== Persegi Panjang ===")
            panjang = int(input("Masukan Nilai panjang nya : "))
            lebar = int(input("Masukan Nilai lebar nya : "))
            luas = (panjang*lebar)
            print ("Nilai Luasnya : ", luas, "\n" "Nilai Kelilingnya : ", (2*panjang) + (2*lebar), "\n")

        elif b == 3 :
            print ("=== Jajar Genjang ===")
            jajar = int(input("Masukan Nilai alasnya nya : "))
            genjang = int(input("Masukan Nilai tinggi ya : "))
            sisi = int(input("Masukan Nilai Sisinya : "))
            hasil3 = (jajar*genjang)
            print ("Nilai Luasnya : ", hasil3, "\n" "Nilai Kelilingnya : ", (jajar+sisi+jajar+sisi), "\n")

        elif b == 4 :
            print ("=== Segitiga ===")
            alas = int(input("Masukan Nilai alasnya : "))
            tinggi = int(input("Masukan Nilai tingginya : "))
            kanan = int(input("Masukan Nilai sisinya : "))
            hasil = (1/2*alas*tinggi)
            print ("Nilai Luasnya : ", hasil, "\n" "Nilai Kelilingnya : ", (alas + kanan * 2 ))
        
        elif b == 5 :
            print ("=== Belah Ketupat ===")
            belah2 = int(input("Masukan Nilai diagonal 1 nya : "))
            belah3 = int(input("Masukan Nilai diagonal 2 nya : "))
            sisi2 = int(input("Masukan Nilai Sisinya : "))
            belah = (1/2*belah2*belah3)
            print ("Nilai Luasnya : ", belah, "\n" "Nilai Kelilingnya : ", 4*sisi2, "\n")

        elif b == 6 :
            print ("=== Layang - Layang ===")
            diag1 = int(input("Masukan Nilai diagonal 1 nya : "))
            diag2 = int(input("Masukan Nilai diagonal 2 nya : "))
            sisiatas = int(input("Masukan Nilai Sisi atas: "))
            sisibawah = int(input("Masukan Nilai Sisi bawah: "))
            belah = (1/2*diag1*diag2)
            print ("Nilai Luasnya : ", belah, "\n" "Nilai Kelilingnya : ", (sisibawah*2)+(sisiatas*2), "\n")

        elif b == 7 :
            print ("=== Trapesium ===")
            alasatas= int(input("Masukan Nilai atasnya : "))
            alasbawah = int(input("Masukan Nilai bawahnya : "))
            layang = int(input("Masukan Nilai Tingginya : "))
            miring = int(input("Masukan Nilai Sisi runcingnya : "))
            ke6 = (1/2*(alasatas + alasbawah)*layang)
            print ("Nilai Luasnya : ", ke6, "\n" "Nilai Kelilingnya : ", alasbawah + miring + alasatas + layang , "\n")

        elif b == 8 :
            print ("=== Lingkaran ===")
            r= float(input("Masukan Nilai jari - jari : "))
            phi = 3.14
            diameter = 2*r

            luas8 = phi*r*r
            keliling8 = phi*diameter

            print ("Nilai Luasnya : ", luas8, "\n" "Nilai Kelilingnya : ", keliling8)
    elif a==2 :
        print ("=" * 20)
        print ("Ruang Bangun")
        print ("=" * 20 + "\n")

        print ("1. Kubus")
        print ("2. Balok")
        print ("3. Prisma Segitiga")
        print ("4. Limas Segiempat")
        print ("5. Limas Segitiga")
        print ("6. Tabung")
        print ("7. Kerucut")
        print ("8. Bola")

        b1 = int(input("Masukan Pilihan Anda 1/2/3/4/5/6/7/8 : \n"))

        if b1 == 1 :
            print ("=== Kubus ===")
            c = int(input("Masukkan Nilai sisi nya : "))
            d = c**3
            print ("Nilai Volumenya : ", d, "\n")

        elif b1 == 2 :
            print ("=== Balok ===")
            panjang = int(input("Masukkan Nilai panjangnya : "))
            lebar = int(input("Masukkan Nilai lebarnya : "))
            tinggi = int(input("Masukkan Nilai Tingginya : "))
            v2 = (panjang*lebar*tinggi)
            print ("Nilai Volume : ", v2, "\n")

        elif b1 == 3 :
            print ("=== Prisma Segitiga ===")
            prisma1 = int(input("Masukkan Nilai alas : "))
            prisma2 = int(input("Masukkan Nilai tinggi segitiga : "))
            prisma3 = int(input("Masukkan Nilai tinggi prisma : "))
            v3 = ((1/2*prisma1*prisma2)*prisma3)
            print ("Nilai Volume : ", v3, "\n")

        elif b1 == 4 :
            print ("=== Limas Segiempat ===")
            limas1 = float(input("Masukkan Luas alas : "))
            limas2 = float(input("Masukkan Nilai tinggi : "))
            v4 = float(1/3*(limas1**2)*18)
            print ("Nilai Volume : ", v4, "\n")

        elif b1 == 5 :
            print ("=== Limas Segitiga ===")
            limas3 = float(input("Masukkan Nilai Luas alasnya : "))
            limas4 = float(input("Masukkan tinggi limas : "))
            v5 = float(1/3*limas3*limas4)
            print ("Nilai Volume : ", v5, "\n")

        elif b1 == 6 :
            print ("=== Tabung ===")
            tabung1 = float(input("Masukkan Jari jari : "))
            tabung2 = float(input("Masukkan tinggi : "))
            phi2 = 3.14 
            v6 = float(phi2*(tabung1**2)*tabung2)
            print ("Nilai Volume : ", v6, "\n")
            
        elif b1 == 7 :
            print ("=== Kerucut ===")
            keru1 = float(input("Masukkan Jari jari : "))
            keru2 = float(input("Masukkan tinggi : "))
            phi3 = 3.14 
            v7 = float(1/3*phi3*keru1*keru1*keru2)
            print ("Nilai Volume : ", v7, "\n")
        
        elif b1 == 8 :
            print ("=== Bola ===")
            Bol1 = float(input("Masukkan Jari jari : "))
            phi4 = 3.14 
            v8 = float(4/3*phi4*(Bol1**3))
            print ("Nilai Volume : ", v8, "\n")

        

    else:
        break

print("Terimakasih")


# In[ ]:




