# Parte 1: Cargar los datos
def cargar_datos(lineas_archivo):
    generos_peliculas= []
    peliculas_por_genero = []
    info_peliculas = []

    for linea in lineas_archivo:
        datos_pelicula = linea.split(",")

        titulo = datos_pelicula[0]
        popularidad = float(datos_pelicula[1])
        voto_promedio = float(datos_pelicula[2])
        cantidad_votos = int(datos_pelicula[3])
        generos = datos_pelicula[4]

        lista_generos_pelicula=generos.split(";")

        info_peliculas.append((titulo, popularidad, voto_promedio, cantidad_votos, lista_generos_pelicula))

        for genero in lista_generos_pelicula:
            if generos_peliculas.count(genero) == 0:
                generos_peliculas.append(genero)

    for genero_actual in generos_peliculas:
        peliculas_del_genero = []

        for pelicula in info_peliculas:
            titulo_pelicula = pelicula[0]
            generos_pelicula = pelicula[4]
            if generos_pelicula.count(genero_actual) > 0:
                peliculas_del_genero.append(titulo_pelicula)

        peliculas_por_genero.append((genero_actual, peliculas_del_genero))

    return generos_peliculas, peliculas_por_genero, info_peliculas

# Parte 2: Completar las consultas
def obtener_puntaje_y_votos(nombre_pelicula):
    lineas_archivo = leer_archivo()
    generos_peliculas, peliculas_por_genero, info_peliculas = cargar_datos(lineas_archivo)

    voto_promedio = None
    cantidad_votos = None

    for pelicula in info_peliculas:
        titulo_pelicula = pelicula[0]
        if titulo_pelicula == nombre_pelicula:
            voto_promedio = pelicula[2]
            cantidad_votos = pelicula[3]
            break
    return voto_promedio, cantidad_votos


def filtrar_y_ordenar(genero_pelicula):
    lineas_archivo = leer_archivo()
    generos_peliculas, peliculas_por_genero, info_peliculas = cargar_datos(lineas_archivo)
    peliculas_filtradas = []

    for par_genero_lista in peliculas_por_genero:
        genero_actual = par_genero_lista[0]
        lista_peliculas = par_genero_lista[1]

        if genero_actual == genero_pelicula:
            peliculas_filtradas = lista_peliculas
            break
    peliculas_filtradas.sort(reverse=True)
    return peliculas_filtradas

def obtener_estadisticas(genero_pelicula, criterio):
    lineas_archivo = leer_archivo()
    generos_peliculas, peliculas_por_genero, info_peliculas = cargar_datos(lineas_archivo)
    valores_criterio = []

    for pelicula in info_peliculas:
        generos_pelicula = pelicula[4]

        if generos_pelicula.count(genero_pelicula) > 0:
            if criterio == "popularidad":
                valores_criterio.append(pelicula[1])
            elif criterio == "voto promedio":
                valores_criterio.append(pelicula[2])
            elif criterio == "cantidad votos":
                valores_criterio.append(pelicula[3])
    
    maximo = valores_criterio[0]
    minimo = valores_criterio[0]
    suma = 0
    for valor in valores_criterio:
        suma += valor
        if valor > maximo:
            maximo = valor
        if valor < minimo:
            minimo = valor
    promedio = suma / len(valores_criterio)
    
    return maximo, minimo, promedio

# NO ES NECESARIO MODIFICAR DESDE AQUI HACIA ABAJO

def solicitar_accion():
    print("\n¿Qué desea hacer?\n")
    print("[0] Revisar estructuras de datos")
    print("[1] Obtener puntaje y votos de una película")
    print("[2] Filtrar y ordenar películas")
    print("[3] Obtener estadísticas de películas")
    print("[4] Salir")

    eleccion = input("\nIndique su elección (0, 1, 2, 3, 4): ")
    while eleccion not in "01234":
        eleccion = input("\nElección no válida.\nIndique su elección (0, 1, 2, 3, 4): ")
    eleccion = int(eleccion)
    return eleccion


def leer_archivo():
    lineas_peliculas = []
    with open("peliculas.csv", "r", encoding="utf-8") as datos:
        for linea in datos.readlines()[1:]:
            lineas_peliculas.append(linea.strip())
    return lineas_peliculas


def revisar_estructuras(generos_peliculas, peliculas_por_genero, info_peliculas):
    print("\nGéneros de películas:")
    for genero in generos_peliculas:
        print(f"    - {genero}")

    print("\nTítulos de películas por genero:")
    for genero in peliculas_por_genero:
        print(f"    genero: {genero[0]}")
        for titulo in genero[1]:
            print(f"        - {titulo}")

    print("\nInformación de cada película:")
    for pelicula in info_peliculas:
        print(f"    Nombre: {pelicula[0]}")
        print(f"        - Popularidad: {pelicula[1]}")
        print(f"        - Puntaje Promedio: {pelicula[2]}")
        print(f"        - Votos: {pelicula[3]}")
        print(f"        - Géneros: {pelicula[4]}")


def solicitar_nombre():
    nombre = input("\nIngrese el nombre de la película: ")
    return nombre


def solicitar_genero():
    genero = input("\nIndique el género de película: ")
    return genero


def solicitar_genero_y_criterio():
    genero = input("\nIndique el género de película: ")
    criterio = input(
        "\nIndique el criterio (popularidad, voto promedio, cantidad votos): "
    )
    return genero, criterio


def main():
    lineas_archivo = leer_archivo()
    datos_cargados = True
    try:
        generos_peliculas, peliculas_por_genero, info_peliculas = cargar_datos(
            lineas_archivo
        )
    except TypeError as error:
        if "cannot unpack non-iterable NoneType object" in repr(error):
            print(
                "\nTodavía no puedes ejecutar el programa ya que no has cargado los datos\n"
            )
            datos_cargados = False
    if datos_cargados:
        salir = False
        print("\n********** ¡Bienvenid@! **********")
        while not salir:
            accion = solicitar_accion()

            if accion == 0:
                revisar_estructuras(
                    generos_peliculas, peliculas_por_genero, info_peliculas
                )

            elif accion == 1:
                nombre_pelicula = solicitar_nombre()
                ptje, votos = obtener_puntaje_y_votos(nombre_pelicula)
                print(f"\nObteniendo puntaje promedio y votos de {nombre_pelicula}")
                print(f"    - Puntaje promedio: {ptje}")
                print(f"    - Votos: {votos}")

            elif accion == 2:
                genero = solicitar_genero()
                nombres_peliculas = filtrar_y_ordenar(genero)
                print(f"\nNombres de películas del género {genero} ordenados:")
                for nombre in nombres_peliculas:
                    print(f"    - {nombre}")

            elif accion == 3:
                genero, criterio = solicitar_genero_y_criterio()
                estadisticas = obtener_estadisticas(genero, criterio)
                print(f"\nEstadísticas de {criterio} de películas del género {genero}:")
                print(f"    - Máximo: {estadisticas[0]}")
                print(f"    - Mínimo: {estadisticas[1]}")
                print(f"    - Promedio: {estadisticas[2]}")

            else:
                salir = True
        print("\n********** ¡Adiós! **********\n")


if __name__ == "__main__":
    main()
