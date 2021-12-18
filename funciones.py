# Esta es para imprimir las potencias arriba y evitar el simbolo ^
normal = "0123456789abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ"
sup_rep = "⁰¹²³⁴⁵⁶⁷⁸⁹ᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾᴿˢᵀᵁⱽᵂˣʸᶻ"
sup_replace = str.maketrans(normal, sup_rep)


def get_data(dato):
    """Esta funcion recibe un string y los separa en el signo, letra y numero
    ejemplo:
        Entrada: -2ac
        Return: 'ac', 2, '-'
    ejemplo 2:
        Entrada: 5b
        Return 'b', 5, '+'
        
    Args:
        dato (string): un elemento del polinomio
        
    Returns:
        string: letra(s) base,
        int: cantidad de la base,
        string: signo del elemento (+, -)
    """
    try:
        #aqui intentamos ver si el dato es solo un numero y lo regresamos
        n = int(dato)
        # si se puede convertir se prosigue
        if n < 0:
            # si el numero es negativo, lo volvemos positivo
            # e indicamos que el signo es -
            s = '-'
            n = abs(n)
        else:
            # en caso de que sea positivo solo indicamos el signo
            s = '+'
        # especificamos que la letra '' ya que no tiene letra pero se devuelve tambien
        l = ''
        #regresamos los valores de la letra, numero y signo
        # y se termina la ejecucion de la funcion
        return l, n, s
    except:
        # en caso de que falle al convetir en numero no se hace nada
        #  y se prosigue con la ejecucion
        pass
    
    # --------  En caso de que la entrada contenga letras -------
    #definimos los datos a regresar, en este caso los ponemos vacios
    # y les asignaremos los valores despues
    letra = ''
    numero = ''
    signo = ''
    # checando es para poder obtener todas las letras que tenga la entrada
    # ejemplo si entra 3ac para poder obtener ac y no solo c
    checando = True
    # n sera la posicion que estaremos checando
    n = 1
    while checando:
        #a letra le damos las ultimas n posiciones de la entrada
        letra = dato[-n:]
        # y a numero el resto
        numero = dato[:-n]
        # en casi de que numero no tenga nada, ejemplo de caso
        # cuando la entrada es b
        # entonces le asignamos el valor de 1 ya que 1b = b
        if numero == '':
            numero = '1'
        """y en caso que solo que sede con el signo -
        ejemplo de entrada -b
        le asignamos -1 ya que -b = -1"""
        if numero == '-':
            numero = '-1'
        try:
            """intentamos convertir numero en un numero, si se puede
            rompemos el ciclo, en casi que no se pueda aumentamos la cantidad
            ejemplo:
            si la entrada es 2ac y tomamos solo una letra quedaria
            letra: c
            numero: 2a
            
            al intentar convertir 2a en un numero fallaria y se aumentaria la toma de letras
            asi en la siguiente quedaria
            letra: ac
            numero: 2
            al intentar convertir en numero ya se podria conventir en 2 a numero
            y el bucle se rompera
            """
            numero = int(numero)
            checando = False
            # lo mismo explicado arriba para asignarle el valor al signo
            if numero < 0:
                signo = '-'
                numero = abs(numero)
            else:
                signo = '+'
        except:
            # si falla convertir a numero se aumenta el rango de toma de letras
            n += 1
    if numero == '':
        numero = 1
    # regresamos los datos
    return letra, numero, signo

def sort_letras(palabra):
    """
    acomodaremos las letras en orden alfabetico
    
    Args:
        palabra (string): una cadena de caracteres
    
    return
    
    """
    largo = len(palabra)
    # si solo es una letra se regresa tal cual
    if largo == 1:
        return palabra
    # un vector para ordenar la letras
    separado = []
    for i in range(largo):
        separado.append(palabra[i])
        # se agrega cada letra para acomodarse despues
    separado.sort() # se ordenan alfabeticamente
    return ''.join(separado) # se regresan las letras ya ordenadas

