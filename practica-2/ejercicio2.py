titles = [
"Speedrun de Super Mario en tiempo récord",
"Charla sobre desarrollo de videojuegos",
"Jugando al nuevo FPS del momento con amigos",
"Música en vivo: improvisaciones al piano"
]

mas_larga = max(titles, key=lambda frase: len(frase.split()))
print(mas_larga)
