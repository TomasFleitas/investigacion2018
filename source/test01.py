import frecuencias
from nltk import word_tokenize
from nltk.tag import StanfordPOSTagger
from nltk.corpus import stopwords
from docx import Document
#cd Documents\Repos\investigacion2018\source\


#Configuracion inicial del POSTagger de Stanford
tagger = r'C:\Users\lau_9\Documents\Repos\investigacion\stanford\stanford-postagger\models\spanish.tagger'
jar = r'C:\Users\lau_9\Documents\Repos\investigacion\stanford\stanford-postagger\stanford-postagger.jar'
etiquetador = StanfordPOSTagger(tagger,jar)


#Creo un set con stopwords y le agrego algunos signos
stop_words = set(stopwords.words('spanish'))
stop_words.update([',','.',':','-','?','¿','!','¡'])


#Abro el documento y extraigo las palabras
texto = ""  #Lista de palabras del texto, incluyendo stopwords
f = open(r'C:\Users\lau_9\Documents\Repos\investigacion\source\data\TextoEjemplo.docx', 'rb')
document = Document(f)
for i in document.paragraphs:
    texto += i.text
f.close()


#Tokenizo el texto, elimino stopwords y muestro los tokens
words = word_tokenize(texto)
palabras = []  #Lista de palabras del texto, sin incluir stopwords
for word in words:
    if word not in stop_words:
        palabras.append(word)
print("Palabras del texto TOKENIZADAS pero SIN ETIQUETAR:\n" + str(palabras) + "\n")


#Etiqueto a los tokens y muestro sus etiquetas
etiquetas = etiquetador.tag(palabras)
palabras_etiquetadas = []
for etiqueta in etiquetas:
    palabras_etiquetadas.append(etiqueta)
print("Palabras del texto TOKENIZADAS y ETIQUETADAS:\n" + str(palabras_etiquetadas) + "\n")


#Calculo de frecuencias
x = 5 #Cantidad de valores mas frecuentes a mostrar
diccionario = frecuencias.listaFrecs(palabras)
diccOrdenado = frecuencias.ordenaDicFrec(diccionario)[:x]
diccOrdenadoFrecPond = frecuencias.listaFrecsPond(palabras)[:x]
print("\nFrecuencia de las " + str(x) + " palabras mas repetidas en el texto:")
for s in diccOrdenado: print(str(s))
print("\nFrecuencia ponderada de las " + str(x) +" palabras mas repetidas en el texto:")
for s in diccOrdenadoFrecPond: print(str(s))