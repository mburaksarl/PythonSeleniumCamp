#PYTHON SELENIUM KURSU 1. HAFTA ÖDEV

#1- Python'da Veri Tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklamalar yazınız.

#Veri Tipleri =
   #•String : Metinsel veri tipidir.
   #•Integer : Sayisal veri tipidir.
   #•Float : Ondalikli sayi tipidir.
   #•Boolean : True ve false değeri tipidir.
   #•List : Birden çok ögeyi tutar.
   #•Dictionary: Key ve values değerlerinden oluşur.
   
#2- Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.


#String Veri Tipi : Kurs isimleri, kurs açıklaması, eğitmenin bilgileri,
#Int(Integer) Veri Tipi : Yorum sayıları ve ders tamamlama yüzdesi


#3- Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.

#Oturum Açma Ekranı

eposta=input("Epostanızı giriniz")
sifre=input("Şifrenizi giriniz")


if eposta==("123456@gmail.com") and sifre ==("123456"):
    print ("Giriş Başarılı")
else:
    print("E-posta veya şifre yanlış tekrar deneyin")