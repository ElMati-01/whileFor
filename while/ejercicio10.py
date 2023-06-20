
numb1 = 3
student = int(input("Número de estudiantes: "))
notes = []

while student > 0:
    counter = 0
    while numb1 > counter:
        noteX = float(input("Ingrese la nota: "))
        notes.append(noteX)
        counter += 1

    noteHigh = max(notes)  
    noteLow = min(notes)  
    average = sum(notes) / numb1

    print(f"La nota más alta es: {noteHigh}, la más baja es: {noteLow} y el promedio es: {average}.")

