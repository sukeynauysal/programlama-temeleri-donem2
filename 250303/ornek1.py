bagaj=int(input("bagajınızın kilosunu giriniz"))
if bagaj>=20:
    print("herhangi bir ücret ödemeniz gerekmiyor") 
else:
    fark=bagaj-20
    print("fazla bagaj için" ,fark*10, "ödemeniz gerekir")
print("iyi yolculaklar")
