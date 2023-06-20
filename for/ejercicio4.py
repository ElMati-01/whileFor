numb1= int(input("Ingrese un numero par: "))

if numb1 % 2==0:
    numbX=0
    for i in range (0,numb1,2):
        numbX+= i
        print(f"El numero es {numbX}")
else:
    print("No es numero par")
