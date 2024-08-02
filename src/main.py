import os
import shutil
import pandas as pd

dicionario = {
    "Name": [],
    "Type": [],
    "Description": [],
    "audio_pt-br": []
}

dados = {
    "diretorio_atual_prompts": fr"{input('Digite o diretório: ')}",
    "projeto": input('Digite o ivr apenas com números: '),
    "tipo_prompt": "user",
    "maximo_linhas_dataframe": 90
}

atual_pasta = dados.get('diretorio_atual_prompts')
lista_prompts = os.listdir(dados.get('diretorio_atual_prompts'))
ivr = "IVR-" + dados.get('projeto')
type_prompt = dados.get('tipo_prompt')
dataframe = pd.DataFrame(dicionario)
qtd_linhas_dataframe = dados.get('maximo_linhas_dataframe')
for index, prompt in enumerate(lista_prompts):
    name = prompt[0:prompt.index(".")]
    #name = f'ivr_clubesaude_{name}' if 'CS' in prompt else f'ivr_quali_{name}'
    dataframe.loc[index] = [name, type_prompt, ivr, prompt]
dataframes = [dataframe[index:index+qtd_linhas_dataframe] for index in range(0,len(lista_prompts),qtd_linhas_dataframe)]
pastas = os.listdir('./prompts')
indexs = [int(pasta.removeprefix(ivr[4:] + '_')) for pasta in pastas if pasta.startswith(ivr[4:])]
ultimo_index = max(indexs) + 1 if len(indexs) != 0 else 0
for index, dataframe in enumerate(dataframes):
    nova_pasta = f'./prompts/{ivr[4:]}_{index + ultimo_index}'
    os.mkdir(nova_pasta)
    [shutil.copy(os.path.join(atual_pasta,prompt), os.path.join(nova_pasta,prompt)) for prompt in list(dataframe["audio_pt-br"])]
    dataframe.to_csv(f'{nova_pasta}/lista.csv', index=False, sep=',')
