import frecuencias, filtros, spacy
from frecuencias import *
from filtros import *
from docx import Document

# Se abre el documento y se extraen las palabras
texto = ""
f = open(r'C:\Users\lau_9\Documents\Repos\investigacion\source\data\TextoEjemplo.docx', 'rb')
document = Document(f)
for i in document.paragraphs:
    texto += i.text
f.close()

# Se carga el modulo de spaCy y se procesa el texto. Se obtienen los sujetos más frecuentes y se divide al texto en oraciones
nlp = spacy.load('es_core_news_sm')
texto = nlp(texto)
smf = sujetosMasFrecuentes(listarSujetos(texto))
oraciones = texto.sents

# Se inicializan algunas variables auxiliares que se utilizaran posteriormente
actores_aux = []
requerimientos_aux = []
i = 0

# Se extraen los actores y los requerimientos de cada oracion
for oracion in oraciones:
    sujetos_candidatos = sujetosCandidatos(getSujeto(oracion),smf)
    roles = getRolObjeto(oracion)
    sujs = getSujetoAdjetivo(oracion,sujetos_candidatos)
    reqs = filtrarRequerimientos(generarRequerimientos(sujs,roles))
    actores_aux.append(sujs)
    requerimientos_aux.append(reqs)

# Se genera un set con todos los actores del documento
actores = set([])
for acs in actores_aux:
    for a in acs: actores.add(a)
actores = sorted(actores)

# Se genera un set con todos los requerimientos del documento
requerimientos = set([])
for reqs in requerimientos_aux:
    for r in reqs: requerimientos.add(r)

# Se imprimen los resultados
print('\nACTORES DEL DOCUMENTO:\n======================')
for a in actores: print('- ' + a)

print('\nREQUERIMIENTOS DEL DOCUMENTO:\n=============================')
for r in requerimientos: i += 1 ; print(str(i) + '. ' + str(r[0]) + ' -->',primeraMayuscula(str(r[1])),primeraMayuscula(str(r[2])))
print('\n(donde "*" indica que el actor no pudo ser determinado)')

print('\nPRECISION DEL PROGRAMA:\n=======================')
correctos = int(input('Ingrese el número de requerimientos que han sido detectados correctamente, sin incluir Falsos Positivos o Falsos Negativos: '))
precision = round((correctos * 100)/i,3)
print('\n=> Los requerimientos han sido obtenidos con un ' + str(precision) + '%' + ' de precisión.\n')

