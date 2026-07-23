#%%
import pandas as pd

#%%
df = pd.DataFrame({
    "cliente": [1,2,3,4,5],
    "nome": ["teo", "jose", "nah", "mah", "lah"],
})

df_02 = pd.DataFrame({
    "cliente": [6,7,8],
    "nome": ["kozato", "laura", "dan"],
    "idade": [32,34,67],
})

df_02
#%%
dfs = [df, df_02]

pd.concat(dfs)
#Pode rodar e ver que agr em idade ta cheio de NAN
#%%

#Faz com que ignore a ordem, porq ali em cima ficou duplicado
pd.concat(dfs, ignore_index = True)
#%%
df_03 = pd.DataFrame({
    "idade":[67,34,90,56,88]



})
#%%
pd.concat([df, df_03], axis = 1)

#%%
df_03 = df_03.sort_values(by = "idade").reset_index(drop=True)

df_03.head()
#%%
pd.concat([df, df_03], axis = 1)

#%%
#O concat serve para empilhar valores ou colocar um do lado do outro, com o axis = 1