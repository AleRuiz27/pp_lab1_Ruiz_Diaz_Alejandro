import json
import csv
import re
from typing import List, Dict

with open("dt.json") as jugadores_file:
    data = json.load(jugadores_file)
    lista_jugadores = data["jugadores"]



  

def mostrar_nombre_jugadores(lista_jugadores):
    for i, jugador in enumerate(lista_jugadores, start=1):
        nombre = jugador["nombre"]
        posicion = jugador["posicion"]
        print("{0}. Nombre: {1} - Posición: {2}".format(i, nombre, posicion))


def mostrar_nombre_posicion(lista_jugadores):
    """
    Esta función toma una lista de jugadores, imprime sus nombres y posiciones, y permite al usuario seleccionar un jugador.

    :param lista_jugadores: una lista de diccionarios que contienen información sobre cada jugador,
    incluido su nombre, posición y estadísticas
    :return: el diccionario del jugador seleccionado o None si no se seleccionó ningún jugador válido
    """
    print("Lista de jugadores:")
    for i, jugador in enumerate(lista_jugadores, start=1):
        nombre = jugador["nombre"]
        posicion = jugador["posicion"]
        print("{0}. Nombre: {1} - Posición: {2}".format(i, nombre, posicion))

    respuesta_jugador = input("Seleccione un jugador por su índice (1-{0}): ".format(len(lista_jugadores)))
    respuesta_jugador_int = int(respuesta_jugador)
    if respuesta_jugador_int >= 1 and respuesta_jugador_int <= len(lista_jugadores):
        jugador_seleccionado = lista_jugadores[respuesta_jugador_int - 1]

        print("Detalles del jugador seleccionado:")
        print("Nombre:", jugador_seleccionado["nombre"])
        print("Posición:", jugador_seleccionado["posicion"])
        print("Estadísticas:")
        for estadistica, valor in jugador_seleccionado["estadisticas"].items():
            print("- {0}: {1}".format(estadistica, valor))

        return jugador_seleccionado  # Devolver el jugador seleccionado
    else:
        print("Número de jugador inválido.")
        return None  # Devolver None si no se seleccionó ningún jugador válido



def guardado_De_Estadisticas_cvs(jugador_seleccionado, rutacsv):
    """
    Esta función guarda las estadísticas de un jugador seleccionado en un archivo CSV.
    
    :param jugador_seleccionado: Un diccionario que contiene las estadísticas del jugador seleccionado
    :param rutacsv: La ruta del archivo donde se guardará el archivo CSV
    """
    rutacsv = r"C:\Users\madruiz\tareapyhton\Parcial\estadisticas.csv"
    
    with open(rutacsv, "w", newline="") as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(["Estadística", "Valor"])
        for estadistica, valor in jugador_seleccionado["estadisticas"].items():
            writer.writerow([estadistica, valor])

    print(f"se a guardado las estadisticas en archivo CSV{rutacsv}")

def jugador_por_nombre(nombre_jugador):
    """
    Esta función toma el nombre de un jugador como entrada, lo busca en una lista de jugadores y
    devuelve sus logros en los campeonatos de la NBA si los encuentra.
    
    :param nombre_jugador: El nombre del jugador cuyos logros en los campeonatos de la NBA se van a
    mostrar
    :return: un valor booleano, ya sea Verdadero o Falso, dependiendo de si un jugador con el nombre
    dado se encuentra en la lista de jugadores o no. Si se encuentra al jugador, su nombre y logros se
    imprimen y se devuelve True. Si no se encuentra el reproductor, se devuelve Falso.
    """
   
    nombre_jugador = nombre_jugador.lower()
    
    for jugadores in lista_jugadores:
        if nombre_jugador in jugadores["nombre"].lower():
            nombre = jugadores["nombre"]
            logros = jugadores["logros"]
            print(f"los logros de {nombre} en los campeonatos de la nba:")

            for logro in logros:
                print(logro)

            return True
    return False

