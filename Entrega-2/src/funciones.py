def inicializar_estadisticas(rounds):
    jugadores = {}
    mvps = {jugador: 0 for jugador in rounds[0]}
    return jugadores, mvps

def calcular_puntos(kills, assists, deaths):
    return kills * 3 + assists - (1 if deaths else 0)

def procesar_ronda(ronda, jugadores):
    puntajes_ronda = {}
    for jugador, stats in ronda.items():
        kills = stats['kills']
        assists = stats['assists']
        deaths = stats['deaths']
        puntos = calcular_puntos(kills, assists, deaths)

        if jugador not in jugadores:
            jugadores[jugador] = {'kills': 0, 'assists': 0, 'deaths': 0, 'puntos': 0}

        jugadores[jugador]['kills'] += kills
        jugadores[jugador]['assists'] += assists
        jugadores[jugador]['deaths'] += 1 if deaths else 0
        jugadores[jugador]['puntos'] += puntos

        puntajes_ronda[jugador] = puntos
    return puntajes_ronda

def mostrar_resultados_ronda(i, ronda, puntajes_ronda):
    print(f"Ranking ronda {i}:")
    print(f"{'Jugador':<10}{'Kills':<7}{'Asistencias':<12}{'Muertes':<8}{'Puntos':<7}")
    for jugador, puntos in puntajes_ronda.items():
        stats = ronda[jugador]
        kills = stats['kills']
        assists = stats['assists']
        deaths = 1 if stats['deaths'] else 0
        print(f"{jugador:<10}{kills:<7}{assists:<12}{deaths:<8}{puntos:<7}")
    print("-" * 40)

def mostrar_ranking_final(jugadores, mvps):
    for jugador in jugadores:
        jugadores[jugador]['mvps'] = mvps[jugador]

    ranking_final = sorted(jugadores.items(), key=lambda x: x[1]['puntos'], reverse=True)

    print("\nRanking final:")
    print(f"{'Jugador':<10}{'Kills':<7}{'Asistencias':<12}{'Muertes':<8}{'MVPs':<6}{'Puntos':<7}")
    for jugador, stats in ranking_final:
        print(f"{jugador:<10}{stats['kills']:<7}{stats['assists']:<12}{stats['deaths']:<8}{stats['mvps']:<6}{stats['puntos']:<7}")
