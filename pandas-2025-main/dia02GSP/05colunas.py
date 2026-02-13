# %%

import pandas as pd
# %%
df = pd.read_csv("../data/transacoes.csv", sep = ";")
df
# %%

df.shape
# %%
#df.rename(columns = {"QtdePontos": "qtpontos",
#                     "DescSistemaOrigem": "SistemasOrigem"
#                     }) 
#da de fazer assim direto 
#ou

renamed_columns = {"QtdePontos": "qtpontos",
                     "DescSistemaOrigem": "SistemasOrigem"
                     }
df = df.rename(columns = renamed_columns) #ou assim, que fica até mais legivel pro leitor
# %%
#Aqui tem outra coisa, se não quiser ficar sempre reatribuindo o df -> df = df. bla bla bla
#da de fazer com ele na linha com o inplace

df.rename(columns = renamed_columns, inplace = True)

# %%
