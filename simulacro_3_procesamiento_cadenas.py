def calcular_porcentaje(cantidad, total):
    porcentaje = 0
    if total > 0:
        porcentaje = (cantidad * 100) // total
    return porcentaje


def calcular_promedio(cantidad, total):
    promedio = 0
    if total > 0:
        promedio = cantidad // total
    return promedio


def es_digito(car):
    return car in '1234567890'


def es_vocal(car):
    return car in 'aeiouAEIOUáéíóúÁÉÍÓÚ'


def es_consonante(car):
    return car in 'qwrtypsdfghjklñzxcvbnmQWRTYPSDFGHJKLÑZXCVBNM'


def es_digito_par(car):
    return car in '2468'

def es_letra(car):
    return car in 'qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM'


def principal():
    #archivo = open('entrada.txt', 'rt')
    #texto = archivo.read()
    #archivo.close()

    texto = 'AC284 DE983 de us28.'
    #acumuladores:
    r1 = r2 = r3 = r4 = 0
    palabras_vocales_maslargas = cont_palabras = palabras_con_tu = 0

    #contadores:
    cont_letras = cont_vocales = cont_consonantes = 0

    #banderas:
    prim_letra = seg_letra = solo_pares = tiene_3char = tiene_tu = tiene_b = tiene_digitos = False
    tiene_otro_char = False
    mas_corta3_char = None
    anterior = ''



    for car in texto:
        if car != ' ' and car != '.':
            cont_letras += 1

            if cont_letras == 1 and es_letra(car):
                prim_letra = True
            if cont_letras == 2 and es_letra(car):
                seg_letra = True

            if cont_letras > 2 and es_digito_par(car):
                solo_pares = True
            if cont_letras > 2 and not es_digito_par(car):
                tiene_otro_char = True




            if cont_letras > 3:
                if es_letra(car) or es_digito(car):
                    tiene_3char = True

            if es_consonante(car):
                cont_consonantes += 1
            if es_vocal(car):
                cont_vocales += 1

            if car in 'Uu' and anterior in 'Tt':
                tiene_tu = True
            if car in 'Bb':
                tiene_b = True
            if es_digito(car):
                tiene_digitos = True


            anterior = car


        else:
            cont_palabras += 1

            if solo_pares and prim_letra and seg_letra and not tiene_otro_char:
                r1 += 1

            if tiene_3char:
                if mas_corta3_char is None:
                    mas_corta3_char = cont_letras
                elif mas_corta3_char > cont_letras:
                    mas_corta3_char = cont_letras

            if cont_vocales > cont_consonantes:
                palabras_vocales_maslargas += 1

            if tiene_tu and not tiene_b and not tiene_digitos:
                palabras_con_tu += 1



            cont_letras = cont_vocales = cont_consonantes = 0
            prim_letra = seg_letra = solo_pares = tiene_3char = tiene_tu = tiene_b = tiene_digitos = False
            tiene_otro_char = False









    r2 = mas_corta3_char
    r3 = calcular_porcentaje(palabras_vocales_maslargas , cont_palabras)
    r4 = palabras_con_tu

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)








if __name__ == '__main__':
    principal()