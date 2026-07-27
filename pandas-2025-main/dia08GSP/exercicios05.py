#%%
import pandas as pd
import os
# %%
#df = pd.read_csv("../data/homicidios.csv", sep = ";")
#%%
#Isso serve pra conseguir lista, é uma biblioteca facilitadora
file_names = os.listdir("../data/ipea/")
file_names
#%%
#fiz esse porq tava dando alguma coisa errada
#print(os.listdir("../data/ipea/")) 
#%%



#Esse split serve para dividir entre começo e final e pega a primeira parte, caso eu quisesse a 2 eu iria pegar o [1]
#%%

#Oque eu fiz la embaixo substitui toda essa pica aqui
df = pd.read_csv("../data/ipea/homicidios.csv", sep = ";")
df_geral = df.rename(columns = {"valor": "homicideos"})
df_geral = df_geral.set_index(["nome", "período"])
df_geral = df_geral.drop(["cod"], axis = 1)
df_geral.head()
#%%
df_negros = pd.read_csv("../data/ipea/homicidios-negros.csv", sep = ";")
df_negros = df_negros.rename(columns = {"valor": "homicideos.negros"})
df_negros = df_negros.set_index(["nome", "período"])
df_negros = df_negros.drop(["cod"], axis = 1)
df_negros.head()
#%%


df_negros.set_index(["nome", "período"])

#%%
pd.concat([df_geral, df_negros], axis = 1)

#%%

#Os dois primeiros blocos sao muito parecidos, 
# da pra fazermos uma função que englobe tudo
#%%

def read_file(file_name:str): 
    df = (pd.read_csv(f"../data/ipea/{file_name}.csv", sep = ";")
            .rename(columns = {"valor": file_name})
            .set_index(["nome", "período"])
            .drop(["cod"], axis = 1))
    return df

#%%
dfs = []
for i in file_names:
    file_names = i.split(".")[0]
    dfs.append(read_file(file_names))
#%%
#Toda def ali em cima serve para facilitar na hora de puxar 
    #os arquivos
df_negros = read_file("homicidios-negros")
df_negros

#%%
#de acordo com a lista que trouxemos do os.listdir nos pdemos puxar
#pelos numeros, podendo ser tanto de baixo pra cima quanto o contrario
#ISSo é literlamente uma lista de dfs, logo, listas de dfs podem ser concatenados
dfs[-5]
#%%

df_full = pd.concat(dfs,axis = 1).reset_index().sort_values(["período", "nome"])

#%%
#caso eu queira salvar a porra toda em csv

df_full.to_csv("homicideos_consolidados.csv", index = False, sep = ";")