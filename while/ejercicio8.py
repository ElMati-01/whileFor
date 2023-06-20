numb1= int(input("Ingrese un numero entero mayor a 0: "))

div= []
i=1
while numb1 > i:
    if numb1 % i== 0:
        div.append(i)
    i+=1
print(div)

