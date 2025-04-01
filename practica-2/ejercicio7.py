import datetime
import random 
import string

def generar_codigo(usuario):
    fecha_actual = datetime.datetime.now().strftime("%d-%m-%Y")
    
    caracteres_random = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(15))

    return usuario.upper() + fecha_actual + caracteres_random


while True: 
    usuario = input("Ingrese un nombre de usuario no debe exceder los 15 caracteres")
    if (len(usuario) <= 15): 
        codigo_descuento = generar_codigo(usuario)
        break
    else:
        print("Nombre de usuario excede los 15 caracteres, intenta de nuevo")

print(f"El codigo de descuento es : {codigo_descuento}")