def suma_iguales(sol):
    """Esta funcion suma los componentes comunes
    ejemplo:
    si tienes un resultado como 
    4 + 2b + 6b + 2a + 5a
    regresara
    4 + 8b + 7a

    Args:
        sol ([list]): la lista con los elementos del polinomio

    Returns:
        [list]: regresa una lista con los nuevos elementos del polinomio ya simplificada
    """
    
    elementos = {} # nos ayudara a guardar las diferentes letras que tenga
    new_sol = [] # sera la nueva solucion
    for ele in sol:
        # recorremos los elementos del polinomio
        # si es lista el segundo elemento es la potencia y el primero la base
        # si es string solo esta la base
        if isinstance(ele, type("")):
            letra, numero, signo = get_data(ele) # obtenemos los datos del elemento
            letra = sort_letras(letra) # ordenamos las bases de la letra
            if letra in elementos: # si las letras estan agregadas en el diccionario
                #obtenemos la cantidad anterior y el signo
                n_ant = int(elementos[letra]['numero'])
                sig_ant = elementos[letra]['signo']
                if sig_ant == '-':
                    n_ant = -n_ant # si el signo es negativo convertimos
                    #el numero anterior a negativo
                # hacemos lo mismo con el numero actual
                if signo == '-':
                    numero = -numero
                    signo = '+'
                numero = int(numero) + n_ant
                # procedemos a hacer la suma para obtener los nuevos valores
                if numero < 0:
                    numero = abs(numero)
                    signo = '-'
                    # si el resultado es negativo, lo ponemos positivo y el signo
                    # lo ponemos negativo
                else:
                    signo = '+' # de lo contrario el signo sera positivo
                elementos[letra]['numero'] = str(numero)
                elementos[letra]['signo'] = signo
            else:
                # en caso de que la letra no este guardada en el diccionario
                # guardamos los elementos como tal
                elementos[letra] = {}
                elementos[letra]['numero'] = str(numero)
                elementos[letra]['signo'] = signo
        elif isinstance(ele, type([])):
            # en caso de que el elemento sea una lista vendra de la forma
            # [base, exponente]
            # por lo cual separamos la potencia y el elemento
            pot = ele[1]
            ele = ele[0]
            letra, numero, signo = get_data(ele)
            letra = f'{letra}{pot}' # para que la letra no se mezcle con una
            # que sea de diferente potencia agregamos la potencia al final
            # como identificador asi no se confundira
            # b y b^2
            if letra in elementos: # realizamos los mismo metodos de arriba
                n_ant = int(elementos[letra]['numero'])
                sig_ant = elementos[letra]['signo']
                if sig_ant == '-':
                    n_ant = -n_ant
                if signo == '-':
                    numero = -numero
                    signo = '+'
                numero = int(numero) + n_ant
                if numero < 0:
                    numero = abs(numero)
                    signo = '-'
                else:
                    signo = '+'
                elementos[letra]['numero'] = str(numero)
                elementos[letra]['signo'] = signo
            else:
                elementos[letra] = {}
                elementos[letra]['numero'] = str(numero)
                elementos[letra]['signo'] = signo
            elementos[letra]['potencia'] = pot # agregamos como especial la potencia

    for elemento in elementos: # ahora que ya estan los elementos unidos
        # los regresamos a una lista para tomar la forma de antes
        ele = elementos[elemento]
        dato = []
        if ele['signo'] == '+':
            ele['signo'] = ''
        if ele['numero'] == 1 or ele['numero'] == '1':
            ele['numero'] = ''
        text = f"{ele['signo']}{ele['numero']}{elemento}"
        if 'potencia' in ele: # si esta 'potencia' en los datos quitamos la potencia
            # del texto identificador
            dato.append(text[:-len(str(ele['potencia']))])
            dato.append(ele['potencia'])
            # y agregamos la base y la potencia en una lista como venia
        else:
            dato = text
            # si no viene la potencia solo pasamos el texto como tal
        new_sol.append(dato)
    return new_sol

def parse_res(res):
    """Recibe un diccionario y lo convierte a su forma de lista o string

    Args:
        res (dict): diccionario con los datos de un elemento del polinomio

    Returns:
        list/string: lista con la base y la potencia del polinomio o solo la base en string
    """
    new_res = []
    text = ''
    if res['numero'] == 1:
        res['numero'] = '' # si el numero recibido es 1 se omitira
    if res['signo'] == '+':
        res['signo'] = '' # tambien se omitira el signo si es positivo
    text += f"{res['signo']}{res['numero']}{res['letra']}"
    
    if 'potencia' in res:
        # si hay potencia en el diccionario se hara una lista de la forma
        # [base, potencia]
        new_res.append(text)
        new_res.append(res['potencia'])
    else:
        # en casi de que no, solo se regresara el string de la base
        new_res = text
    return new_res

