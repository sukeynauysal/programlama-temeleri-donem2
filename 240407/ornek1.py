derece=int(input("suyun derecesini giriniz"))
if derece <0:
    print("su katıdir")
elif derece >=0 and derece <100:
    print("su sıvıdır")
else:
    print("su buhardır")