def calculo_promedio(lista_jugadores:list[dict],sub_clave:str):
    """
    Esta función calcula el promedio de una estadística específica para una lista de jugadores.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores y sus estadísticas
    :type lista_jugadores: list[dict]
    :param sub_clave: La sub_clave es una cadena que representa una estadística específica de un
    jugador, como "puntos" (puntos), "rebotes" (rebotes) o "asistencias" (asistencias). Se utiliza para
    acceder al valor correspondiente en las "estadisticas" (estadísticas
    :type sub_clave: str
    :return: el valor de la variable "promedio", que representa la media de una determinada estadística
    ("sub_clave") para todos los jugadores de la lista de entrada "lista_jugadores". Si la lista de
    entrada está vacía, la función no ejecutará el ciclo y devolverá Ninguno.
    """
    acomulador = 0
    contador = 0
    
    if lista_jugadores:
        for jugador in lista_jugadores:
            acomulador += jugador["estadisticas"][sub_clave]
            contador += 1
        if contador > 0:
            promedio = acomulador / contador
            print(f"El promedio total de {sub_clave.replace('_',' ')} de todos los jugadores es: {promedio}")
    return promedio

    

    
def promedio_puntos_partido(lista_jugadores):
    """
    La función toma una lista de jugadores y sus estadísticas, extrae sus puntos promedio por juego, los
    ordena alfabéticamente por nombre e imprime sus nombres y los puntos promedio correspondientes por
    juego.
    
    para lista_jugadores: una lista de diccionarios, donde cada diccionario representa un jugador y
    sus estadísticas. Cada diccionario tiene las siguientes claves: "nombre" (cadena), "estadisticas"
    (diccionario). El diccionario de "estadisticas" tiene las siguientes claves:
    "promedio_puntos_por_partido"
     se utliza la funcion lamba para utulizar una clave y ordenar una lista de tuplas por el elemento de la posicion 0 de cada tupla (
    """
    promedios = []

    for jugador in lista_jugadores:
        nombre = jugador["nombre"]
        promedios_puntos = jugador["estadisticas"]["promedio_puntos_por_partido"]
        promedios.append((nombre, promedios_puntos))

    promedios_En_orden = sorted(promedios, key = lambda x: x[0])


    print("el promedio de puntos de partidos de Dream Team es: ")

    for jugador, promedios in promedios_En_orden:
        print(f"{jugador}: {promedios}")


def si_es_miembro_De_sala(lista_jugadores):
    """
    Esta función verifica si un jugador determinado es miembro de un salón de la fama del baloncesto al
    buscar en una lista de jugadores y sus logros.
    
    :param lista_jugadores: una lista de diccionarios que contienen información sobre jugadores de
    baloncesto, incluido su nombre y logros
    :return: un valor booleano (Verdadero o Falso) dependiendo de si el nombre del jugador ingresado es
    miembro del salón de la fama del baloncesto o no.
    """
    nombre_jugador_sala = input("ingrese el nombre el jugador que quiere comprobar si es miembro de la sala: ")
    while not nombre_jugador_sala.isalpha():
        print("El nombre debe contener solo letras. Inténtalo nuevamente.")
        nombre_jugador_sala = input("Ingrese el nombre del jugador que desea verificar si es miembro del salón de la fama: ")
    
    nombre_jugador_sala = nombre_jugador_sala.lower()

    for jugador in lista_jugadores:
        if nombre_jugador_sala in jugador["nombre"].lower():
            logros = jugador["logros"]
            if "Miembro del Salon de la Fama del Baloncesto" in logros:
                return True
           
    return False

