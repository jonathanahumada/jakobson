import os
import csv
from functools import reduce

def directorio_usuario():
    return os.path.dirname(os.path.abspath(__name__))

def output_csv(nom_archivo):
    return os.path.join(directorio_usuario() , f"{nom_archivo}.csv")


def guardar_csv(filename, ref_metaforica, header):

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(header)
        for fila in ref_metaforica.items():
            writer.writerow(fila)


