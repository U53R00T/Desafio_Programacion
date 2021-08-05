cadena=(input("Ingrese la cadena: "))
print("Cadena Ingresada: "+cadena)
cod = []
i=0
k=0
#   Convierto la cadena de caracteres en codigo ASCII. 
for letra in cadena:
    cod.append(ord(letra))
for i in range(0,1):
    print ("Cadena convertida: '{}'".format(cod))
    print(" Resultado Final")
for i in range(len(cadena)):
    j =int(cod[i]-97) 
    if -1 < j < 15:
        k= j-j%3-1
        for k in range(k,j):
            m=int(2+j/3)
            print(m,end="")
    if 14 < j < 19: 
        k=14
        for k in range(k,j):
            print(7,end="")
    if 18 < j < 22:
        k=18
        for k in range(k,j):
            print(8,end="")
    if 21 < j < 26:
        k=21
        for k in range(k,j):
            print (9,end="") 
    if cod[i]==32:
        print(0,end="")