def calcular_estadisticas_jugadores(lista_jugadores):
    """
    La función calcula e imprime las estadísticas de los jugadores con mayor porcentaje de rebotes,
    tiros y asistencias.
    
    :param lista_jugadores: una lista de diccionarios, donde cada diccionario representa a un jugador y
    contiene su nombre y estadísticas (rebotes, porcentaje de tiros de campo y total de asistencias)
    """
    jugador_max_rebotes = max(lista_jugadores, key=lambda jugador: jugador["estadisticas"]["rebotes_totales"])
    jugador_max_porcentaje_tiros = max(lista_jugadores, key=lambda jugador: jugador["estadisticas"]["porcentaje_tiros_de_campo"])
    jugador_max_asistencias = max(lista_jugadores, key=lambda jugador: jugador["estadisticas"]["asistencias_totales"])

    print("Jugador con la mayor cantidad de rebotes totales:")
    print(f"Nombre: {jugador_max_rebotes['nombre']}")
    print(f"Rebotes totales: {jugador_max_rebotes['estadisticas']['rebotes_totales']}")

    print("\nJugador con el mayor porcentaje de tiros de campo:")
    print(f"Nombre: {jugador_max_porcentaje_tiros['nombre']}")
    print(f"Porcentaje de tiros de campo: {jugador_max_porcentaje_tiros['estadisticas']['porcentaje_tiros_de_campo']}")

    print("\nJugador con la mayor cantidad de asistencias totales:")
    print(f"Nombre: {jugador_max_asistencias['nombre']}")
    print(f"Asistencias totales: {jugador_max_asistencias['estadisticas']['asistencias_totales']}")

def comparar_promedio_puntos(lista_jugadores):
    """
    La función compara el promedio de puntos por juego de una lista de jugadores con un valor dado e
    imprime los nombres y promedios de los jugadores con un promedio más alto.
    
    :param lista_jugadores: una lista de diccionarios, donde cada diccionario representa a un jugador y
    contiene su nombre y estadísticas (incluyendo su promedio de puntos por juego)
    """
    while True:
        puntos = input("Ingrese el valor de puntos para comparar con los promedios de puntos por partido: ")
        if puntos.isdigit():
            puntos = float(puntos)
            break
        else:
            print("Por favor, ingrese solo números.")

    jugadores_con_mayor_promedio = [jugador for jugador in lista_jugadores if jugador["estadisticas"]["promedio_puntos_por_partido"] > puntos]

    if jugadores_con_mayor_promedio:
        print(f"Jugadores con promedio de puntos por partido mayor que {puntos}:")
        for jugador in jugadores_con_mayor_promedio:
            print("Nombre:", jugador["nombre"])
            print("Promedio de puntos por partido:", jugador["estadisticas"]["promedio_puntos_por_partido"])
            print()
    else:
        print(f"No se encontraron jugadores con promedio de puntos por partido mayor que {puntos}.")


def comparar_promedio_rebotes(lista_jugadores):
    """
    Esta función compara los rebotes promedio por juego de los jugadores de baloncesto en una lista
    determinada con un valor ingresado por el usuario e imprime los nombres y los promedios de los
    jugadores con promedios más altos.
    
    :param lista_jugadores: una lista de diccionarios, donde cada diccionario representa a un jugador de
    baloncesto y contiene su nombre y estadísticas (incluido el promedio de rebotes por partido)
    """
    while True:
        rebotes = input("Ingrese el valor de rebotes para comparar con los promedios de rebotes por partido: ")
        if rebotes.isdigit():
            rebotes = float(rebotes)
            break
        else:
            print("Por favor, ingrese solo números.")

    jugadores_con_mayor_promedio = [jugador for jugador in lista_jugadores if jugador["estadisticas"]["promedio_rebotes_por_partido"] > rebotes]

    if jugadores_con_mayor_promedio:
        print(f"Jugadores con promedio de rebotes por partido mayor que {rebotes}:")
        for jugador in jugadores_con_mayor_promedio:
            print("Nombre:", jugador["nombre"])
            print("Promedio de rebotes por partido:", jugador["estadisticas"]["promedio_rebotes_por_partido"])
            print()
    else:
        print(f"No se encontraron jugadores con promedio de rebotes por partido mayor que {rebotes}.")

