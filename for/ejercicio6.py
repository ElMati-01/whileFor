numb1= int(input("Digite el primer numero: "))
numb2= int(input("Digite el segundo numero: "))

print(f"Lista entre {numb1} y {numb2}:")

if numb1 < numb2:
    for i in range (numb1, numb2+1):
        print(i)


else:
    print("El primer numero no es valido")
