# %%

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")
transacoes.head()

#%%
transacoes.groupby(by=["IdCliente"]).count()
#%%
transacoes.groupby(by=["IdCliente"])["IdTransacao"].count()
#Os numeros que aparecem são a qtd de transações que cada cliente fez
# %%
#fazendo a soma de pontos de cada cabra.  qtd de transacao total de pontos e pontos/ transacao

summary = (transacoes.groupby(by=["IdCliente"], as_index = False) 
                .agg({"IdTransacao" : ["count"],
                      "QtdePontos" : ["sum", "mean"]}))
summary

#%%
summary[("QtdePontos","mean")]
