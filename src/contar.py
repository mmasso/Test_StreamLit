# Cargamos de la libreria Collections las clases que necesitaremos
from collections import Counter, defaultdict


def contar_parrafos(texto):

    # Asignamos a la varible el la longitud del resultado de dividir el
    # texto para obtener el numero de parrafos.
    n_parrafos = len(texto.split(".  "))

    # Devolvemos en un string el número de parrafos obtenido
    return "El número de parrafos es de: " + str(n_parrafos)


def contar_frase(texto):

    # Separando el texto por puntos y espacio obtendremos la cantidad
    # de frases del texto dado
    n_frases = len(texto.split(". "))

    # Devolvemos el numero obtenido de frases anterior
    return "El número de frases es de: " + str(n_frases)


def contar_palabras(texto):

    # Separamos el texto dado por sus espacios para contar las
    # palabras y obtener su número
    n_palabras = len(texto.split())

    # Devolvemos el numero de palabras obtenido
    return "El número de palabras es de: " + str(n_palabras)


# Funcion de contar.py, usable para obtener una lista de palabras,
# tratada para ser correctamente comparable entre si.
def _tratar_lista(texto):

    # creamos lista de palabras del texto separandolas por sus espacios
    lista_palabras = texto.split()

    # Inicializamos lista vacia donde añadiremos las palabras tratadas
    tratada_lista_palabras = list()

    # Por cada palabra de la lista, nos aseguramos que no tengan ni
    # espacios ni puntos ni comas, y que esten todas en minuscula, y las
    # añadimos a la nueva lista
    for palabra in lista_palabras:
        palabra = palabra.strip()
        palabra = palabra.strip(".")
        palabra = palabra.strip(",")
        palabra = palabra.lower()
        tratada_lista_palabras.append(palabra)
    return tratada_lista_palabras


# Función auxiliar a contar_palindromos para detectar si una
# palabra es igual o no a su inversa
def _es_palindromo(palabra):
    return palabra.lower() == palabra.lower()[::-1]


# CONTAR PALINDROMOS #

# Función auxiliar para comprobar que la palabra ya existiera
# en la lista de palindromos
def _ya_era_palindromo(palabra, lista_palindromos):
    if palabra in lista_palindromos:
        return False
    return True


def contar_palindromos(texto):

    # Creamos lista de palabras del texto separadas por espacios
    lista_palabras = texto.split()

    # Creamos lista vacia de posibles palindromos
    lista_palindromos = list()

    # Por cada palabra de la lista que sea palindromo y de mas de un
    # cáracter la añadimos a la lista de palindromos si no estaba ya
    # previamente
    for palabra in lista_palabras:
        if _es_palindromo(palabra) and len(palabra) > 1 \
                and _ya_era_palindromo(palabra, lista_palindromos):
            lista_palindromos.append(palabra)
    return "El número de palíndromos es de: " + str(len(lista_palindromos)) + \
        " siendo: " + str(lista_palindromos)


# CONTAR PALABRAS #

# Funcion auxiliar de contar_palabras_repetidas:
# Formateamos los resultados obtenidos en forma de diccionario de la
# cantidad de palabras repetidas para representarlo en una string leible
def _representar_lista_valores(dicc_palabras_repetidas, lista_keys_repetidas):

    # string que devolveremos con el contenido entendible y leible
    string_final = "Las palabras más repetidas són:"

    # Por cada palabra de la lista con las palabras repetidas,
    # miraremos su valor en el diccionario para sacar sus repeticiones
    for key in lista_keys_repetidas:
        string_final += "\n" + "'" + key + "' con " + \
            str(dicc_palabras_repetidas.get(key)) + " repeticiones"

    # Devolvemos el string obtenido
    return string_final


# Funcion auxiliar de contar_palabras_repetidas() para sacar del
# diccionario las 5 claves cuyo valor sea el máximo
def _lista_llaves_mas_repetidas(dict_palabras):

    # Inicializamos contador
    i = 0

    # Inicializamos lista para añadir las palabras mas repetidas
    lista_mas_repetidas = list()

    # Copiamos el diccionario para no dañar el original
    dict_palabras_copy = dict_palabras.copy()

    # Mientras que el contador no llegue a 5, buscaremos el valor maximo
    # del diccionario, guardaremos su llave en la lista y eliminaremos este
    # valor del diccionario copiado, e sumaremos una al contador.
    while i < 5:
        lista_mas_repetidas.append(
            max(dict_palabras_copy, key=dict_palabras_copy.get))
        dict_palabras_copy.pop(
            max(dict_palabras_copy, key=dict_palabras_copy.get))
        i += 1

    # Devolvemos la lista de las palabras mas repetidas
    return lista_mas_repetidas


