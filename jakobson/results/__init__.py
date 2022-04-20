
import pandas as pd

#para mostrar dos cifras decimales y separador de miles
pd.options.display.float_format = '{:,.2f}'.format

def leer_muestra(sample_number,folder_prefix):
    metafora = pd.read_csv(f"{folder_prefix}/metafora/{sample_number}.csv")
    metonimia = pd.read_csv(f"{folder_prefix}/metonimia/{sample_number}.csv")
    merge =  pd.merge(metafora, metonimia, how='inner')
    #reorganizo las columnas
  
    return   merge[['categoria', 'metafora', 'metonimia','w']]

