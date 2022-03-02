#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 16:33:52 2022

@author: jaumaf
"""
import nltk
from jakobson import indice_metaforico, construir_referencia
def construirCorpusDeReferencia():
      
        corpus = nltk.corpus.brown.words("cj22")

        r1 = nltk.corpus.brown.words("cj23")  # J22	Max F. Millikan & Donald L. Blackmer, editors	The Emerging Nations
        r2 = nltk.corpus.brown.words("cj24")  # J24	Howard J. Parad	Preventive Casework: Problems & Implications
        r3 = nltk.corpus.brown.words(
            "cj25")  # J25	Sister Claire M. Sawyer	Some Aspects of Fertility of a Tri-Racial Isolate
        r4 = nltk.corpus.brown.words("cj26")  # J26	Frank Lorimer	Demographic Information on Tropical Africa
        r5 = nltk.corpus.brown.words(
            "cj27")  # J28	William H. Ittelson & Samuel B. Kutash, editors	Perceptual Changes in Psychopathology
        r6 = nltk.corpus.brown.words("cj28")  # J30	Raymond J. Corsini	Roleplaying in Business & Industry

        corpus_referencia = construir_referencia([r1,r2,r3,r4,r5,r5])
        
    
    
def informativa():
    pass
def reportaje():
    muestra = {"a01":"Political Reportage"
               ,"a11":"Sports Reportage", 
               "a19": "Spot News",
               "a26": "Financial Reportage",
               "a40": "People, Art & Education"}
    pass

def editorial():
    muestra = {"b03":"Editorials",
               "b08":"Columns", 
               "b15": "Letters to the editor",
               "b19": "The Voice of the people",
               "b24": "Reviews"
               }
    pass

def religion():
    muestra = {"d15":"Zen:A Rational critique",
               "d11": "War & the Cristian Conscience",
               "d13b": "The Seeming Impossible",
               "d04": "The Shape of death",
               "d02": "Christ Without Myth"
               
        }
    pass
    
def hobbies():
    muestra = {
        "e05b": "Use of Common Sense Makes Dogs Acceptable",
        "e06": "The American Boating Scene",
        "e10": "The New Guns of 61",
        "e19": "How to Own a Pool and Like It",
        "e23": "The Watercolor Art or Roy Mason"
        }
    pass

def popular():
    muestra = {
        "fo7b":"Attitudes Toward Nudity",
        "f12": "New Methods of Parapsychology",
        "f13": "Part-time Farming",
        "f14": "The Trial and Eichmann",
        "f33": "Slurs and Suburbs"}
    pass

def bellasArtes():
    muestra = {
        "g15":"	Themes and Methods: Early Storie of Thomas Mann",
        "g13": "Sex in Contemporary Literature",
        "g18": "	Verner von Heidenstam",
        "g26": "Two Modern Incest Heroes",
        "g28": "William Faulkner, Southern Novelist"
        }
    pass

def academia():
    muestra = {
        "j18": "Linear Algebra",
        "j17": "Prolegomena to a Theory of Emotions",
        "j28": "Perceptual Changes in Psycopathology",
        "j39": "Stock, Wheats and Pharaohs",
        "j35": "Semantic Contribution of Lexicostatistics"}
    pass


def imaginativa():
    pass



def ficcion():
    muestra = {
        "k18": "Midcentaury",
        "k25": "The Prophecy",
        "k04": "Worlds of Color",
        "k23": "The Tight of the Sea",
        "k17": "Mila 8"
        }
    pass

def misterio():
        muestra = {"l05": "Bloodstain",
                   "l11": "	Semantic Contribution of Lexicostatistics",
                   "l04":"Encounter with Evil",
                   "l19": "Make a Killing",
                   "l20": "Death by the Numbers"}
        pass
    
def cienciaFiccion():
    muestra = {
        "m01": "Stranger in a Strange Land",
        "m03": "The Star Dwellers",
        "m04": "The Planet with no Nightmare",
        "m05": "The Ship who Sang",
        "m06": "A Planet Named Shayol"
        }
        
    pass

def aventura():
    muestra = {
        "n01": "The Killer Marshall",
        "n05": "Bitter Valley",
        "n15": "Sweeny Squadron",
        "n20": "The Flooded Deares",
        "n26": "Toughest Lawman in the Old West"}
    pass

def romance():
    muestra = {
        "p29": "My Hero",
        "p27": "Measure of a Man",
        "p22": "A Husband Stealer from Way Back",
        "p16": "A Secret Between Friends",
        "p12": "A Passion in Rome"
        }
    pass



