toplam=0
sayi1=int(input("sayı girin :"))
sayi2=int(input("sayı girin :"))
for i in range(sayi1,sayi2):
    if i %2 == 0:
        toplam=toplam+i
        print("çift 2 sayının toplam değeri :", toplam)

