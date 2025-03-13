def es_vocal(car):
    vocales = 'aeiouáéíóúAEIOUÁÉÍÓÚ'
    if car in vocales:
        return True


def es_consonante(car):
    consonantes = 'qwrtypsdfghjklñzxcvbnmQWRTYPSDFGHJKLÑZXCVBNM'
    if car in consonantes:
        return True

def es_digito(car):
    digitos = '1234567890'
    if car in digitos:
        return True

def calcular_promedio(cantidad, total):
    promedio = 0
    if total > 0:
        promedio = cantidad // total
    return promedio

def principal():

    #texto = 'RAX rax rax rax Hace falta coraje para saltar de ese punto Siempre aparece una clave como ax13zy o 123tz o 2tepa5w Siempre pasa que es pesado o que es salado Otra rara ocasion para esos tarados.'

    archivo = open('entrada.txt', 'rt')
    texto = archivo.read()
    archivo.close()


    anterior = ''
    tiene_Pp = tiene_dig = tiene_Ss = primeras2_vocal = tiene_RA =False
    may_pal_dig_no_Pp = None
    cont_letras = cont_vocales = cont_consonantes = cant_let_pal_Ss = silaba_RA = 0
    r1 = r2 = r3 = r4 = cant_let_pal_Ss = total_pal_Ss = 0

    for car in texto:
        if car != ' ' and car != '.':
            cont_letras += 1

            if es_consonante(car):
                cont_consonantes += 1

            if es_vocal(car):
                cont_vocales += 1

            if car == 'p' or car == 'P':
                tiene_Pp = True

            if es_digito(car):
                tiene_dig = True

            if car == 's' or car == 'S':
                tiene_Ss = True

            if cont_letras == 1 or cont_letras == 2:
                if es_vocal(car):
                    primeras2_vocal = True

            if car == 'a' or car == 'A':
                if anterior == 'r' or anterior == 'R':
                    tiene_RA = True


            anterior = car

        else:
            if cont_consonantes == cont_vocales:
                r1 += 1

            if tiene_dig and not tiene_Pp:
                if may_pal_dig_no_Pp == None:
                    may_pal_dig_no_Pp = cont_letras
                elif may_pal_dig_no_Pp < cont_letras:
                    may_pal_dig_no_Pp = cont_letras

            if cont_letras > 2 and tiene_Ss:
                cant_let_pal_Ss += cont_letras
                total_pal_Ss += 1

            if primeras2_vocal and tiene_RA:
                r4 += 1

            cont_letras = cont_vocales = cont_consonantes = silaba_RA = 0
            tiene_Pp = tiene_dig = tiene_Ss = primeras2_vocal = tiene_RA = False

    r2 = may_pal_dig_no_Pp
    r3 = calcular_promedio(cant_let_pal_Ss, total_pal_Ss)


    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()

# 3. Determinar el promedio entero de caracteres por palabra entre las palabras que tienen más de dos caracteres pero incluyen una o más veces una "s".
# Por ejemplo, en el texto "Siempre pasa que es pesado o que es salado."
# hay cuatro palabras que cumplen el criterio: "Siempre", "pasa", "pesado" y "salado" y suman 23 caracteres entre todas ellas.
# Por lo tanto, el promedio entero pedido es de 5 letras por palabra.