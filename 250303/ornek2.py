urun1=int(input("1. ürünün fiyatını giriniz"))
urun2=int(input("2. ürünün fiyatını giriniz"))
fiyat=urun1+urun2
if fiyat>=200:
    print("ödenecek miktar" ,fiyat ,"tl dir")
else:
    odeme=fiyat*0,75
    print("ödenecek miktar indirimden sonra", odeme , "tl dir")