def comparar_promedio_asistencias(lista_jugadores):
    """
    La función compara las asistencias medias por partido de una lista de jugadores con un valor
    determinado e imprime los nombres y medias de los jugadores con una media superior.
    
    :param lista_jugadores: una lista de diccionarios, donde cada diccionario representa a un jugador y
    contiene su nombre y estadísticas (incluido el número promedio de asistencias por juego)
    """
    while True:
        asistencias = input("Ingrese el valor de asistencias para comparar con los promedios de asistencias por partido: ")
        if asistencias.isdigit():
            asistencias = float(asistencias)
            break
        else:
            print("Por favor, ingrese solo números.")

    jugadores_con_mayor_promedio = [jugador for jugador in lista_jugadores if jugador["estadisticas"]["promedio_asistencias_por_partido"] > asistencias]

    if jugadores_con_mayor_promedio:
        print(f"Jugadores con promedio de asistencias por partido mayor que {asistencias}:")
        for jugador in jugadores_con_mayor_promedio:
            print("Nombre:", jugador["nombre"])
            print("Promedio de asistencias por partido:", jugador["estadisticas"]["promedio_asistencias_por_partido"])
            print()
    else:
        print(f"No se encontraron jugadores con promedio de puntos por partido mayor que {asistencias}.")


def calcular_estadisticas_jugadores_rebotes_porcentaje_asistencias(lista_jugadores):
    """
    Esta función calcula e imprime las estadísticas de los jugadores con más rebotes, porcentaje de
    tiros de campo y asistencias totales.
    
    :param lista_jugadores: una lista de diccionarios, donde cada diccionario representa a un jugador y
    contiene su nombre y estadísticas (incluidos el total de rebotes, el porcentaje de tiros de campo y
    el total de asistencias)
    """
    
    jugador_max_rebotes = max(lista_jugadores, key=lambda jugador: jugador["estadisticas"]["rebotes_totales"])
    jugador_max_porcentaje_tiros = max(lista_jugadores, key=lambda jugador: jugador["estadisticas"]["porcentaje_tiros_de_campo"])
    jugador_max_asistencias = max(lista_jugadores, key=lambda jugador: jugador["estadisticas"]["asistencias_totales"])

    print("Jugador con la mayor cantidad de rebotes totales:")
    print(f"Nombre: {jugador_max_rebotes['nombre']}")
    print(f"Rebotes totales: {jugador_max_rebotes['estadisticas']['rebotes_totales']}")

    print("\nJugador con el mayor porcentaje de tiros de campo:")
    print(f"Nombre: {jugador_max_porcentaje_tiros['nombre']}")
    print(f"Porcentaje de tiros de campo: {jugador_max_porcentaje_tiros['estadisticas']['porcentaje_tiros_de_campo']}")

    print("\nJugador con la mayor cantidad de asistencias totales:")
    print(f"Nombre: {jugador_max_asistencias['nombre']}")
    print(f"Asistencias totales: {jugador_max_asistencias['estadisticas']['asistencias_totales']}")




def comparar_porcentaje_tiros_libres(lista_jugadores):
    """
    La función toma una lista de jugadores y un valor ingresado por el usuario, y devuelve una lista de
    jugadores con un porcentaje de tiros libres mayor que el valor ingresado.
    
    :param lista_jugadores: una lista de diccionarios, donde cada diccionario representa a un jugador y
    contiene su nombre y estadísticas (incluido su porcentaje de tiros libres)
    "Ingrese el valor para comparar con el porcentaje de tiros libres: "
    """
    while True:
        valor_ingresado = input( "Ingrese el valor para comparar con el porcentaje de tiros libres: ")
        if valor_ingresado.isdigit():
            valor_ingresado = float(valor_ingresado)
            break
        else:
            print("Por favor, ingrese solo números.")

    jugadores_con_mayor_porcentaje = [jugador for jugador in lista_jugadores if jugador["estadisticas"]["porcentaje_tiros_libres"] > valor_ingresado]

    if jugadores_con_mayor_porcentaje:
        print(f"Jugadores con porcentaje de tiros libres mayor que {valor_ingresado}:")
        for jugador in jugadores_con_mayor_porcentaje:
            print("Nombre:", jugador["nombre"])
            print("Porcentaje de tiros libres:", jugador["estadisticas"]["porcentaje_tiros_libres"])
            print()
    else:
        print(f"No se encontraron jugadores con porcentaje de tiros libres mayor que {valor_ingresado}.")

