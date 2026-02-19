# %%

import pandas as pd
# %%

df = pd.read_csv("../data/transacao_produto.csv", sep = ";")
df
# %%
#Eu tentando debugar essa tabela, porque na colunda IdProduto estava dando valores em string oque nao permitia aplicaçao de filtros. Dai converti para int, n deu, ive que apagar colunas vazias e em NaN
df["IdProduto"] = df["IdProduto"].astype(int)
df["IdProduto"] = pd.to_numeric(df["IdProduto"], errors="coerce")
df = df.dropna(subset=["IdProduto"])

# %%
##Explicaçao do gepeteco
#1Converter forçando inválidos para NaN

df["IdProduto"] = pd.to_numeric(df["IdProduto"], errors="coerce")


#2Remover linhas inválidas

df = df.dropna(subset=["IdProduto"])

#3Converter para inteiro

df["IdProduto"] = df["IdProduto"].astype(int)

# %%

filtro = (df["IdProduto"] == 5) 
filtro
# %%
#Isin funciona como um filtro, se tiver retorna com um true.
filtro = df["IdProduto"].isin([5,11])
df[filtro]
# %%

clientes = pd.read_csv("../data/clientes.csv", sep = ";")
clientes.head()
# %%
#MUITO IMPORTANTE#
#Porq esse .isna teria sido muito útil ali em cima quando eu precisei fazer a limpa, agr essa coluna está limpa e a do Téo n está
#Podia ter feito um filtro como abaixo so para pegar aqueles não nulos
clientes["DtCriacao"].isna() # ou
#clientes["DtCriacao"].isna() ou clientes["DtCriacao"].notna(). Um retorna True se for Nan e o outro retorna true se não for nan
# %%
#Se eu fizer filtro = clientes["DtCriacao"].isna() não retorna nada, por isso que eu tive q fazer o caminho inverso
filtro = clientes["DtCriacao"].notna()
clientes[filtro]

# %%
#Porém, se fizer com um ~ ele inverte a porra toda e se "torna" um notna
~clientes["DtCriacao"].notna()
# %%
