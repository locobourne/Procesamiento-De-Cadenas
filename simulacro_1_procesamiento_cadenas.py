def es_consonante(car):
    return car in 'qwrtypsdfghjklñzxcvbnmQWRTYPSDFGHJKLÑZXCVBNM'
    #if car in consonantes:
        #return True


def es_vocal(car):
    return car in 'aeiouAEIOUáéíóúÁÉÍÓÚ'
    #if car in vocales:
        #return True

def es_digito(car):
    return car in '1234567890'


def calcular_promedio(cantidad, total):
    promedio = 0
    if total > 0:
        promedio = cantidad // total
    return promedio

def principal():
    archivo = open('entradap.txt' , 'rt')
    texto = archivo.read()
    archivo.close()


    #texto = 'La clave 1alfaxy puede funcionar en lugar de 1beta9 o en lugar de 9sigmaZ Antes de esa esperada circunstancia era imposible Secos los pozos entre tantas mejoras La dadiva va a ser dividida dijo el pastor Hace falta coraje para saltar de ese punto Siempre aparece una clave como ax13zy o 123tz o 2tepa5w Siempre pasa que es pesado o que es salado Otra rara ocasión para esos tarados.'
    anterior = ''
    primera_letra = ''
    #contadores:
    cont_letras = 0

    #banderas:
    cons_3or5 = tiene_digito = tiene_T = tiene_TS = tiene_MA = tiene_la_p_letra = False
    primera_palabra = True
    #acumuladores:
    r1 = r2 = r3 = r4 = total_TS = cantidad_TS = 0

    for car in texto:
        if car != ' ' and car != '.':
            cont_letras += 1

            if cont_letras == 3 or cont_letras == 5:
                if es_consonante(car):
                    cons_3or5 = True

            if es_digito(car):
                tiene_digito =True

            if car in 'Tt':
                tiene_T = True

            if tiene_T and car in 'Ss':
                tiene_TS = True

            if cont_letras >= 4:
                if car in 'Aa' and anterior in 'Mm':
                    tiene_MA = True


            if primera_palabra and cont_letras == 1:
                primera_letra = car.lower() , car
                primera_palabra = False

            if car in primera_letra:
                tiene_la_p_letra = True

            anterior = car

        else:
            if cons_3or5 and es_vocal(anterior):
                r1 += 1

            if tiene_digito and cont_letras % 2 == 1:
                r2 += 1

            if tiene_TS:
                cantidad_TS += cont_letras
                total_TS += 1

            if tiene_la_p_letra and tiene_MA:
                r4 += 1

            cont_letras = 0
            cons_3or5 = tiene_digito = tiene_T = tiene_TS = tiene_MA = tiene_la_p_letra = False

    r3 = calcular_promedio(cantidad_TS, total_TS)

    print('Primer resultado:', r1)
    print('Segundo resultado:', r2)
    print('Tercer resultado:', r3)
    print('Cuarto resultado:', r4)



if __name__ == '__main__':
    principal()