def encontrar_promedio_puntos_minimo(lista_jugadores):
    """
    Esta función encuentra al jugador con el promedio de puntos más bajo por juego, identifica a los
    jugadores con promedios más altos y calcula el promedio de esos promedios más altos.
    
    :param lista_jugadores: una lista de diccionarios, donde cada diccionario representa a un jugador y
    contiene su nombre y estadísticas (incluyendo su promedio de puntos por juego)
    """
    
    jugador_minimo = min(lista_jugadores, key=lambda jugador: jugador["estadisticas"]["promedio_puntos_por_partido"])

    
    jugadores_superiores = [jugador for jugador in lista_jugadores if jugador["estadisticas"]["promedio_puntos_por_partido"] > jugador_minimo["estadisticas"]["promedio_puntos_por_partido"]]

    total_promedio = sum(jugador["estadisticas"]["promedio_puntos_por_partido"] for jugador in jugadores_superiores) / len(jugadores_superiores)


    print("Jugador con el promedio de puntos más bajo:")
    print("Nombre:", jugador_minimo["nombre"])
    print("Promedio de puntos por partido:", jugador_minimo["estadisticas"]["promedio_puntos_por_partido"])
    print()

    print("Jugadores con promedio de puntos superior al mínimo:")
    for jugador in jugadores_superiores:
        print("Nombre:", jugador["nombre"])
        print("Promedio de puntos por partido:", jugador["estadisticas"]["promedio_puntos_por_partido"])
    print()

    print("Promedio total de los jugadores con promedio de puntos superior al mínimo:", total_promedio)
    print()



def jugador_mayor_logros(lista_jugadores: list[dict]):
    """
    La función encuentra al jugador con más logros en una lista de jugadores.
    
    :param lista_jugadores: una lista de diccionarios que representan a los jugadores, donde cada
    diccionario contiene información sobre un jugador, incluido su nombre y una lista de sus logros o
    "logros"
    :type lista_jugadores: list[dict]
    """
    jugador_mayores_logros = None
    logros_mayor = 0

    for jugador in lista_jugadores:
        cantidad_de_logros = len(jugador["logros"])
        if cantidad_de_logros > logros_mayor:
            logros_mayor = cantidad_de_logros
            jugador_mayores_logros = jugador["nombre"]

    print(f"El jugador con mayor logros es {jugador_mayores_logros} con una cantidad de {logros_mayor}")


def mostrar_jugadores_mayor_porcentaje_triples(lista_jugadores):
    # El código anterior solicita al usuario que ingrese un valor, lo convierte en un flotador y luego
    # filtra una lista de jugadores de baloncesto según su porcentaje de tiros de 3 puntos. Luego
    # imprime los nombres y los porcentajes de tiros de 3 puntos de los jugadores que tienen un
    # porcentaje más alto que el valor de entrada. Si no hay jugadores con un porcentaje superior,
    # imprime un mensaje indicándolo.
    while True:
        valor_ingresado = input("Ingrese un valor para comparar con el porcentaje de tiros triples: ")
        if valor_ingresado.isdigit():
            valor_ingresado = float(valor_ingresado)
            break
        else:
            print("Por favor, ingrese solo números.")

    jugadores_con_mayor_porcentaje = [jugador for jugador in lista_jugadores if jugador["estadisticas"]["porcentaje_tiros_triples"] > valor_ingresado]

    if jugadores_con_mayor_porcentaje:
        print(f"Jugadores con porcentaje de tiros triples mayor a {valor_ingresado}:")
        for jugador in jugadores_con_mayor_porcentaje:
            print("Nombre:", jugador["nombre"])
            print("Porcentaje de tiros triples:", jugador["estadisticas"]["porcentaje_tiros_triples"])
            print()
    else:
        print(f"No se encontraron jugadores con porcentaje de tiros triples mayor a {valor_ingresado}.")


