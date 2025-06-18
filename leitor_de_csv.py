# %%
# Ler um arquivo csv, identificar seu cabeçalho e mostrar os dados de forma coerente
file = "data.csv"

with open(file) as open_file:
    lines: str = open_file.readlines()

# %%
data_dict: dict = {}

# identificar o cabeçalho (primeira linha) do csv
keys: list = lines[0].strip("\n").split(";")

# para cada item em keys, criar uma chave no dict e atribuir a ela uma lista vazia
for key in keys:
    data_dict[key] = []
    print(keys)
# %%
# ler e mostrar demais linhas do arquivo csv
for line in lines[1:]:
    values: list = line.strip("\n").split(";")
    
# %%
