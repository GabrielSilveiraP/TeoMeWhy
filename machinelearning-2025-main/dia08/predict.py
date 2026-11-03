#%%
import pandas as pd
import mlflow
#Importe do modelo na mão
#model_df = pd.read_pickle("../dia07/model.pkl")
# model = model_df['model']
# features = model_df['features']
#Import de dados novos ->fingindo que são dados novos e pegando 3 amotras
df = pd.read_csv("../data/abt_churn.csv")
amostra = df[df['dtRef'] == df['dtRef']. max()].sample(3)
# amostra
#predicao
# predicao = model.predict_proba(amostra[features])[:,1]
# predicao
# amostra['proba'] = predicao
# amostra
#O jeito acima é mt mais manual pra fazer essas coisas, mas tbm depende mt de código, pra fazer cagada é fácil
#%%
#Importando via mlflow
mlflow.set_tracking_uri("http://localhost:5000")
#isso aqui abaixo é para puxar a versão mais recente. E isso abaixo é um artefato
models = mlflow.search_registered_models(filter_string="name='model_churn'")
Latest_version = max ([i.version for i in models[0].latest_versions])
Latest_version

model = mlflow.sklearn.load_model(f"models:/model_churn/{Latest_version}")

features = model.feature_names_in_
features
# %%
#predicao ficou  igual
predicao = model.predict_proba(amostra[features])[:,1]
predicao
amostra['proba_new'] = predicao
amostra

# %%

# %%
