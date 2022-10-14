import math

'''db_labda=input('Adja meg a labda számát: ')
atmero=input('Adja meg a labda átmérőjét: ')
masni=60
math.pi

kerület= float(math.pi*atmero)
masnihossz= (masni+db_labda*kerület)
'''

db_labda=int(input("Labdák száma: "))

K=30*math.pi #1x a kerülete a labdának

szalag=round(((2*K+60)*db_labda),0)

'''print("Szalagmennyiség (m): ",(szalag//100)+1)'''

print("Szalagmennyiség (m): ",(szalag//100)+1)