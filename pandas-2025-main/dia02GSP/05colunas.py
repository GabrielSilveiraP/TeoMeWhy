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

df[["IdCliente", "qtpontos"]] #data frame
df["IdCliente"] #data frame com uma coluna
# %%

#Pensando no SQL 
#select * from df, aq é só 
df
#select IdCliente, qtpontos from df limit 5
df[[" IdCliente", "qtpontos"]].sample(5) #-> 5 aleatórios
#df[[" IdCliente", "qtpontos"]].head(5) -> os 5 primeiros
#df[[" IdCliente", "qtpontos"]].tail(5) -> os 5 ultimos

# %%

colunas = list(df.columns)
colunas.sort()
colunas
# %%

df =df[colunas]
df

#Ajeitei as colunas da forma q eu queria e depois reatribui pro df, ou seja, em vez de mudar elas de local uma por uma ou na mao, só lancei comandas q invertessem e organizassem em ordem alfabética e depois reatribui.
# %%
