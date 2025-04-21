toplam=0
sayi1=int(input("küçük bir sayi giriniz:"))
sayi2=int(input("büyük bir sayi giriniz:"))
for sayi in range (sayi1,sayi2):
    toplam=toplam+sayi
hesap=sayi1-sayi2
ort=toplam/hesap
print("sayıların ortalamsını:",ort)