# funcion auxiliar de contar_palabras_repetidas, para crear un diccionario
# con las palabras mas repetidas y el numero de veces que lo estan
def _crear_dict_repetidas(texto):

    # asignamos una lista de palabras del texto tratada para su uso
    lista_palabras = _tratar_lista(texto)

    # inicializamos diccionario vacio
    dict_palabras = dict()

    # por cada palabra de la lista, miramos si esta en el diccionario, si
    # lo esta, le sumamos una al recuento, y si no, lo añadimos al diccionario
    # con valor de recuento 1
    for palabra in lista_palabras:
        if palabra in dict_palabras:
            dict_palabras[palabra] += 1
        else:
            dict_palabras[palabra] = 1

    # devolvemos el diccionario con lo obtenido
    return dict_palabras


# funcion donde reunimos todas las funciones auxiliares anteriores para
# devolver una string con la cantidad de palabras repetidas
def contar_palabras_repetidas(texto):
    dict_palabras = _crear_dict_repetidas(texto)
    lista_keys_repetidas = _lista_llaves_mas_repetidas(dict_palabras)
    string_lista_valores = _representar_lista_valores(
        dict_palabras, lista_keys_repetidas)
    return string_lista_valores


# CONTAR_TUPLAS #

# Funcion auxiliar de contar_mas_repetidas donde tenemos una lista de
# palabras y el numero de palabras que queremos que sean contadas a la vez
# de manera secuencial
def _count_secuencias(lista_palabras, n):

    # inicializamos un diccionario defaultdict que nos permitira no tener que
    # tratar con KeyError cuando no existe una llave dada y devuelve default
    count_dict = defaultdict(int)

    # En el rango del numero total de palabras, menos el numero de palabras
    # que queremos que sea la tupla
    for i in range(len(lista_palabras) - n + 1):

        # la llave sera una tupla con las posiciones de la posicion i hasta
        # la posicion de i mas el largo de la tupla deseado n
        key = tuple(lista_palabras[i: i + n])

        # le sumamos a su valor 1 para su contabilizacion
        count_dict[key] += 1

    # Devolvemos el diccionario
    return count_dict


# Funcion auxiliar para contar_tuplas_repetidas donde contaremos las tuplas
# mas repetidas de dos o mas palabras de largo
def _contar_mas_repetidas(lista_palabras, texto):

    # Inicializamos diccionario vacio para introducir todos los diccionarios
    # generados con _count_secuencias()
    dict_total = dict()

    # Inicializamos el contador cuyo valor lo basaremos en el resultado de la
    # division entre el numnero de palabras y el numero de oraciones, para una
    # media aproximada de palabras por frase, convertido a int por si es float
    contador = int(len(texto.split()) / len(texto.split(". "))) + 1

    # Mientras el contador sea mayor o igual que 2, asignaremos al contador
    # el numero de palabras que queremos que este compuesta la tupla y se lo
    # pasaremos a _count_secuencias()
    while contador >= 2:
        n = contador
        count_dict = _count_secuencias(lista_palabras, n)

        # Añadiremos el diccionario al creado anteriormente
        dict_total.update(count_dict)

        # Restamos 1 al contador
        contador -= 1

    # Devolvemos las 5 mas comunes usando Counter, que nos crea un diccionario
    # con las mas comunes a partir de un iterable
    return Counter(dict_total).most_common(5)


# Funcion auxiliar de contar_tuplas_repetidas:
# Formateamos los resultados obtenidos en forma de lista de la
# cantidad de palabras repetidas para representarlo en una string leible
def _representar_lista_tuplas(list_total):

    # Inicializamos string para devolver
    string_final = "Las tuplas más repetidas són:"

    # Por cada elemento de la lista, cogemos su primer y segundo valor para
    # Formatearlo e añadirlo a la string
    for element in list_total:
        string_final += "\n" + \
            str(element[0]) + " con " + str(element[1]) + " repeticiones"

    # Devolvemos la sting
    return string_final


# funcion donde reunimos todas las funciones auxiliares anteriores para
# devolver una string con la cantidad de tuplas repetidas
def contar_tuplas_repetidas(texto):
    lista_palabras = _tratar_lista(texto)
    list_mas_repetidas = _contar_mas_repetidas(lista_palabras, texto)
    string_lista_tuplas = _representar_lista_tuplas(list_mas_repetidas)
    return string_lista_tuplas
