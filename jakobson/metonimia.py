#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 20:24:03 2022

@author: jaumaf
"""
from . import output
from nltk.util import ngrams

sentence = 'The purpose of our life is to happy'

def bigramas(mensaje):
    
    bigrams = ngrams(mensaje, 2)
    return list(bigrams)


def metonimia(tupla):
    
    n1 = set(tupla[0])
    n2 = set(tupla[1])
    total_letras = n1.union(n2)
    letras_iguales = n1.intersection(n2)
    
    return len(letras_iguales)/len(total_letras)



def indice_metonimico(corpora, nom):
    referencia_metonimica = {}
  
    tuplas = bigramas(corpora)
    indice = 0
    
    for tupla in tuplas: 
        met = metonimia(tupla)
        
        referencia_metonimica[tupla] = met
        indice += met
        
    output.guardar_csv( output.output_csv("referencia_metonimica_"+nom ), referencia_metonimica, ('w','taza'), recurso=nom)
    
    return indice