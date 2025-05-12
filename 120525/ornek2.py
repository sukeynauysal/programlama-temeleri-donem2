gecme=0
notlar=[]
toplam=0
for i in range (0,6,1):
    notlar.append(int (input( "notları girin")))
for j in notlar:
    toplam=toplam + j
    if j <50:
        gecme=gecme+1
ortalama=toplam/6
print("des notlarının ortalaması :" , ortalama)
print("kaldınız not sayısı :" , gecme)