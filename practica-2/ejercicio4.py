nombre = input("Ingrese nombre de usuario: ")
cumple = False

if (len(nombre) >= 5 
    and any(char.isdigit() for char in nombre) 
    and any(char.isupper() for char in nombre) 
    and nombre.isalnum()):
    print(f"Nombre de usuario {nombre} válido.")
    cumple = True

if not cumple:
    print(f"Nombre de usuario {nombre} inválido.")

