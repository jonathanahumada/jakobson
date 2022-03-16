#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 16:33:52 2022

@author: jaumaf
"""
import nltk
import itertools
from .utils import textoDeBrown
def recopilarMuestra():
        corpus_referencia = [
            reportaje(),
            editorial(),
            religion(),
            hobbies(),
            popular(),
            bellasArtes(),
            academia(),
            ficcion(),
            misterio(),
            cienciaFiccion(),
            aventura(),
            romance(),
            ]
        
        codigos_brown =  [ list(dictionary.keys())for dictionary in corpus_referencia]
        
        flattened = list(itertools.chain.from_iterable(codigos_brown))
        return flattened
def tablaDeReferencia():
        corpus_referencia = [
            reportaje(),
            editorial(),
            religion(),
            hobbies(),
            popular(),
            bellasArtes(),
            academia(),
            ficcion(),
            misterio(),
            cienciaFiccion(),
            aventura(),
            romance(),
            ]
        print("{0},{1},{2}".format("literal", "nombre del texto", "categoría" ))
        for diccionario in corpus_referencia:
            for fila in diccionario.items():
                print("{0},{1},{2}".format(fila[0], fila[1], obtener_categoria(fila[0])))

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

def construirCorpusDeReferencia(keys):
      
       words = [textoDeBrown(key)for key in keys]
       flattened = list(itertools.chain.from_iterable(words))
       
       return flattened

        
    
    

def reportaje():
    muestra = {"a01":"Political Reportage"
               ,"a11":"Sports Reportage", 
               "a19": "Spot News",
               "a26": "Financial Reportage",
               "a40": "People, Art & Education"}
    return muestra

def editorial():
    muestra = {"b03":"Editorials",
               "b08":"Columns", 
               "b15": "Letters to the editor",
               "b19": "The Voice of the people",
               "b24": "Reviews"
               }
    return muestra


def religion():
    muestra = {"d15":"Zen:A Rational critique",
               "d11": "War & the Cristian Conscience",
               "d13": "The New Science & The New Faith",
               "d04": "The Shape of death",
               "d02": "Christ Without Myth"
               
        }
    return muestra

    
def hobbies():
    muestra = {
        "e05": "The Younger Generation/Use of Common Sense Makes Dogs Acceptable",
        "e06": "The American Boating Scene",
        "e10": "The New Guns of 61",
        "e19": "How to Own a Pool and Like It",
        "e23": "The Watercolor Art or Roy Mason"
        }
    return muestra


def popular():
    muestra = {
        "f07": "How to Have a Successful Honeymoon/Attitudes Toward Nudity",
        "f12": "New Methods of Parapsychology",
        "f13": "Part-time Farming",
        "f14": "The Trial and Eichmann",
        "f33": "Slurs and Suburbs"}
    return muestra


def bellasArtes():
    muestra = {
        "g15":"Themes and Methods: Early Storie of Thomas Mann",
        "g13": "Sex in Contemporary Literature",
        "g18": "Verner von Heidenstam",
        "g26": "Two Modern Incest Heroes",
        "g28": "William Faulkner, Southern Novelist"
        }
    return muestra


def academia():
    muestra = {
        "j18": "Linear Algebra",
        "j17": "Prolegomena to a Theory of Emotions",
        "j28": "Perceptual Changes in Psycopathology",
        "j39": "Stock, Wheats and Pharaohs",
        "j35": "Semantic Contribution of Lexicostatistics"}
    return muestra





def ficcion():
    muestra = {
        "k18": "Midcentaury",
        "k25": "The Prophecy",
        "k04": "Worlds of Color",
        "k23": "The Tight of the Sea",
        "k17": "Mila 8"
        }
    return muestra


def misterio():
        muestra = {"l05": "Bloodstain",
                   "l11": "The Man Who Looked Death in the Eye",
                   "l04":"Encounter with Evil",
                   "l19": "Make a Killing",
                   "l20": "Death by the Numbers"}
        return muestra

    
def cienciaFiccion():
    muestra = {
        "m01": "Stranger in a Strange Land",
        "m03": "The Star Dwellers",
        "m04": "The Planet with no Nightmare",
        "m05": "The Ship who Sang",
        "m06": "A Planet Named Shayol"
        }
        
    return muestra


def aventura():
    muestra = {
        "n01": "The Killer Marshall",
        "n05": "Bitter Valley",
        "n15": "Sweeny Squadron",
        "n20": "The Flooded Deares",
        "n26": "Toughest Lawman in the Old West"}
    return muestra


def romance():
    muestra = {
        "p29": "My Hero",
        "p27": "Measure of a Man",
        "p22": "A Husband Stealer from Way Back",
        "p16": "A Secret Between Friends",
        "p12": "A Passion in Rome"
        }
    return muestra




