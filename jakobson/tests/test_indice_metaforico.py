from unittest import TestCase, skip
import nltk

from nltk.probability import FreqDist
from jackobson.base import *

import logging

log = logging.getLogger("tests")

class TestIndiceMetaforico(TestCase):

    def setUp(self):
        self.corpus_base = nltk.corpus.brown.words("cj22")
        self.corpus_referencia = nltk.corpus.brown.words("cj23")

    def test_matriz_semantica_retorna_un_diccionario(self):
        mat_semantica = matriz_semantica(self.corpus_base)
        self.assertEqual(type(mat_semantica), dict)
        breakpoint()

    def test_matriz_de_uso_cuenta_frecuencias(self):

        freq_base = FreqDist(self.corpus_base)
        mat_semantica = matriz_semantica(self.corpus_base)

        mat_uso = matriz_uso(mat_semantica, freq_base)
        breakpoint()
    def test_freq_media_de_corpora(self):
        freq_base = FreqDist(self.corpus_base)
        f_m = freq_media(freq_base)
        self.assertIsInstance(f_m, float)
        log.info("frequencia media en corpora: %s" % f_m)


    def test_uso_de_una_palabra(self):
        freq_base = FreqDist(self.corpus_base)
        w = self.corpus_base[0]
        f_m = freq_media(freq_base)
        u = uso(w,freq_base, f_m)
        log.info("uso de palabra %s en corpora: %s" % (w, u))



    @skip
    def test_calcular_promedio_vector_uso(self):

        freq_base = FreqDist(self.corpus_base)
        mat_semantica = matriz_semantica(self.corpus_base)
        mat_uso = matriz_uso(mat_semantica, freq_base)

        promedio = prom_vector_uso(mat_uso["affects"])
        log.info( "promedio vector_de_uso: %s" % promedio)

        self.assertTrue( promedio > 0 and promedio < 1)

        
    

    def test_freq_w(self):
        """obtiene valor representativo
        del uso de una palabra dentro
        de un corpora objetivo
        """

        
        freq_base = FreqDist(self.corpus_base)
        f_w = freq_w("affects", freq_base )

        log.info("freq_w: " + str(f_w) )
        
        self.assertTrue( f_w > 0 and f_w < 1)


    def test_freq_w_en_corpora_referencia(self):
        """Observo qué tan viable es buscar la
        freq_w en una palabra existente en el
        un corpus base, en el corpus de referencia.

        En este caso, ambos corpus están emparentados
        por lo que deberían tener un contenido 
        léxico similar

        """
        
        freq_ref = FreqDist(self.corpus_referencia)
        
        f_w = freq_w("affects", freq_ref )
        
        log.info("freq_w en corpus_referencia: " + str(f_w) )
        
        self.assertTrue( f_w > 0 and f_w < 1)


    def test_indice(self):
        index = indice_metaforico(self.corpus_base)
        log.info("indice metaforico en corpus: %s" % index)


    @skip
    def test_uso_en_mismo_corpora(self):
        freq_base = FreqDist(self.corpus_base)
        vec_s = vector_semantico(self.corpus_base)
        vec_u = vector_uso(vec_s, freq_base)
        
        f_w = freq_w("affects", freq_base )
        u_uso = prom_vector_uso(vec_u["affects"])
        
        uso_para_palabra =  uso("affects",f_w, u_uso )
        log.info("uso en mismo corpus:" + str(uso_para_palabra))

    @skip
    def test_uso_en_corpora_paralelos(self):
        freq_base = FreqDist(self.corpus_base)
        freq_ref = FreqDist(self.corpus_referencia)

        vec_s = vector_semantico(self.corpus_base)
        vec_u = vector_uso(vec_s, freq_ref)
        
        f_w = freq_w("affects", freq_base )
        u_uso = prom_vector_uso(vec_u["affects"])
        
        uso_para_palabra =  uso("affects",f_w, u_uso )
        log.info("uso en corpus referencia:" + str(uso_para_palabra))

    @skip
    def test_indice_metaforico(self):
        i = indice_metaforico(cbase=self.corpus_base, creferencia=self.corpus_referencia)

        log.info("indice metafórico: " + str(i))

        