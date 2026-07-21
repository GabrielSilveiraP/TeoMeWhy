#%%
import pandas as pd
import numpy as np

transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")
# %%
#amplitude, distancia da amplitude pra média e elevar ao quadrado e tirar a raiz
#sqrt((amplitude - mean)**2)

#%%
def dif_amp(x :pd.Series):
        amplitude = x.max() - x.min()
        media = x.mean()
        return np.sqrt((amplitude - media)**2)
#%%

idades = pd.Series([25, 30, 35, 40, 45, 24,25,25,67,87])
dif_amp(idades)
# %%
(transacoes.groupby(by=["IdCliente"])
                .agg({"IdTransacao" : ['count'],
                      "QtdePontos" : ["sum", "mean", dif_amp]})
 )