'''import math

magasság = 35

sugár = 6.5

T=math.pi*sugár**2*magasság
T2=T**3

eredmény1= T2/100*75
eredmény2= eredmény1//100
print("Eredmény: ",eredmény2)'''



'''import math


m = 35

r = 6.5

T=round((math.pi*r**2*m),0)
print("Eredmény: (75%)",T)

eredmeny = T//100*25

print("Eredmény:  (25%)",eredmeny)'''


import math

r=float(input("Adja meg a sugarat: "))
magassag=float(input("Adja meg a magasságot: "))

V=math.pow(r,2)*math.pi*magassag 

print("Szükséges vízmennyiség",V*0.75)