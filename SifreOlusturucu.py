
import random
import time
dosya = open("Şifre.txt","w", encoding='utf-8')

karakter = ["q", "w", "e", "r", "t", "y", "u", "ı", "o", "p", "ğ", "ü", "a", "s", "d", "f", "g", "h", "j", "k", "l", "ş", "i", "z", "x", "c", "v", "b", "n", "m", "ö", "ç",
         "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
         "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "Ğ", "Ü", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Ş", "İ", "Z", "X", "C", "V", "B", "N", "M", "Ö", "Ç",
            "!", "^", "+", "%", "&", "/", "(", ")", "=", "?", "_", "-"]
#Şifrede olabilcek karakterleri girdik#

print("\n")
print("---OTOMATİK ŞİFRE OLUŞTURUCU---")
time.sleep(0.5)
print("\n ")
print("Lütfen Şİfre uzunluğu girin (min. 8, max. 20 olabilir)")
uzunluk = int(input(">>>"))
#Şİfre uzunluğumuzu giriyoruz#


if (8<uzunluk<20):
    for i in range(uzunluk):
        index = random.choice(karakter)
        dosya.write(str(index))

elif uzunluk <8 or uzunluk > 20:
    print("En az 8 en fazla 20 karakter uzunluğunda olmalı. Lütfen tekrar deneyin.")
    uzunluk = input(">>>")
    exit()
else:
    print("")
time.sleep(0.6)
print("\n")
print("Şifreniz hazırlanıyor...\n")
dosya.close()
time.sleep(2)
print("Bitti.\n")
time.sleep(0.6)

print("Şifreniz", dosya.name, "Dan alabilirsiniz")
