from unittest import TestCase, skip
import nltk

from nltk.probability import FreqDist
from jakobson.base import *

import logging

log = logging.getLogger("tests")


class TestIndiceMetaforico(TestCase):

    def setUp(self):
        self.corpus_base = nltk.corpus.brown.words("cj22")
        self.corpus_referencia = nltk.corpus.brown.words("cj23")

    def test_matriz_semantica_retorna_un_diccionario(self):
        mat_semantica = matriz_semantica(self.corpus_base)
        self.assertEqual(type(mat_semantica), dict)

    def test_matriz_de_uso_cuenta_frecuencias(self):
        freq_base = FreqDist(self.corpus_base)
        mat_semantica = matriz_semantica(self.corpus_base)

        mat_uso = matriz_uso(mat_semantica, freq_base)

    def test_freq_media_de_corpora(self):
        freq_base = FreqDist(self.corpus_base)
        f_m = freq_media(freq_base)
        self.assertIsInstance(f_m, float)
        log.info("frecuencia media en corpora: %s" % f_m)

    def test_uso_de_una_palabra(self):
        freq_base = FreqDist(self.corpus_base)
        w = self.corpus_base[0]
        f_m = freq_media(freq_base)
        u = uso(w, freq_base, f_m)
        log.info("uso de palabra %s en corpora: %s" % (w, u))

    def test_calcular_promedio_vector_uso(self):
        freq_base = FreqDist(self.corpus_base)
        mat_semantica = matriz_semantica(self.corpus_base)
        mat_uso = matriz_uso(mat_semantica, freq_base)

        promedio = prom_vector_uso(mat_uso["affects"])
        log.info("promedio vector_de_uso: %s" % promedio)

        self.assertTrue(promedio > 0 and promedio < 1)

    def test_indice(self):
        index = indice_metaforico(self.corpus_base)
        log.info("indice metaforico en corpus: %s" % index)
