from nltk import word_tokenize, sent_tokenize, bigrams, trigrams
from nltk.tag import StanfordPOSTagger
from nltk.parse import CoreNLPParser
from docx import Document
#cd Documents\Repos\investigacion\source\


#Configuracion inicial del POSTagger de Stanford (verificar que la ruta sea la correcta, sino no funciona)
tagger = r'C:\Users\lau_9\Documents\Repos\investigacion\stanford\stanford-postagger\models\spanish.tagger'
parser = r'C:\Users\lau_9\Documents\Repos\investigacion\stanford\stanford-corenlp\spanishPCFG.ser.gz'
jar1 = r'C:\Users\lau_9\Documents\Repos\investigacion\stanford\stanford-postagger\stanford-postagger.jar'
jar2 = r'C:\Users\lau_9\Documents\Repos\investigacion\stanford\stanford-corenlp\stanford-corenlp-3.9.1.jar'
etiquetador = StanfordPOSTagger(tagger,jar1)
parseador = CoreNLPParser(url='http://localhost:9000')
print(list(parseador.parse('El viejo hombre se sentó solo sobre la montaña a observar el horizonte'.split())))