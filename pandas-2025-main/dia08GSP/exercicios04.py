#%%
import pandas as pd 
# %%

#QUEM teve mais transações de streak?
#Streak é o produto
# %%

transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")
transacoes.head()

transacao_produto = pd.read_csv("../data/transacao_produto.csv", sep = ";")
transacao_produto.head()
#%%
produtos = pd.read_csv("../data/produtos.csv", sep = ";")
produtos.head()
#%%
#é importante conhecer os df, para que saiba qual coluna vai servir de ancora, podem ter nomes diferentes, mas exercem a mesma função
#%%
clientes_transacao_produto = transacoes.merge(transacao_produto, on = "IdTransacao", how = "left")

clientes_transacao_produto[["IdTransacao", "IdCliente", "IdProduto"]]

# %%
df_full = clientes_transacao_produto.merge(produtos, on = ["IdProduto"], how = "left")

df_full=   df_full[df_full["DescCategoriaProduto"] == "Presença Streak"]
# %%
df_full.groupby(by=["IdCliente"])["IdTransacao"].count().sort_values(ascending=False).head(1)
# %%
#Ttem uma maneira mais simples de escrever, porem, é mais complexa o entendimento
#%%
#Só mbotamos um filtro auqi
produtos = produtos[produtos["DescDescricaoProduto"]=="Presença de Streak"]
# %%
(transacoes.merge(
        transacao_produto,
        on = "IdTransacao",
        how = "left")
        .merge(produtos, on = ["IdProduto"], how = "right")
)