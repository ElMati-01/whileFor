numb= int(input("Ingrese numero: "))

if numb> 10:
    result= 1
    i = 1
    while i <= 10:
        result *= i
        i += 1
else:
    result = 0
    i = 1
    while i <= numb:
        result+=i
        i += 1

print(result)