def jugador_con_mas_temporadas(lista_jugadores):
    """
    Esta función encuentra al jugador con más temporadas jugadas de una lista de jugadores e imprime su
    nombre y el número de temporadas jugadas.
    
    :param lista_jugadores: una lista de diccionarios, donde cada diccionario representa a un jugador y
    contiene información como su nombre y estadísticas. La función encuentra al jugador con más
    temporadas jugadas y devuelve su nombre y el número de temporadas que jugó
    """
    jugador_mayor_temporadas = None
    max_temporadas = 0

    for jugador in lista_jugadores:
        temporadas = jugador["estadisticas"]["temporadas"]
        if temporadas > max_temporadas:
            max_temporadas = temporadas
            jugador_mayor_temporadas = jugador["nombre"]

    if jugador_mayor_temporadas:
        print(f"Jugador con la mayor cantidad de temporadas jugadas: {jugador_mayor_temporadas}")
        print(f"Cantidad de temporadas: {max_temporadas}")
    else:
        print("No se encontraron jugadores.")

def mostrar_jugadores_superiores_porcentaje(lista_jugadores: List[Dict[str, any]]):
    # El código anterior solicita al usuario que ingrese un valor porcentual, filtra una lista de
    # jugadores de baloncesto en función de que su porcentaje de tiros de campo sea mayor que el valor
    # ingresado, ordena la lista filtrada por posición del jugador y luego imprime los nombres, las
    # posiciones y el campo. porcentajes de goles de los jugadores filtrados y ordenados. Si ningún
    # jugador cumple con los criterios de filtrado, se imprime un mensaje que indica que no se
    # encontraron jugadores.
    while True:
        porcentaje = input("Ingrese el valor de porcentaje para comparar con los tiros de campo: " )
        if porcentaje.isdigit():
            porcentaje = float(porcentaje)
            break
        else:
            print("Por favor, ingrese solo números.")
    
    jugadores_filtrados = [jugador for jugador in lista_jugadores if jugador["estadisticas"].get("porcentaje_tiros_de_campo", 0) > porcentaje]
    jugadores_ordenados = sorted(jugadores_filtrados, key=lambda jugador: jugador["posicion"])

    if jugadores_ordenados:
        print(f"Jugadores con porcentaje de tiros de campo superior a {porcentaje}%:")
        for jugador in jugadores_ordenados:
            print("Nombre:", jugador["nombre"])
            print("Posición:", jugador["posicion"])
            print("Porcentaje de tiros de campo:", jugador["estadisticas"]["porcentaje_tiros_de_campo"])
            print()
    else:
        print(f"No se encontraron jugadores con porcentaje de tiros de campo superior a {porcentaje}%.")

def obtener_posiciones_rankings(lista_jugadores: List[Dict[str, any]]):
   
    jugadores_ordenados_puntos = sorted(lista_jugadores, key=lambda jugador: jugador["estadisticas"]["puntos_totales"], reverse=True)
    jugadores_ordenados_rebotes = sorted(lista_jugadores, key=lambda jugador: jugador["estadisticas"]["rebotes_totales"], reverse=True)
    jugadores_ordenados_asistencias = sorted(lista_jugadores, key=lambda jugador: jugador["estadisticas"]["asistencias_totales"], reverse=True)
    jugadores_ordenados_robos = sorted(lista_jugadores, key=lambda jugador: jugador["estadisticas"]["robos_totales"], reverse=True)

    
    jugadores_posiciones = []
    for i, jugador in enumerate(lista_jugadores):
        jugador_posicion = {
            "nombre": jugador["nombre"],
            "posicion_puntos": i + 1,
            "posicion_rebotes": i + 1,
            "posicion_asistencias": i + 1,
            "posicion_robos": i + 1
        }
        jugadores_posiciones.append(jugador_posicion)

    return jugadores_posiciones

