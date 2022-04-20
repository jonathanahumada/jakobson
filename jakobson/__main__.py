from jakobson import indice_metaforico, construir_referencia, recopilarMuestra,construirCorpusDeReferencia, textoDeBrown, indice_metonimico
from jakobson import corpus_objetivo  as objetivos
from jakobson import output
from itertools import chain

def main():
    import nltk
 
    corpus_objetivo = objetivos.c2
    objetivo = "c2"
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
    imprimirFila = lambda row: print("{0:^30},{1:^30},{2:^10}".format(row[0], row[1], row[2]))
    
    imprimirFila(["categoria,", "índice metafórico,", "w"])
    for fila in categoriasResultadosYtamanos: imprimirFila(list(chain.from_iterable(fila)))
   
    output.guardar_resultado(f"./resultados/metafora/{objetivo}.csv", categoriasResultadosYtamanos, ["categoria", "metafora", "w"])
    
    categoriasResultadosYtamanosMet = list(zip(zip(categorias,metonimia),tamanos))
    imprimirFila(["categoria,", "metonimia,", "w"])
    for fila in categoriasResultadosYtamanosMet: imprimirFila(list(chain.from_iterable(fila)))
    
    output.guardar_resultado(f"./resultados/metonimia/{objetivo}.csv", categoriasResultadosYtamanosMet, ["categoria", "metonimia", "w"])
    
    
def flatten(l):
    for el in l:
        if isinstance(el, tuple) and any(isinstance(sub, tuple) for sub in el):
            for sub in flatten(el):
                yield sub
        else:
            yield el
    
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
 