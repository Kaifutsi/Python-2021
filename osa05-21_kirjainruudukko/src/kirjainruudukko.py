# Kirjoita ratkaisu tähän
n = int(input("Kerrokset: "))
 
aakkoset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 
vase = ""    
oike = ""   
k = n-1       
m = 2*n-1    
while k >= 1:
    vase = vase+aakkoset[k]
    oike = aakkoset[k]+oike
    m -= 2
    print(vase+aakkoset[k]*m+oike)
    k -= 1
while k <= n-1:
    print(vase+aakkoset[k]*m+oike)
    vase = vase[:-1]
    oike = oike[1:]
    m += 2
    k += 1








