# Tratamos el txt obtenido para convertiro en una string que
# Python pueda leer y operar mas facilmente
def text_to_string():
    file = open("resources/lorem_ipsum.txt")
    lorem_string = file.read().replace("\n", " ")
    file.close()
    return lorem_string
