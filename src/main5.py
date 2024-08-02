import os

ivr = '210750'
pastas = os.listdir('./prompts')
indexs = [int(pasta.removeprefix(ivr + '_')) for pasta in pastas if pasta.startswith(ivr)]
ultimo_index = max(indexs) + 1 if len(indexs) != 0 else 0
print(ultimo_index)