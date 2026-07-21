# %%
import pandas as pd
# %%

df = pd.read_csv("../data/clientes.csv", sep = ";")
df.head()
# %%
#COmo que fariamos caso quisessemos pegar o somente o ultimo pedaço da identificaçao do usuário?
idCliente = "000dc0f6-e4f2-4a42-b8cd-b586ed1c709a"

# %%
#Aqui ele ta funcionando como um dataframe ent ele aceita comandos, igual visto anteriormente [-1]
idCliente.split("-")[-1]

# %%
#Da pra fazer uam funçao do q foi feito antes p agilizar
def get_last_id(x):
    return x.split("-")[-1]

# %%
#Testando
get_last_id("0028dda2-334f-40bb-9582-475fb6719471")
# %%
#Fazendo uma coluna com somente o novo id dos clientes
id_novo = []
for c in df["idCliente"]:
    novo = get_last_id(c)
    id_novo.append(get_last_id(c))
df["NovoID"] = id_novo
df.head()
#Essa forma não é mt boa, tem outras funções que conseguem fazer isso de maneira mt mais fácil
# %%
#Esse .apply é um método de aplicar linha a linha 
df["idCliente"].apply(get_last_id)
# %%
