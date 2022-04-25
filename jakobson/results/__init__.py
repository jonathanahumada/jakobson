
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

import matplotlib.pyplot as pyplot
import seaborn as sns

#para mostrar dos cifras decimales y separador de miles
pd.options.display.float_format = '{:,.2f}'.format
NON_FICCION = ['reportage','editorial', 'reviews','religion','skills & hobbies', 'popular lore','belles lettres', 'learned']
UNCLASSIFIED = ['miscellaneous']

asignar_metacategoria = lambda dato: 'non-fiction' if dato in NON_FICCION else 'neither' if dato in UNCLASSIFIED else 'fiction'
def leer_muestra(sample_number,folder_prefix):
    df = None
    scaler = MinMaxScaler()
    metafora = pd.read_csv(f"{folder_prefix}/metafora/{sample_number}.csv")
    metonimia = pd.read_csv(f"{folder_prefix}/metonimia/{sample_number}.csv")
    df =  pd.merge(metafora, metonimia, how='inner')
    #reorganizo las columnas
    df = df[['categoria', 'metafora', 'metonimia','w']]
    df["metacategoria"] = [asignar_metacategoria(dato) for dato in df['categoria']]

    df[['metafora_n', 'metonimia_n']] = scaler.fit_transform(df[['metafora','metonimia']])
    df.to_csv(f'{folder_prefix}/{sample_number}.csv' ,index=False)
    
    graficar_muestra(df,sample_number,folder_prefix)
    graficar_meta_grupos(df,sample_number,folder_prefix)

    return   df

def set_style():
    sns.set_theme()
    sns.set(rc={"figure.figsize":(15, 12)})
    pyplot.xticks(rotation=45)
    
def graficar_muestra(df,sample_number, folder_prefix):
    graficar_metafora(df,sample_number, folder_prefix)
    graficar_metonimia(df,sample_number, folder_prefix)

def graficar_metafora(df,sample_number, folder_prefix):
    set_style()
    metafora = sns.barplot(x="categoria", y="metafora_n", data=df,  palette="ch:r=-.2,d=.3_r")
    metafora.get_figure().savefig(f"{folder_prefix}/graphs/{sample_number}_metafora.png")
    pyplot.clf()

def graficar_metonimia(df,sample_number, folder_prefix):
    set_style()
    metonimia = sns.barplot(x="categoria", y="metonimia_n", data=df,  palette="ch:r=-.2,d=.3_r")
    metonimia.get_figure().savefig(f"{folder_prefix}/graphs/{sample_number}_metonimia.png")
    pyplot.clf()
    
def graficar_meta_grupos(df, sample_number, folder_prefix):

    agrupados = df.groupby('metacategoria',as_index=False)
    metacategoria = sns.barplot(x="metacategoria", y="metafora_n", data=agrupados.mean()[["metacategoria","metafora_n"]],  palette="ch:r=-.2,d=.3_r")
    metacategoria.get_figure().savefig(f"{folder_prefix}/graphs/meta/{sample_number}_metacategoria_metafora.png")
    pyplot.clf()
    metacategoria = sns.barplot(x="metacategoria", y="metonimia_n", data=agrupados.mean()[["metacategoria","metonimia_n"]],  palette="ch:r=-.2,d=.3_r")
    metacategoria.get_figure().savefig(f"{folder_prefix}/graphs/meta/{sample_number}_metacategoria_metonimia.png")
    pyplot.clf()
