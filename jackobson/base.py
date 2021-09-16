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


def uso(w, freq_w, prom_vector_uso):
    debug.debug(
        "uso(%(w)s): %(numerador)s / %(denominador)s  " % {"w": w, "numerador": freq_w, "denominador": prom_vector_uso})

    uso = freq_w / prom_vector_uso

    return uso


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


@compensacion_por_cero
def freq_w(w, freqDist):
    """
    La frecuencia de w está dada por 
    su valor en la tabla de frecuencia 
    con relación a todas las frecuencias 
    
    """
    log.info("inicia busqueda de freq_w para: '" + w +"'")
    freq = freqDist[w]
    freq_promedio = _prom_en_freqDist(freqDist)
    res = freq/freq_promedio
    
    debug.debug("freq_w(%(w)s): %(numerador)s / %(denominador)s )" %{"w": w, "numerador": freq, "denominador":freq_promedio})
    log.info("termina busqueda de freq_w para: '" + w +"'")
    return res

from statistics import mean

def _prom_en_freqDist(freqDist):

    f = []
    log.info("inicia" + _prom_en_freqDist.__name__)
    for palabra, frecuencia in freqDist.items():
        f.append(frecuencia)
    log.info("frecuancias antes de promediar: " + str(f))
    
    return mean(f)    


def freq_media(freqDist):
    f = []
    log.info("inicia calculo de freq media para corpora")
    for palabra, frecuencia in freqDist.items():
        f.append(frecuencia)
    log.info("frecuancias antes de promediar: " + str(f))

    return mean(f)



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





def indice_metaforico(cbase=None, creferencia=None):
        out.info("inicia construcción indice metafórico")
        uso_por_palabra = []
        
        for w in cbase:
            uso = _calcular_el_uso_por_palabra(w, cbase=cbase, creferencia=creferencia)
            
            uso_por_palabra.append(uso)

        
        log.info("termina construcción de inice metafrórica")
       

        debug.debug("uso_por_palabra:\n" + str(uso_por_pablabra))
        return mean(uso_por_pablabra)

def indice_metaforico(corpora):
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

def taza_metaforica(numerador,denominador):
    if denominador == 0:
        #compenso el 0
        denominador = 0.01


    return numerador/denominador

def _calcular_el_uso_por_palabra(w, cbase=None, creferencia=None):
        out.info("inicia calculo de uso para palabra: " + w)

        freq_base = FreqDist(cbase)
        freq_ref = FreqDist(creferencia)
        
        vec_s = vector_semantico(cbase)
        vec_u = vector_uso(vec_s, freq_ref)
        
        f_w = freq_w(w, freq_base )
        
        if vec_u[w] == {}:
            u_uso= 0.01
        else:
            u_uso = prom_vector_uso(vec_u[w])
        
        uso_para_palabra =  uso(w,f_w, u_uso)

        return uso