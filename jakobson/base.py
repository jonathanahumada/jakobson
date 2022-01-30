from nltk.corpus import wordnet as wn

import logging.config

from nltk.probability import FreqDist

from os import path
log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
logging.config.fileConfig(log_file_path)

from pprint import pformat



log = logging.getLogger("base")
debug = logging.getLogger("debug")
out = logging.getLogger("tests")
artefactos = logging.getLogger("artefactos")

def matriz_semantica(mensaje):
    """Cada fila de la matriz semantica
    de un mensaje es un vector semántico.

    La matriz semántica es un diccionario
    que da una noción del campo semántico
    de un mensaje


    >> matriz = jackobson.matriz_semantica(corpus)
    >> matriz
    >> {'purchased': ['purchase', 'buy'], 'suggested': ['paint_a_picture', 'suggest', 'advise', 'indicate', 'intimate', 'evoke', 'propose', 'hint'], 'But': ['but', 'simply', 'just', 'merely', 'only'],
    """

    matriz = {}
    log.info("inicia construcción de matriz semántica")
    for w in set(mensaje):
        matriz[w] = vector_semantico(w)

    log.info("termina construcción de matriz semántica")
    return matriz


def vector_semantico(w):
    """vector\ semantico(w) = \{s_1, s_2, s_3, \dots, s_j \} \\

    :param w: la palabra para la cual construir el vector semantico
    :return: list

    >> jackobson.vector_semantico("red")
    ['cherry-red', 'ruby', 'redness', 'ruddy', 'Marxist', 'blood-red', 'reddened', 'Bolshevik', 'crimson', 'bolshie', 'violent', 'red', 'Red_River', 'red_ink', 'flushed', 'red-faced', 'carmine', 'Red', 'loss', 'scarlet', 'bolshy', 'cherry', 'cerise', 'ruby-red', 'reddish']
    """

    debug.debug("Buscando sinónimos de '%(palabra)s'" % {"palabra": w})
    vector_semantico = []

    for s in wn.synsets(w):
            vector_semantico.extend(s.lemma_names())

    # elimino duplicados
    vector_semantico = list(set(vector_semantico))
    return vector_semantico



def matriz_uso(matriz_semantica, freqDist):
    """
    Cada fila de la matriz de uso está compuesta
    por un vector de uso.

    :param matriz_semantica: una matriz semantica
    :param freqDist: una tabla de frequencias de corpus
    :return: una matriz de uso

    Ej.
    >> mat_uso = jackobson.matriz_uso(matriz, fd)
    >> mat_uso
    {'purchased': [0, 0], 'suggested': [0, 0, 0, 0, 0, 0, 0, 0], 'But': [9, 0, 0, 1, 6],
    """

    matriz_uso = {}
    log.info("inicia construcción de matriz de uso")
    for w, vec_uso in matriz_semantica.items():
        matriz_uso[w] = vector_uso(vec_uso, freqDist)
    log.info("termina construccion de matriz de uso")
    return matriz_uso

def vector_uso(vector_semantico, freqDist):
    """El vector de uso da una noción de
    qué tan frecuente es el campo semántico
    de una palabra.

    La frecuencia de la palabra será contrastada
    con su vector de uso, para obtener una noción
    de

    :param vector_semantico:
    :param freqDist:
    :return:

    Ej.
    >> vector_semantico
    ['honestly', 'frankly', 'candidly', 'aboveboard']
    >> jackobson.vector_uso(vector_semantico,fd)
    [2, 0, 0, 0]
    """
    vector_uso = []
    for sin in vector_semantico:
        freq_sinonimo = freqDist[sin]
        vector_uso.append(freq_sinonimo)

        if freq_sinonimo == 0:

            debug.debug("No se encontró para '%(sin)s' frecuencia en tablacomparativa: %(freq)d" % {"sin": sin, "freq":
                freqDist[sin]})
        else:

            debug.debug("Se encontró para '%(sin)s' frecuencia en tabla comparativa: %(freq)d" % {"sin":
                                                                                                      sin,
                                                                                                  "freq": freqDist[
                                                                                                      sin]})
    return vector_uso






