import frecuencias, filtros, spacy
from frecuencias import *
from filtros import *
from nltk import word_tokenize, sent_tokenize, bigrams, trigrams
from nltk.tag import StanfordPOSTagger
from docx import Document
#cd Documents\Repos\investigacion\source\


#Configuracion inicial del POSTagger de Stanford (verificar que la ruta sea la correcta, sino no funciona)
tagger = r'C:\Users\lau_9\Documents\Repos\investigacion\stanford\stanford-postagger\models\spanish.tagger'
jar = r'C:\Users\lau_9\Documents\Repos\investigacion\stanford\stanford-postagger\stanford-postagger.jar'
etiquetador = StanfordPOSTagger(tagger,jar)


#Abro el documento y extraigo las palabras
texto = ""  #Lista de palabras del texto, incluyendo stopwords
f = open(r'C:\Users\lau_9\Documents\Repos\investigacion\source\data\TextoEjemplo.docx', 'rb')
document = Document(f)
for i in document.paragraphs:
    texto += i.text#.lower()
f.close()


#Tokenizo y reformateo el texto, eliminando stopwords
#texto_ref = ' '.join(reformatearTexto(texto))
#palabras_ref = borrarStopwords(word_tokenize(texto_ref))
#print("TEXTO REFORMATEADO:\n" + texto.upper() + "\n")
#print("PALABRAS TOKENIZADAS Y SIN ETIQUETAR:\n" + str(palabras).upper() + "\n")


#Etiqueto a los tokens y muestro sus etiquetas
#palabras_etiquetadas = etiquetador.tag(palabras)
#print("Palabras del texto TOKENIZADAS y ETIQUETADAS:\n" + str(palabras_etiquetadas) + "\n")


#Muestro algunas frecuencias
#verFrecuencias(5,palabras)

nlp = spacy.load('es_core_news_sm')
texto = nlp(texto)
smf = sujetosMasFrecuentes(listarSujetos(texto))
oraciones = texto.sents

for s in oraciones:
    print('\nOracion: ' + str(s))
    #for token in s:
        #print(token.text, token.pos_, token.dep_)
    sujetos_candidatos = sujetosCandidatos(getSujeto(s),smf)
    roles_objetos = getRolObjeto(s)
    sujeto_adjetivos = getSujetoAdjetivo(s,sujetos_candidatos)
   # print('Posibles actores: ' + str(sujetos_candidatos))
    print('Posibles roles y objetos asociados: ' + str(roles_objetos))
    print('Posibles actores y sus adjetivos: ' + str(list(sujeto_adjetivos)))
    print('Requerimientos:')
    reqs = generarRequerimientos(sujeto_adjetivos,roles_objetos)
    reqs = filtrarRequerimientos(reqs)
    for r in reqs:
        print(str(r[0]) + ' -> ',primeraMayuscula(str(r[1])),primeraMayuscula(str(r[2])))

'''
oraciones = sent_tokenize(texto)
i = 0

for o in oraciones:
    i = i + 1
    tags_oracion = etiquetador.tag(word_tokenize(o))
    print('ORACIÓN N°' + str(i) + ': ' + str(o) + '\n============')
    print('Bigramas: ' + str(getBigramas(o)))
    print('Trigramas: ' + str(getTrigramas(o)))
    print('Actores: ' + str(getActores(tags_oracion)))
    print('Infinitivos:' + str(getInfinitivos(tags_oracion)))
    print('Roles: ' + str(getRoles(tags_oracion)) + '\n')
    for inf in getInfinitivos(tags_oracion):
        print('TrisCon: ' + str(getTrigramasConsecutivos(o,inf)))
'''