# %%

import pandas as pd
# %%

df = pd.read_csv("../data/clientes.csv", sep = ";")
df

# %%
#conversor de tipos
df["qtdePontos"].astype(float)
# %%
#Joga tudo isso para datetime
pd.to_datetime(df["DtCriacao"])
# %%
#Com isso a gente substitui um valor antigo por um novo e joga na serie nova pela retribuiçao
df["DtCriacao"] = df["DtCriacao"].replace(
    {"2024-02-01 00:00:00.000": "2024-02-01 09:00:00.000"})
# %%
#Já fica mais bonito
replace = {"2024-02-01 00:00:00.000": "2024-02-01 09:00:00.000"}
df["DtCriacao"] = pd.to_datetime(df["DtCriacao"].replace(replace))
# %%

df["DtCriacao"].dt.month
# %%