def freq_media(freqDist):
    """

    :param freqDist:
    :return:

    >> jackobson.freq_media(fd)
    2.73125
    """
    f = []
    log.info("inicia calculo de freq media para corpora")
    for palabra, frecuencia in freqDist.items():
        f.append(frecuencia)
    log.info("frecuencias antes de promediar: " + str(f))

    return mean(f)

    
def compensacion_por_cero(func):
    """
    Si la funcion decorada retorna cero,
    se hace una corrección para evitar
    operaciones indefinidas o propagar el 0
    """
    def wrapper(*args, **kwargs):
        debug.debug("se inicia calculo suceptible a compensacion por cero")
        res = func(*args, **kwargs)
        if res == 0:
            res = 0.01
            debug.debug("Se aplicó compensacion por cero")
        return res   
    return wrapper




from statistics import mean

def _prom_en_freqDist(freqDist):

    f = []
    log.info("inicia" + _prom_en_freqDist.__name__)
    for palabra, frecuencia in freqDist.items():
        f.append(frecuencia)
    log.info("frecuancias antes de promediar: " + str(f))
    
    return mean(f)    







def freq_sinonimos_base(vector_uso, freq_corpus_base):
    frecuencias = []
    for palabra, frecuencia in vector_uso.items():
        log.info("buscando '" + palabra + "' en tabla de frecuencua de corpus base")
        try:
            frecuencias.append(freq_corpus_base[palabra])
            log.info("se encontró frecuencia")
        except:
            # si no encuentra w en c_base, freq es 0
            frecuencias.append(0)
            log.info("no se encontró frecuencia")
    return mean(frecuencias)


def media_de_frecuencias(tabla_de_frecuencias):
    frecuencias = []
    for palabra, frecuencia in tabla_de_frecuencias.items():
        frecuencias.append(frecuencia)

    return mean(frecuencias)



def indice_metaforico(corpora):
    """

    :param corpora:
    :return:

    >> jackobson.indice_metaforico(corpus)
    32284.159329079586
    """
    # primero calculo freqMedia
    f_d = FreqDist(corpora)
    f_m = freq_media(f_d)
    # calculo la matriz de uso
    mat_semantica = matriz_semantica(corpora)
    mat_uso = matriz_uso(mat_semantica, f_d)


    valores_indice = []
    referencia_metaforica = {}
    for w, vec_uso in mat_uso.items():
        uso_ = uso(w,f_d, f_m)
        vector_de_uso = mat_uso[w]

        prom = prom_vector_uso(vector_de_uso)

        taza = taza_metaforica(numerador=uso_, denominador=prom)
        valores_indice.append(taza)
        referencia_metaforica[w] = taza


    log.info("Termina recorrido por palabra para indice metaforico")
    artefactos.info("Inicia red. metaforica")
    artefactos.info(pformat(referencia_metaforica,indent=4))
    artefactos.info("Termina ref. metafórica")
    log.info("sumando valores del indice")

    return sum(valores_indice)

def uso(w, freqDist, freqMedia):
    """
    dada una palabra w, calcula el
    el uso.

    El uso necesita tomar como
    parametros un corpora base y
    otro de refencia
    """
    freq_w = freqDist[w]

    return freq_w/freqMedia


@compensacion_por_cero
def prom_vector_uso(vector_uso):
    """Dado un vector_uso, retorna
    el promedio de las frecuencias
    """
    frecuencias = []
    log.info("inicia promedio de vector de uso")

    for frecuencia in vector_uso:
        frecuencias.append(frecuencia)

    log.info("frecuencias antes de promediar: " + str(frecuencias))
    if len(frecuencias) != 0:
        return mean(frecuencias)
    else:
        return 0.01

def taza_metaforica(numerador,denominador):
    if denominador == 0:
        #compenso el 0
        denominador = 0.01


    return numerador/denominador




