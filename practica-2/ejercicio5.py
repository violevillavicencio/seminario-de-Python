rangos = [
    (lambda x: x < 200, "Rapido"),
    (lambda x: 200 <= x <= 500, "Normal"),
    (lambda x: x > 500, "Lento")
]

numero = int(input("Ingrese un número de tiempo de reacción: "))

for funcion, mensaje in rangos:
    if funcion(numero):
        print(mensaje)
        break
