import spacy
from spacy import displacy

nlp = spacy.load('es_core_news_sm')
doc = nlp('El empleado debe completar el sello para realizar el envío.')
#displacy.serve(doc, style = 'dep')
doc1 = nlp('proceso')
doc2 = nlp('enviar')
similarity = doc1.similarity(doc2)
print(doc1.text, doc2.text, similarity)