import frecuencias, filtros
from frecuencias import listaFrecs, ordenaDicFrec, listaFrecsPond, verFrecuencias
from filtros import esActor, esRol, reformatearTexto, borrarStopwords
from nltk import word_tokenize, sent_tokenize, bigrams, trigrams
from nltk.tag import StanfordPOSTagger
from docx import Document
#cd Documents\Repos\investigacion2018\source\


#Configuracion inicial del POSTagger de Stanford (verificar que la ruta sea la correcta, sino no funciona)
tagger = r'C:\Users\lau_9\Documents\Repos\investigacion\stanford\stanford-postagger\models\spanish.tagger'
jar = r'C:\Users\lau_9\Documents\Repos\investigacion\stanford\stanford-postagger\stanford-postagger.jar'
etiquetador = StanfordPOSTagger(tagger,jar)


#Abro el documento y extraigo las palabras
texto = ""  #Lista de palabras del texto, incluyendo stopwords
f = open(r'C:\Users\lau_9\Documents\Repos\investigacion\source\data\TextoEjemplo.docx', 'rb')
document = Document(f)
for i in document.paragraphs:
    texto += i.text.lower()
f.close()


#Tokenizo y reformateo el texto, eliminando stopwords
texto = ' '.join(reformatearTexto(texto))
palabras = borrarStopwords(word_tokenize(texto))
print("TEXTO REFORMATEADO:\n" + texto.upper() + "\n")
print("PALABRAS TOKENIZADAS Y SIN ETIQUETAR:\n" + str(palabras).upper() + "\n")


#Etiqueto a los tokens y muestro sus etiquetas
etiquetas = etiquetador.tag(palabras)
palabras_etiquetadas = []
for etiqueta in etiquetas:
    palabras_etiquetadas.append(etiqueta)
print("Palabras del texto TOKENIZADAS y ETIQUETADAS:\n" + str(palabras_etiquetadas) + "\n")


#Muestro algunas frecuencias
verFrecuencias(5,palabras)

'''
#VER STANFORD PARSER!!!!!!!
oraciones = sent_tokenize(texto)
i = 0

for o in oraciones:
    i = i + 1
    print('Bigramas de la oración ' + str(i) + ':' + str(list(bigrams(word_tokenize(o)))) + '\n')
    print('Trigramas de la oración ' + str(i) + ':' + str(list(trigrams(word_tokenize(o)))) + '\n')
actores = []
roles = []
for (p,e) in palabras_etiquetadas:
    if esActor(e): actores.append(p)
    else: 
        if esRol(e): roles.append(p)

print(actores)
print(roles)
'''