# %%

import pandas as pd
# %%
df_clientes = pd.read_csv("../data/clientes.csv", sep = ";")
df_clientes
# %%

df_clientes.head() #mostra os 5 primeiros
# %%
df_clientes.head(n = 10)# os 10 primeiros
# %%
df_clientes.tail() #mostra as ultimas 5 linhas
df_clientes.tail(10) #os ultimos 10
# %%

df_clientes.sample(10)# mostra 10 valores aleatórios
# %%
df_clientes.shape #shape é um atributo, retorna uma tupla-> as linhas e colunas
# %%

#Quer saber o nome das colunas?
df_clientes.columns
# %%
df_clientes.index
# %%
df_clientes.info()


# %%
df_clientes.info(memory_usage="deep")#acho q n funciona ais direito porq o outro tbm tava dando o mesmo numero
# %%
df_clientes.dtypes# serie q mostra os valores da tipagem de cada coluna
# %%
