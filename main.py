import os
import json
import shutil
import pandas as pd

dicionario = {
    "Name": [],
    "Type": [],
    "Description": [],
    "audio_pt-br": []
}

with open('dados.json', 'rb') as  file_json:
    dados = json.loads(file_json.read())

atual_pasta = dados.get('diretorio_atual_prompts')
lista_prompts = os.listdir(dados.get('diretorio_atual_prompts'))
ivr = "IVR-" + dados.get('projeto')
type_prompt = dados.get('tipo_prompt')
dataframe = pd.DataFrame(dicionario)
qtd_linhas_dataframe = dados.get('maximo_linhas_dataframe')
for index, prompt in enumerate(lista_prompts):
    name = prompt[0:prompt.index(".")]
    dataframe.loc[index] = ['ivr_clubesaude_' + name, type_prompt, ivr, prompt]
dataframes = [dataframe[index:index+qtd_linhas_dataframe] for index in range(0,len(lista_prompts),qtd_linhas_dataframe)]
for index, dataframe in enumerate(dataframes):
    nova_pasta = f'{ivr[4:]}_{index}'
    os.mkdir(nova_pasta)
    [shutil.copy(os.path.join(atual_pasta,prompt), os.path.join(nova_pasta,prompt)) for prompt in list(dataframe["audio_pt-br"])]
    dataframe.to_csv(f'{nova_pasta}/lista.csv', index=False, sep=',')
