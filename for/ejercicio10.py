numb1= int(input("Ingrese un numero entero mayor a 0: "))

if numb1 <= 0:
    print("El numero que registró no es mayor a 0")

else:
    for i in range(1, 10):
        if numb1 % i== 0:
            print(i)