while True:
    respuesta = input("Seleccione una opción:\n"
                  "1) Mostrar la lista de todos los jugadores del Dream Team.\n"
                  "2) Seleccionar un jugador por su índice y mostrar sus estadísticas completas.\n"
                  "3) Guardar estadísticas en un archivo CSV.\n"
                  "4) Buscar jugador por nombre.\n"
                  "5) Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team,"
                  " ordenado por nombre de manera ascendente.\n"
                  "6) Si es miembro del salón de la fama.\n"
                  "7) Máximos de cantidad de rebotes, porcentaje de tiros y cantidad de asistencias de cada jugador.\n"
                  "8) Ingresar valor y mostrar jugadores con mayor promedio por puntos de partido del valor ingresado.\n"
                  "9) Ingresar puntos y mostrar jugadores con mayor promedio por rebotes.\n"
                  "10) Ingresar puntos y mostrar jugadores con mayor promedio de asistencias.\n"
                  "11) Máximos en rebotes, porcentaje de tiros y asistencias.\n"
                  "12) Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.\n"
                  "13) Promedio de puntos de los jugadores excepto el mínimo.\n"
                  "14) Mostrar el jugador con la mayor cantidad de logros obtenidos.\n"
                  "15) Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.\n"
                  "16) Jugadores con mayor temporadas jugadas.\n"
                  "17) Ingresar un valor y mostrar los jugadores, ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.\n"
                  "18) ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.\n"
                  "Opción: ")

  
    respuesta_int = int(respuesta)



    match(respuesta_int):
        case 1:
            mostrar_nombre_jugadores(lista_jugadores)
        case 2:
           jugador_seleccionado = mostrar_nombre_posicion(lista_jugadores)
        case 3:

            guardado_De_Estadisticas_cvs(jugador_seleccionado, rutacsv= r"C:\Users\madruiz\tareapyhton\Parcial\estadisticas.csv")

        case 4:
            mostrar_nombre_jugadores(lista_jugadores) 
            nombre_jugador = input("Indique el nombre del jugador que quiera buscar: ")

            jugador_Econtrado = jugador_por_nombre(nombre_jugador)

            if not jugador_Econtrado:
                print("el jugador indicado no esta en la lista")


        case 5:
            promedio_puntos_partido(lista_jugadores)
            calculo_promedio(lista_jugadores,"promedio_puntos_por_partido")


        case 6:

            es_miembro = si_es_miembro_De_sala(lista_jugadores)

            if es_miembro:
                print("El jugador es miembro del Salón de la Fama del Baloncesto.")
            else:
                print("El jugador no es miembro del Salón de la Fama del Baloncesto.")
            
        case 7:

                calcular_estadisticas_jugadores(lista_jugadores)


        case 8:
                   
               comparar_promedio_puntos(lista_jugadores)

        case 9:
                comparar_promedio_rebotes(lista_jugadores)

        case 10:
                comparar_promedio_asistencias(lista_jugadores)

        case 11:
                calcular_estadisticas_jugadores_rebotes_porcentaje_asistencias(lista_jugadores)

        case 12: 
                comparar_porcentaje_tiros_libres(lista_jugadores)

        case 13:
                encontrar_promedio_puntos_minimo(lista_jugadores)

        case 14:
                jugador_mayor_logros(lista_jugadores)

        case 15:
                mostrar_jugadores_mayor_porcentaje_triples(lista_jugadores)

        case 16:

                jugador_con_mas_temporadas(lista_jugadores)

        case 17:
                mostrar_jugadores_superiores_porcentaje(lista_jugadores)

        case 18: 

                obtener_posiciones_rankings(lista_jugadores)


    
