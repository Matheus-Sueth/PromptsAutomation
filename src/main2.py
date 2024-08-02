import pandas as pd
from genesys import api

# Ler o arquivo CSV
api_genesys = api.Genesys()
df = pd.read_excel('arquivo.xlsx')


df = df.dropna()
# Salvar o resultado em um novo arquivo CSV
nome_bot = input('Digite a sigla do bot ou digite 1 caso não precise digitar a sigla: ')
print(df)
for linha in df.index:
    if nome_bot != "1":
        palavras = df.loc[linha, "Prompt"].split("_")
        palavras.insert(-1,nome_bot)
        name_prompt = '_'.join(palavras)
    else:
        name_prompt = df.loc[linha, "Prompt"]
    print(name_prompt)
    conteudo = df.loc[linha, "PrConteudoompt"]
    api_genesys.create_new_user_prompt()
    api_genesys.create_new_user_prompt_resource()