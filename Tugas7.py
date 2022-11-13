#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Nama : Ari Perdian
#Kelas : J

while (True):
    print ("=" * 30)
    print ("Program Kalkulator Sederhana")
    print ("=" * 30)
    
    print ("1. Menghitung Luas Segitiga")
    print ("2. Menghitung Luas Persegi Panjang")
    print ("3. Tentukan Number ganjil genap")
    print ("4. Quit")
    
    a = float(input("Masukan Pilihan Anda 1/2/3/4 : "))
    
    if a==1 :
        alas = float(input("Masukkan nilai Alas : "))
        tinggi = float(input("Masukkan nilai Tinggi : "))
        luas = 1/2 * alas * tinggi
        print ("Luas Segitiganya : ", luas, "\n")
        
    elif a==2 :
        panjang = float(input("Masukkan nilai panjang : "))
        lebar = float (input("Masukan nilai lebar : "))
        hasil = panjang * lebar
        print ("Luas Persegi panjangnya : ", hasil, "\n")
        
    elif a==3 :
        nilai = int(input("Masukan number : "))
        if (nilai % 2) == 0 :
            print (nilai, "Adalah bilangan genap" + "\n")
        else :
            print (nilai, "Adalah bilangan ganjil" + "\n")
            
    else:
        break
        
print ("Terimakasih")


# In[ ]:




