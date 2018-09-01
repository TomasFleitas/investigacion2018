import nltk
from nltk.corpus import cess_esp as cess
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk import collocations
from nltk.stem import SnowballStemmer
from docx import Document
from nltk import UnigramTagger as ut
from nltk import BigramTagger as bt
#cd Documents\Repos\investigacion2018\source\

# Read the corpus into a list,
# each entry in the list is one sentence.
#cess_sents = cess.tagged_sents()
# Train the unigram tagger
#uni_tag = ut(cess_sents)

#Creo un set con stopwords y signos de puntuación
stop_words = set(stopwords.words('spanish'))
stop_words.add(',')
stop_words.add('.')

#Abro el documento y extraigo las palabras
text = ""
f = open(r'C:\Users\lau_9\Documents\Repos\investigacion\source\data\TextoEjemplo.docx', 'rb')
document = Document(f)
for i in document.paragraphs:
    text += i.text
f.close()

#Tokenizo el texto y elimino stopwords
words = word_tokenize(text)
new_sentence = []
for word in words:
    if word not in stop_words:
        new_sentence.append(word)

print(new_sentence)

#Lemmatizacion:
#Creo un diccionario desde el lemmatizador
lemmaDict = {}
with open(r'C:\Users\lau_9\Documents\Repos\investigacion\source\data\lemmatization-es.txt', 'rb') as f:
   data = f.read().decode('utf8').replace(u'\r', u'').split(u'\n')
   data = [a.split(u'\t') for a in data]
   
for a in data:
   if len(a) >1:
      lemmaDict[a[1]] = a[0]

for v in set(lemmaDict.values()):
    lemmaDict[v] = v
   
def lemmatize(word):
   return lemmaDict.get(word, word + u'*')

print('LEMATIZACIÓN')
lematizadas = []
for palabra_lem in new_sentence:
    lematizadas.append(lemmatize(palabra_lem))
print(lematizadas)
#Stemmer
stemmer_spanish = SnowballStemmer('spanish')
print('STEMMIZACIÓN')
stemmatizadas = []
for palabra_lem in new_sentence:
    stemmatizadas.append(stemmer_spanish.stem(palabra_lem))
print(stemmatizadas)
