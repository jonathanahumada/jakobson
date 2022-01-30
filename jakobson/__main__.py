from jakobson import indice_metaforico, construir_referencia
def main():
    import nltk
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

    indice = indice_metaforico(corpus, corpus_referencia)
    print(indice)


if __name__ == "__main__":
    # execute only if run as a script
    main()
 