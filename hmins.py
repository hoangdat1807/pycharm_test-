t=int(input("mơi nhap so giay"))
h=(t//3600)%24
min=(t%3600)//60
second=(t%3600)%60
print(h,":",min,":",second)
