#sıra sizdeler b

sayilar=[10,11,12,13,14,15,16,17,18,19,20]
sayilar2=[21,22,23,24,25]
sayilar.extend(sayilar2)
for i in sayilar:
    if  i %4==0:
        print(i)
