numb= int(input("Ingrese un numero "))

i=1
add=0
counter= 0

while numb > i:
     if numb % 2!=0:
        add+=i
        counter+=1
     i+=1

else:
    print("El numero digitado no es impar")

print(f"La suma es: {add} y el numero de impares son: {counter}")

