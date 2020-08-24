# Importamos las funciones necesarias de los otros modulos
from lorem_convert import text_to_string
from contar import (contar_frase, contar_parrafos, contar_palabras,
                    contar_palindromos, contar_palabras_repetidas,
                    contar_tuplas_repetidas)


# El main del proyecto, donde juntamos todo
def main():
    texto = text_to_string()
    n_parrafos = contar_parrafos(texto)
    n_frases = contar_frase(texto)
    n_palabras = contar_palabras(texto)
    n_palindromos = contar_palindromos(texto)
    n_palabras_repetidas = contar_palabras_repetidas(texto)
    n_tuplas_repetidas = contar_tuplas_repetidas(texto)
    return n_parrafos + "\n" + n_frases + "\n" + n_palabras + "\n" + \
        n_palindromos + "\n" + n_palabras_repetidas + "\n" + n_tuplas_repetidas


if __name__ == "__main__":
    print(main())
