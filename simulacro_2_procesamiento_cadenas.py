__name__ = '__name__'
r1 = r2 = r3 = r4 = 0
archivo = open('entrada.txt', 'rt')
texto = archivo.read()
archivo.close

def pal_pares_iguales(palabra):
    cont_consonantes = 0
    cont_vocales = 0
    es_verdad = 0
    vocales = 'AEIOUaeiouÁÉÍÓÚáéíóú'
    consonantes = 'qwrtypsdfghjklñzxcvbnmQWRTYPSDFGHJKLÑZXCVBNM'

    for char in palabra:
        if char in vocales:
            cont_vocales += 1
        if char in consonantes:
            cont_consonantes += 1
    if cont_consonantes == cont_vocales:
        es_verdad = 1
    return es_verdad

#def pal_digito_no_p:

# def principal(texto):
palabra = ''
r1 = 0
for letra in texto:
    if letra != ' ' or letra != '.':
        palabra += letra
    if letra == ' ' or letra == '.':
        print(palabra)
        r1 += pal_pares_iguales(palabra)
        palabra = ''




#print(texto)
print("Primer resultado:", r1)
print("Segundo resultado:", r2)
print("Tercer resultado:", r3)
print("Cuarto resultado:", r4)
