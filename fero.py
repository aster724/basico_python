print("Promedio de cinco materias cursadas.")
print("-------------------------------------")
# En las siguientes lineas se muestra el metodo rjust()
# Tambien se pueden utilizar ljust() y center()
# En este caso estamos alineando el texto a la derecha a 35
# espacios del margen.
espanol = float(input("Calificacion Espanol: ".rjust(35)))
matematicas = float(input("Calificacion en Matematicas: ".rjust(35)))
economia = float(input("Calificacion en Economia: ".rjust(35)))
programacion = float(input("Calificacion en Programacion: ".rjust(35)))
ingles = float(input("Calificacion en Ingles: ".rjust(35)))

promedio = (espanol + matematicas + economia + programacion + ingles) / 5
print("El promedio de las cinco materias es :", promedio)
