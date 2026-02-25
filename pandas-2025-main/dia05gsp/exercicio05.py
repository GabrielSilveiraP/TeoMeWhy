# %%
#ESSE EXERCICIO É PRA PUXAR A PRIMEIRA TRANSACAO DIÁRIA DO CLIENTE
import pandas as pd
# %%
transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")
transacoes.head()
# %%
#temos que ordenar pela DtCriacao em conjunto do id cliente
transacoes = transacoes.sort_values("DtCriacao")
transacoes
# %%
#pode parecer confuso, mas primeiro tem q transformar em tipo de data, para despois falar q é realemnte data, porq poderia ser só ano, só mes etc.
transacoes["data"] = pd.to_datetime(transacoes["DtCriacao"]).dt.date
transacoes
# %%
#Removemos todas aquelas que se repetiam no Id cliente, já que agr ele ficou marcado com a primeira transação de cada um
transacoes.drop_duplicates(keep = "first", subset= ["IdCliente", "data"])
# %%
# %%
#Agora pra saber a diferença entre a primeira compra e a ultima, isso pode ser por usado em locais como serviços, quanto tempo o carro fica parado no shopping
PrimeiraCompra = transacoes.drop_duplicates(keep = "first", subset= ["IdCliente", "data"])
PrimeiraCompra
# %%
#Aqui encontra a ultima compra do cliente no !!dia!!
UltimaCompra = transacoes.drop_duplicates(keep = "last", subset= ["IdCliente", "data"])
UltimaCompra
# %%



# %%
