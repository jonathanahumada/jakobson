from jakobson import indice_metaforico, construir_referencia, recopilarMuestra,construirCorpusDeReferencia, textoDeBrown, indice_metonimico
from itertools import chain
def main():
    import nltk
 
    corpus_objetivo = {
        "a40": "People. Art & Education",
        "b27": "Letters to the Editor",
        "c17": "Reviews",
        "d09": "Organizing the Local Church",
        "e36": "Renting a Car in Europe",
        "f48": "Christian Ethics & the Sit-In",
        "g75": "A Wreath for Garibaldi",
        "h30": "Annual Report of Year Ending June 30, 1961",
        "j80": "Principles of Inertial Navigation",
        "k29": "The Sheep's in the Meadow",
        "l24": "The Murders",
        "m02": "The Lovers",
        "n29":  "Riding the Dark Train Out",
        "p20": "Dirty Dig Inn"
        }
    
   
    corpus = nltk.corpus.brown.words("cj22")
    

    
    corpus_referencia = construirCorpusDeReferencia(recopilarMuestra())
    nombres = corpus_objetivo.keys()
    categorias = [obtener_categoria(nombre) for nombre in nombres]
    tamanos = [[(len(textoDeBrown(c)))] for c in corpus_objetivo]
    resultados = []
    metonimia = []
    for c in corpus_objetivo.keys():
        corpus = textoDeBrown(c)
        resultados.append(indice_metaforico(corpus,corpus_referencia,nom_recurso=corpus_objetivo[c]))
    
        metonimia.append(indice_metonimico(list(chain(corpus)), corpus_objetivo[c]))
        
        

    categoriasResultadosYtamanos = list(zip(zip(categorias,resultados),tamanos))
    imprimirFila = lambda row: print("{0:^30}{1:^30}{2:^10}".format(row[0], row[1], row[2]))
    
    imprimirFila(["categoria", "índice metafórico", "w"])
    for fila in categoriasResultadosYtamanos: imprimirFila(list(chain.from_iterable(fila)))
    
    categoriasResultadosYtamanosMet = list(zip(zip(categorias,metonimia),tamanos))
    imprimirFila(["categoria", "índice metonimico", "w"])
    for fila in categoriasResultadosYtamanosMet: imprimirFila(list(chain.from_iterable(fila)))
    
    
                                                           
    #print( [list(chain.from_iterable(tp)) for tp in categoriasResultadosYtamanos])

def obtener_categoria(nombre):
    CATEGORIAS = {
        "a": "reportage",
        "b": "editorial",
        "c": "reviews",
        "d": "religion",
        "e": "skills & hobbies",
        "f": "popular lore",
        "g": "belles lettres",
        "h": "miscellaneous",
        "j": "learned",
        "k": "general fiction",
        "l": "mistery and detective fiction",
        "m": "science fiction",
        "n": "adventure and western fiction",
        "p": "romance and love story",
        "r": "humor"
        
        }
    literal = nombre[0]
    return CATEGORIAS[literal]

if __name__ == "__main__":
    # execute only if run as a script
    main()
 