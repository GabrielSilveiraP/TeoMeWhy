#%%
import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")
transacoes.head(10)
#%%
clientes = pd.read_csv("../data/clientes.csv", sep = ";")
clientes.head()
#%%
#renamed_columns = {"QtdePontos": "qtpontos",
#                     "DescSistemaOrigem": "SistemasOrigem"
#                     }
#df = df.rename(columns = renamed_columns)
# %%
colunas_renomeadas= {"IdCliente": "idCliente"}
transacoes= transacoes.rename (columns= colunas_renomeadas)
# %%
transacoes.merge(right=clientes, how = "left", on = ["idCliente"])
#Por mais que o meu how seja "left" o default é inner, que só vai voltar na tabela do merged aquilo que tem nas duas tabelas em comum
# De um lado tem 1,3,5,6,7,10
#Do outro 1,2,3,4,5,6,7,10 -> nesse somente voltariam: 1,3,5,6,7 e 10
#O left faz com que a verdade seja na esquerda, apagando somente os dados que não tiveram match com a da esq. Se na base da esq tenho 1 ao 5 e na direita 1 ao 6 o 6 será cortado
#Existe tbm o how = "right"
# %%
#Tem como fazer dessa forma aqui, que mostra da onde veio a coluna (as repetidas), se veio de transacoes ou clientes (os df que tamo usando aqui)
transacoes.merge(right=clientes, how = "left", on = ["idCliente"], suffixes = ["Transacaoes","clientes"])

#%%
#Vai ser util para não precisa ter que renomear a coluna igual eu fiz
#Pode ser que tenha mais chaves tbm, dai da pra fazer dessa forma
df_1 = pd.DataFrame({
    "transacao": [1, 2, 3, 4, 5],
    "idCliente": [1, 2, 3, 2, 2],
    "valor": [10, 45, 32, 17, 87],
})

df_2 = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "nome": ["teo", "nah", "mah", "jose"],
})

df_1.merge(df_2, lefone_on=["idCliente"], right_on=["id"], how = "left")