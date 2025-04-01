descriptions = [
"Streaming de música en vivo con covers y composiciones",
"Charla interactiva con la audiencia sobre series y películas",
"Jugamos a juegos retro y charlamos sobre su historia",
"Exploramos la mejor música de los 80s y 90s",
"Programa de entretenimiento con noticias y curiosidades del mundo gamer",
"Sesión de charla con invitados especiales del mundo del streaming",
"Música en directo con improvisaciones y peticiones del chat",
"Un espacio para charlar relajada sobre tecnología y cultura digital",
"Exploramos el impacto de la música en los videojuegos clásicos"
]

palabras_buscar = ["entretenimiento", "música", "charla"]

def count():
    for palabra in palabras_buscar:
        cantidad = sum(1 for linea in descriptions if palabra in linea.lower())
        print(f"Menciones de {palabra}: {cantidad}")

count()
