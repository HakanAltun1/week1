#Hakan ALTUN
sayi1 = int(input("İlk Sayıyı Giriniz :"))
sayi2 = int(input("İkinci Sayıyı Giriniz :"))
islem = input("Lütfen İşlemi Seçiniz :")


if islem == "+":
    sonuc=sayi1+sayi2
    print("Sonuc =", sonuc)
elif islem == "-":
    sonuc = sayi1 - sayi2
    print("Sonuc =", sonuc)
elif islem == "*":
    sonuc = sayi1 * sayi2
    print("Sonuc =", sonuc)
elif islem == "/":
    sonuc = sayi1 / sayi2
    print("Sonuc =", sonuc)
else:
    print("Geçersiz Karakter Girdiniz Lütfen Kontrol Ediniz")