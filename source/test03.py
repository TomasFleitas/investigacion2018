import nltk  
from nltk.corpus import stopwords  
from nltk import word_tokenize  
from nltk.data import load  
from nltk.stem import SnowballStemmer  
from string import punctuation        


#stopword list to use
spanish_stopwords = stopwords.words('spanish')

#spanish stemmer
stemmer = SnowballStemmer('spanish')

#punctuation to remove
non_words = list(punctuation)  
#we add spanish punctuation
print(non_words.extend(['¿', '¡']))  
print(non_words.extend(map(str,range(10))))

stemmer = SnowballStemmer('spanish')  
def stem_tokens(tokens, stemmer):  
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):  
    # remove punctuation
    text = ''.join([c for c in text if c not in non_words])
    # tokenize
    tokens =  word_tokenize(text)

    # stem
    try:
        stems = stem_tokens(tokens, stemmer)
    except Exception as e:
        print(e)
        print(text)
        stems = ['']
    return stems

texto = 'Hoy es un dia que huele a mierda. Hoy es un dia de mierda. Lo es? Sí, mierda que lo es.'
print(tokenize(texto))