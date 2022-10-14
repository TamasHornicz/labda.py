import math

hektar = int(input("Terület hektárban: "))
sebesseg = int(input("Traktor sebessége (km/h): "))
terulet = hektar*10000


ms = (sebesseg/3.6)*5 #5m széles eke 

ido = terulet/ms
ora = ido//3600
perc = round((ido/60),1)


print("Várható munkaidő: ",ora,"óra és",perc,"perc!")


