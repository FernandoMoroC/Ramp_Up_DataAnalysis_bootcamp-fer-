
def dia_de_la_semana(x: int):
    ''' 
    Transforma el numero en un dia de la semana
    Inputs:
    x:int
    Outputs:
    dias[x-1] : str    
    '''
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    return dias[x-1]


def pyramid(x):
    lista = list(range(x, 0, -1))

    for i in range(len(lista)):
        print(*lista)
        del lista[0]

def comparison(x,y):
    try:
        if x == y:
            return (f"{x} es igual a {y}")
        elif x > y:
            return (f"{x} es mayor que {y}")
        else:
            return (f"{x} es menor que {y}")
    except:
        return "Introduce dos valores numéricos"

def wordcounter(x:str, y:str):
    occurences = 0
    for i in x:
        if i.lower() == y.lower():
            occurences +=1
    return occurences

def dictcounter(x:str):

    # Convertimos todas las letras a minúscula, eliminamos signos de puntuación.
    x = x.lower().replace(",","").replace(" ","").replace(".","").replace(":","").replace(";","")

    # Definimos el diccionario de almacenaje
    dictionary = {}

    # Recorremos las letras del string
    for i in x:

        # Si la letra no se encuentra en las claves del diccionario, creamos una clave con sea 
        # letra y le damos el valor 1
        if i not in dictionary:
            dictionary[i] = 1

        # Si la letra se encuentra ya en las claves, le sumamos 1 al valor correspondiente a esa clave
        else:
            dictionary[i] += 1

    return dictionary


def eliminator(group:list, action:str, element = None):
    ''' 
    Add items into a list or remove them from it.
    action could be "add" or "remove"
    Inputs:
    group:list
    action:str
    element = None

    Outputs:
    return group:list
    '''
    if element != None:
        if action == "add":
            group.append(element)

        elif action == "remove":
            group.remove(element)

    return group

def sentencemaker(*args):
    sentence = []
    for i in args:
        sentence.append(i)

    sentence = " ".join(sentence)
    return sentence


def n_esimofibonacci(n):

    x = [0,1]

    for i in range(1, n, 1):
        y = x[i] + x[(i-1)]
        x.append(y)
    return x[-1]

def area_cuadrado(lado):
    return lado * lado

# Función de cálculo del área del triángulo

def area_triangulo(base,altura):
    return (base * altura) / 2

# Función de cálculo de área del circulo

def area_circulo(radio):
    import math
    return 2 * math.pi * radio
