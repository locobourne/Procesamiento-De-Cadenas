def es_vocal(car):
    return car in 'aeiouáéíóúAEIOUÁÉÍÓÚ'

def es_consonante(car):
    return car in 'qwrtypsdfghjklñzxcvbnmQWRTYPSDFGHJKLÑZXCVBNM'

def es_consonante_mayus(car):
    mayusculas = 'QWRTYPSDFGHJKLÑZXCVBNM'
    if car in mayusculas:
        return True

def es_digito(car):
    return car in '1234567890'

def es_impar(car):
    impar = '13579'
    if car in impar:
        return True

def calcular_promedio(cantidad, total):
    proemdio = 0
    if total > 0:
        promedio = cantidad // total
    return promedio

def calcular_porcentaje(cantidad, total):
    porcentaje = 0
    if total > 0:
        porcentaje = (cantidad * 100) // total
    return porcentaje

def principal():

    archivo = open('entradaF.txt' , 'rt')
    texto = archivo.read()
    archivo.close()

    #texto = 'La clave 1alfaxy puede funcionar en lugar de 1beta9 en lugar de 9sigmaZ. Las cosas comienzan volverse extremadamente negras. Secos los pozos entre tantas mejoras. Se nota la esencia pese al segundo tiempo El lugar marcado como X31F57 es conocido también como X23A54 Antes de esa esperada circunstancia era imposible hg3djh jui8 3ko4 5 uj6ui Las esperas nunca acaban Didide didida dijo el cantor.'

    pal_vocal_corta = None
    anterior = ''
    #contadores:
    cont_letras = tiene_Aa = tiene_Ee = tiene_DI = digito_en_posicion = 0

    #banderas:
    solo_impar = solo_mayus = empieza_vocal = tiene_digito = False
    primer_digito = True

    #acumuladores:
    r1 = r2 = r3 = r4 = r5 = masA_que_E = cont_palabras = palabras_con_DIDI = contador_digito_p_mitad = 0

    for car in texto:
        if car != ' ' and car != '.':
            cont_letras += 1

            if es_impar(car) or es_consonante_mayus(car):
                if es_impar(car):
                    solo_impar = True

                if es_consonante_mayus(car):
                    solo_mayus = True
            else:
                solo_impar = solo_mayus = False

            if cont_letras == 1 and es_vocal(car):
                empieza_vocal = True

            if car in 'Aa':
                tiene_Aa += 1
            if car in 'Ee':
                tiene_Ee += 1

            if car in 'Ii' and anterior in 'Dd':
                tiene_DI += 1

            if es_digito(car):
                if primer_digito:
                    digito_en_posicion = cont_letras
                    tiene_digito = True
                    primer_digito = False

            anterior = car


        else:
            cont_palabras += 1

            if solo_mayus and solo_impar:
                r1 += 1

            if empieza_vocal:
                if pal_vocal_corta == None:
                    pal_vocal_corta = cont_letras
                elif pal_vocal_corta > cont_letras:
                    pal_vocal_corta = cont_letras

            if tiene_Aa > tiene_Ee:
                masA_que_E += 1

            if tiene_DI >= 2 and es_vocal(anterior):
                palabras_con_DIDI += 1

            if tiene_digito:
                if cont_letras > 1:
                    if (cont_letras / 2) >= digito_en_posicion:
                        contador_digito_p_mitad += 1

                # 1BBBTFFFF


            solo_impar = solo_mayus = tiene_digito = empieza_vocal = False
            primer_digito = True
            cont_letras = tiene_Aa = tiene_Ee = tiene_DI = digito_en_posicion = 0

    r2 = pal_vocal_corta
    r3 = calcular_porcentaje(masA_que_E, cont_palabras)
    r4 = palabras_con_DIDI
    r5 = contador_digito_p_mitad

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado: %", r3)
    print("Cuarto resultado:", r4)
    print("Quinto resultado:", r5)



if __name__ == '__main__':
    principal()
