import os
import shutil
from openpyxl import Workbook
from genesys.api import Genesys



def upload_user_prompts(api_genesys: Genesys, diretorio: str, ivr: str, type_prompt: str, qtd_linhas_dataframe: int, prefixo_prompt: str = '', sufixo_prompt: str = ''):
    lista_prompts = os.listdir(diretorio)
    lista_prompts_divididos: list[range] = [lista_prompts[l:l+qtd_linhas_dataframe] for l in range(0, len(lista_prompts), qtd_linhas_dataframe)]

    for range_prompt in lista_prompts_divididos:
        pasta_principal = ivr[4:] if 'IVR-' in ivr else ivr
        pasta_secundaria = f'{pasta_principal}/{range_prompt.stop}/'
        os.mkdir(pasta_secundaria)
        wb = Workbook()
        ws = wb.active
        ws.append(['Nome', 'Tipo', 'IVR', 'Prompt', 'Sucesso', 'Message'])

        for prompt in range_prompt:
            shutil.copy(os.path.join(diretorio,prompt), os.path.join(pasta_secundaria,prompt))
            prompt_name = prefixo_prompt + prompt[0:prompt.index(".")] + sufixo_prompt
            user_prompt = api_genesys.create_new_user_prompt(prompt, ivr)
            user_prompt_resource = api_genesys.create_new_user_prompt_resource(user_prompt['id'], 'pt-br')
            ws.append([prompt_name, type_prompt, ivr, prompt])


        wb.save(f'{pasta_secundaria}/dados.xlsx')
