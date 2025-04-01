rules = """Respeta a los demás. No se permiten insultos ni lenguaje ofensivo.
Evita el spam. No publiques enlaces sospechosos o repetitivos.
No compartas información personal.
Usa los canales adecuados para cada tema.
Sigue las instrucciones de los moderadores."""

lineas = rules.splitlines()

palabra = input('ingresa una palabra')

cumplen = [linea for linea in lineas if palabra.lower() in linea.lower()]

for elem in cumplen:
    print(elem)
