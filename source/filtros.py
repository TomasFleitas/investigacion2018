import stop_words
from stop_words import STOP_WORDS
from nltk import word_tokenize, sent_tokenize

# Dado un texto, lo reformatea, tokenizando y borrando las stopwords de cada oracion y luego volviendolas a juntar.
def reformatearTexto(texto):
    oraciones = sent_tokenize(texto)
    texto = []
    for o in oraciones:
        palabras = borrarStopwords(word_tokenize(o))
        oracion = ' '.join(palabras)
        texto.append(oracion + '.')
    return texto

# Dada una lista de tokens, borra aquellos que sean stopwords.
def borrarStopwords(listaTokens):
    palabrasResultado = []
    for token in listaTokens:
        if token not in STOP_WORDS: palabrasResultado.append(token)
    return palabrasResultado

# Dada una etiqueta, define si representa a un actor o no.
def esActor(etiqueta):
    if(etiqueta == 'nc0s000' or #Sustantivo comun singular
       etiqueta == 'nc0p000' or #Sustantivo comun plural
       etiqueta == 'dd0000'):   #Determinante demostrativo
       return True

# Dada una etiqueta, define si representa a un rol o no.
def esRol(etiqueta):
    if(etiqueta == 'vaif000' or #Verbo auxiliar, modo indicativo, tiempo futuro
       etiqueta == 'vaip000' or #Verbo auxiliar, modo indicativo, tiempo presente
       etiqueta == 'vam0000' or #Verbo auxiliar, modo imperativo
       etiqueta == 'vasp000' or #Verbo auxiliar, modo subjuntivo, tiempo presente
       etiqueta == 'vasi000' or #Verbo auxiliar, modo subjuntivo, tiempo imperfecto
       etiqueta == 'vmif000' or #Verbo principal, modo indicativo, tiempo futuro
       etiqueta == 'vmip000' or #Verbo principal, modo indicativo, tiempo presente
       etiqueta == 'vmis000' or #Verbo principal, modo indicativo, tiempo preterito perfecto
       etiqueta == 'vmm0000' or #Verbo principal, modo imperativo
       etiqueta == 'vmsp000' or #Verbo principal, modo subjuntivo, tiempo presente
       etiqueta == 'vsif000' or #Verbo semiauxiliar, modo indicativo, tiempo futuro
       etiqueta == 'vsip000' or #Verbo semiauxiliar, modo indicativo, tiempo presente
       etiqueta == 'vssf000' or #Verbo semiauxiliar, modo subjuntivo, tiempo futuro
       etiqueta == 'vssp000'):  #Verbo semiauxiliar, modo subjuntivo, tiempo presente
       return True
'''
def procesarOracion(oraciones):
    for o in oraciones:
        actores = o.getActores()
        roles = o.getRoles()


        #CON LA TUPLA ACTOR-ROL-OBJETIVO COMPARAR VER SI EXISTE TRIGRAMA
        #SI EN UNA ORACION HAY UN "ESTE-ESTOS-ÉL", COMPARAR CON N TRIGRAMAS ANTERIORES PARA ENCONTRAR A QUE ACTOR SE REFIERE
        #VER PALABRAS COMO EMPLEADO (SI SE REFIERE A UN EMPLEADO O QUE ALGUIEN HAYA EMPLEADO ALGO) o ENVIO (SI SE TRATA DE UN ENVIO O YO REALIZO UNO)
'''