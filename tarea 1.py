print("Tarea 1\n")
calificacion=float(input("Por favor, ingresa la calificación entre 0 y 10\n"))
if calificacion>=0 and calificacion<6:
    print('Corresponde a una "NA"')

elif calificacion>=6 and calificacion<7.6:
    print('Corresponde a una "S"')

elif calificacion>=7.6 and calificacion<8.6:
    print('Corresponde a una "B"')

elif calificacion>=8.6 and calificacion<=10:
    print('Corresponde a una "MB"')

else:
    print("Calificación no válida")

    
