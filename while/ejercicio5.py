

numb1 = int(input("Ingrese el total de sus facturas: "))

counter = 0
billTotalX = 0

while numb1 > counter:
    bill = float(input("Ingrese el valor de la factura: "))
    counter += 1
    if bill <= 0:
        print("Se cierra la cuenta.")
    else:
        billTotalX += bill

if billTotalX > 1000:
    discount = billTotalX * 0.1
    totalPay = billTotalX - discount
else:
    totalPay = billTotalX

print(f"El total a pagar es: {totalPay}")






