numb1= int(input("Ingrese la cantidad de notas: "))

notes= []
counter=0

while numb1 > counter:
    noteX= float(input("Ingrese sus notas aquí: "))
    notes.append(noteX)
    counter+=1

average= sum(notes) / numb1

print(average)