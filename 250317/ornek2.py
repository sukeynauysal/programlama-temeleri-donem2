adet=int(input("kaç tane alcaksınız :"))
birim_fiyat=int(input("ürün birim fiyatını giriniz :"))
toplam=adet*birim_fiyat
if toplam <= 3000:
    toplam=toplam-toplam*0.20
    print ("ürünlerin tutarı : ",toplam)
else:
    toplam=toplam-100
    print("ürünlerini tutarı :", toplam)
