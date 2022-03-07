import nltk 
def construir_referencia(lista_corpora):
       corpora_referencia = []
       for corpus in lista_corpora:
            for w in corpus:
                corpora_referencia.append(w)
       return corpora_referencia


def textoDeBrown(cod):
    return nltk.corpus.brown.words("c" + cod)

