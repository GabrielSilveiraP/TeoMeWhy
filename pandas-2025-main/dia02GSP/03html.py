# %%

import pandas as pd
import requests
# %%
url = "https://www.w3schools.com/html/tryit.asp?filename=tryhtml_table_intro"
dfs = pd.read_html(url)
dfs
# len(dfs)
# %%


df_uf = dfs[0]
df_uf
# %%
df_uf.to_csv("ufs.csv", sep = ";", index = False)
# %%
