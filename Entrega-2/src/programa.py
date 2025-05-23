from src.funciones import *

rounds = [
    {
        'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
        'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
        'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
        'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': False},
    },
    {
        'Shadow': {'kills': 1, 'assists': 2, 'deaths': False},
        'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
        'Viper': {'kills': 1, 'assists': 1, 'deaths': False},
        'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
        'Reaper': {'kills': 0, 'assists': 1, 'deaths': False},
    },
    {
        'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
        'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
        'Viper': {'kills': 2, 'assists': 1, 'deaths': False},
        'Frost': {'kills': 0, 'assists': 1, 'deaths': True},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': False},
    },
    {
        'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
        'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
        'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
        'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': True},
    }
]

# Inicializar datos
jugadores, mvps = inicializar_estadisticas(rounds)

# Procesar cada ronda
for i, ronda in enumerate(rounds, start=1):
    puntajes_ronda = procesar_ronda(ronda, jugadores)
    mvp = max(puntajes_ronda, key=puntajes_ronda.get)
    mvps[mvp] += 1
    print(f"MVP de la ronda: {mvp} ({puntajes_ronda[mvp]} puntos)")
    mostrar_resultados_ronda(i, ronda, puntajes_ronda)

# Mostrar ranking final
mostrar_ranking_final(jugadores, mvps) 
