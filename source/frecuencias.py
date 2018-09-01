# Dada una lista de palabras, devuelve un diccionario de pares de palabra-frecuencia.
def listaFrecs(listaPalabras):
    frecuenciaPalab = [listaPalabras.count(p) for p in listaPalabras]
    return dict(list(zip(listaPalabras,frecuenciaPalab)))


# Ordena un diccionario de pares palabra-frecuencia en orden de frecuencia descendente.
def ordenaDicFrec(dicfrec):
    aux = [(dicfrec[key], key) for key in dicfrec]
    aux.sort()
    aux.reverse()
    return aux

# Obtiene la frecuencia del elemento mas repetido en un diccionario. No contempla que haya mas de un elemento maximo repetido.
# CONTROLAR LO ANTERIOR
def getFrecMaxima(dix):
    frecs = []
    for k,v in dix.items():
        frecs.append(v)
    return max(frecs)

# Dada una lista de palabras, devuelve un diccionario de pares palabra-frecuencia ponderada.
def listaFrecsPond(listaPalabras):
    #Obtengo la frecuencia maxima de la lista argumento.
    frecMax = getFrecMaxima(listaFrecs(listaPalabras))
    #Calculo la frecuencia ponderada para cada elemento de la lista argumento.
    frecuenciaPalab = [listaPalabras.count(p) for p in listaPalabras]
    frecsPro = list(map(lambda x: round(x/frecMax,3), frecuenciaPalab))
    #Creo el diccionario resultante.
    return ordenaDicFrec(dict(list(zip(listaPalabras,frecsPro))))
            