def multiplicar_polinomios(polinomio_1, polinomio_2):
    """Multiplica 2 polinomios

    Args:
        polinomio_1 (list): lista con los elementos del polinomio a multiplicar
        polinomio_2 (list): lista con los elementos del polinomio a multiplicar

    Returns:
        list: elementos del polinomio resultante
    """
    res_pre = []
    res_temp = {}
    for elemento in polinomio_1: # recorremos los elementos del primer polinomio
        if isinstance(elemento, type("")):
            # si el elemento es string indica que no esta elevado a alguna potencia
            for elemento2 in polinomio_2:
                # recorremos los elementos del segundo polinomio
                # y los multiplicamos con el elemento del primero polinomio
                res_temp = {}
                try:
                    res = int(elemento) * int(elemento2)
                    # en caso de que ambos elementos sean numeros y no contrangan
                    # letras solo los multiplicamos
                    if res < 0:
                        res = abs(res)
                        res_temp['signo'] = '-'
                        # en caso que el resultado sea negativo lo volvemos positivo
                        # e indicamos que el signo es negativo
                    else:
                        res_temp['signo'] = '+'
                        # de lo contrario indicamos que es signo es positivo
                    res_temp['numero'] = str(res)
                    res_temp['letra'] = ''
                    # agregamos los datos de letra, numero y signo
                except:
                    # en caso de que falle quiere decir que tiene literales
                    # y obtenemos los datps de ambos elementos
                    letra1, numero1, signo1 = get_data(elemento)
                    letra2, numero2, signo2 = get_data(elemento2)
                    # aplicamos leyes de signos
                    if signo1 == signo2:
                        res_temp['signo'] = '+'
                    else:
                        res_temp['signo'] = '-'
                    # y multiplicamos los numeros para el nuevo resultado
                    res_temp['numero'] = int(numero1) * int(numero2)
                    if letra1 == letra2:
                        res_temp['letra'] = letra1
                        res_temp['potencia'] = 2
                        # en caso de que las literales sean iguales agregaremos
                        # la potencia a los datos, como no habia potencia anterior
                        # la potencia tendra que ser cuadrada
                    else:
                        res_temp['letra'] = letra1 + letra2
                        # en casi de ser diferentes solo las concatenamos
                res_pre.append(parse_res(res_temp))
                # agregamos a los resultados la respuesta ya transformada a lista o string segun corresponda
        elif isinstance(elemento, type([])):
            aux = elemento
            for elemento2 in polinomio_2:
                res_temp = {}
                res_temp['potencia'] = aux[1]
                elemento = aux[0]
                # Si el elemento es una lista separamos la base de la potencia
                # y realizamos el mismo procedimiento que la de arriba
                # solo haciendo cambio en las potencias
                try:
                    res = int(elemento) * int(elemento2)
                    if res < 0:
                        res = abs(res)
                        res_temp['signo'] = '-'
                    else:
                        res_temp['signo'] = '+'
                    res_temp['numero'] = str(res)
                    res_temp['letra'] = ''
                except:
                    letra1, numero1, signo1 = get_data(elemento)
                    letra2, numero2, signo2 = get_data(elemento2)
                    if signo1 == signo2:
                        res_temp['signo'] = '+'
                    else:
                        res_temp['signo'] = '-'
                    res_temp['numero'] = int(numero1) * int(numero2)
                    if letra1 == letra2:
                        res_temp['letra'] = letra1
                        res_temp['potencia'] += 1
                        # si las literales son iguales se sumara un valor mas a la potencia
                    else:
                        res_temp['letra'] = letra1 + letra2
        
                res_pre.append(parse_res(res_temp))
    return suma_iguales(res_pre) # regresamos el resultado simplificando
    # los resultados iguales

def resolver(elementos, potencia):
    solucion = elementos
    if potencia == 0:
        solucion = '1'
    elif potencia < 0:
        solucion = 'Sin soporte para potencias negativas de momento'
    elif potencia > 1:
        for i in range(potencia - 1):
            solucion = multiplicar_polinomios(solucion, elementos)
    return solucion

def imprimir_ecuacion(elementos, imprimir_potencia = False, potencia = 1):
    if isinstance(elementos, type("")):
        print(elementos)
        return
    text = ("(")
    for elemento in elementos:
        if isinstance(elemento, type("")):
            if elemento[0] == '-':
                text += f"- {elemento[1:]} "
            else:
                text += f"+ {elemento} "
        elif isinstance(elemento, type([])):
            base = elemento[0]
            potencia = elemento[1]
            if base[0] == '-':
                text += f"- {base[1:]}" + str(potencia).translate(sup_replace) + " "
            else:
                text += f"+ {base}" + str(potencia).translate(sup_replace) + " "
        elif isinstance(elemento, type({})):
            try:
                signo = elemento['signo']
            except:
                signo = '+'
            try:
                numero = elemento['numero']
            except:
                numero = '1'
            try:
                letra = elemento['letra']
            except:
                letra = ''
            try:
                pot = elemento['potencia']
            except:
                pot = '1'
            text += f'{signo} '
            if numero != '1':
                text += f'{numero}'
            if letra != '':
                text += f'{letra}'
            if pot != '1':
                text += pot.translate(sup_replace)
    text = text[:-1]
    if imprimir_potencia:
        text += ")" + str(potencia).translate(sup_replace)
    else:
        text += ")"
    if text[1] == '+':
        text = '(' + text[3:]
    elif text[1] == '-':
        text = '(' + '-' + text[3:]
    print(text)

def pedir_elementos(posicion):
    ele = input(f"Ingrese el variable de la posicion {posicion} (en caso de ya no tener escriba 'fin'): ")
    if ele == 'fin':
        return False, ''
    return True, ele

def ingresar():
    posicion = 1
    elementos = []
    pidiendo = True
    while pidiendo:
        pidiendo, dato =  pedir_elementos(posicion)
        if pidiendo:
            elementos.append(dato)
        posicion += 1
    ingresando_potencias = True
    while ingresando_potencias:
        try:
            potencia = int(input("Ingrese la potencia: "))
            ingresando_potencias= False
        except ValueError:
            print("Error, ingrese un numero")

    return elementos, potencia
