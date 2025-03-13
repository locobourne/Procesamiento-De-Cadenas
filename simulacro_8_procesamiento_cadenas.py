__name__ = '__name__'


archivo = open('entrada1.txt', 'rt')
texto = archivo.read()
archivo.close()


def es_impar(car):
    numeros_impar = '13579'
    if car in numeros_impar:
        return True

def es_consonante(car):
    consonantes = 'qwrtypsdfghjklñzxcvbnmQWRTYPSDFGHJKLÑZXCVBNM'
    if car in consonantes:
        return True

def es_minuscula(car):
    minusculas = 'qwertyuiopasdfghjklñzxcvbnm'
    if car in minusculas:
        return True

def es_vocal(car):
    vocales = 'aeiouáéíóúAEIOUÁÉÍÓÚ'
    if car in vocales:
        return True

def calcular_promedio(cantidad, total):
    promedio = 0
    if total > 0:
        promedio = cantidad // total
    return promedio

r1 = r2 = r3 = r4 = cant_let = cant_vocales = cant_consonantes = letras_c_cont = palabras_c = 0
silaba_d_vocal = 0
comienza_vocal = solo_minuscula = empieza_impar = tiene_B_b = tiene_aA_o_mM = False
palabra = ''
anterior = ''
mayor_con_vocal_bB = None

for car in texto:
    if car != ' ' and car != '.':
        cant_let += 1
        palabra += car
        if cant_let == 1 and es_impar(car):
            empieza_impar = True

        if cant_let >= 2 and es_minuscula(car):
            solo_minuscula = True
        else:
            solo_minuscula = False

        if cant_let == 1 and es_vocal(car):
            comienza_vocal = True

        if car == 'b' or car == 'B':
            tiene_B_b = True

        if car == 'm' or car == 'M' or car == 'a' or car == 'A':
            tiene_aA_o_mM = True

        if es_consonante(car):
            cant_consonantes += 1

        if es_vocal(car):
            cant_vocales += 1
            if anterior == 'd' or anterior == 'D':
                silaba_d_vocal += 1

        anterior = car
    else:
        if empieza_impar and solo_minuscula:
            r1 += 1

        if comienza_vocal and tiene_B_b:
            if mayor_con_vocal_bB == None:
                mayor_con_vocal_bB = cant_let
            elif mayor_con_vocal_bB < cant_let:
                mayor_con_vocal_bB = cant_let

        if cant_consonantes > cant_vocales and not tiene_aA_o_mM:
            letras_c_cont += cant_let
            palabras_c += 1

        if silaba_d_vocal >= 2 and es_vocal(anterior):
            r4 +=1

        #print('---------vueltas-----------')
        #print('cantidad de letras:', cant_let)
        #print('palabra: "', palabra, '" cantidad de letras:', len(palabra))
        #print(palabra)
        palabra = ''
        cant_let = cant_vocales = cant_consonantes = silaba_d_vocal = 0
        comienza_vocal = solo_minuscula = empieza_impar = tiene_B_b = tiene_aA_o_mM = False

r2 = mayor_con_vocal_bB
r3 = calcular_promedio(letras_c_cont, palabras_c)

print('Primer resultado:', r1)
print('Segundo resultado:', r2)
print('Tercer resultado:', r3)
print('Cuarto resultado:', r4)


# Determinar el promedio entero de caracteres por palabra entre las palabras que tienen más consonantes que vocales, pero no contienen ninguna "m" ni tampoco ninguna "a".
# Por ejemplo, en el texto "Secos los pozos entre tantas mejoras."
# hay cuatro palabras que cumplen el criterio: "Secos", "los", "pozos" y "entre", y suman 18 caracteres entre todas ellas.
# Por lo tanto, el promedio entero pedido es de 4 letras por palabra.