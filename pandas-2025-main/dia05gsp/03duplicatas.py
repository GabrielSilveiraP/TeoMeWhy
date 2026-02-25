# %%

import pandas as pd
# %%

df = pd.DataFrame({
    "nome": ["ana", "mah", "bia", "juliana", "teo", "leonardo", "mah", "mah"],
    "sobrenome": ["carvalho", "silva","carvalho", "ferreira", "almeida", "almeida","silva", "silva"],
    "salário": [1800,1990,5340,6780,6102,1040,1561,1990]

})
df
# %%
#Com isso eu retirei as ultimas duplicates, que foram as "mah silva"
df.drop_duplicates()
# %%
#Só tirei a última, agora com salários eles n reconhecem como duplicata, j's que tem uma coluna diferente
df.drop_duplicates(keep = "last")
# %%
#Dessa forma por mais que o salário seja difente ele vai apgar todas as repetições de nomes
df = df.sort_values("salário", ascending = False)
df.drop_duplicates(subset = ["nome", "sobrenome"])
# %%
#Ou se quiser reduzir as linhas da de fazer assim
df = (df.sort_values("salário", ascending = False).drop_duplicates(subset = ["nome", "sobrenome"]))
df
# %%
