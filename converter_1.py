import os, re

path = 'C:\\Arquivos\\arquivos_py\\continuacao'

def removendoNumeros():
    # Percorrer todos os arquivos na pasta
    for nome_arquivo in os.listdir(path):
        # Verifica se o arquivo tem a extensão .jpg
        if nome_arquivo.endswith('.JPG'):
            # Remover números no final do nome do arquivo (antes da extensão .jpg)
            novo_nome = re.sub(r' \d+\.JPG$', '.JPG', nome_arquivo)
            # Renomear o arquivo
            os.rename(os.path.join(path, nome_arquivo), os.path.join(path, novo_nome))

    print("Números finais removidos com sucesso!")

def convertendoParaJPG():
    def extrair_numeros(nome):
        return [int(num) for num in re.findall(r'\d+', nome)]

    # Obter uma lista de todos os arquivos .jpeg na pasta e ordená-los pelos números no nome
    arquivos = sorted([f for f in os.listdir(path) if f.endswith('.jpeg')], key=extrair_numeros)

    # Percorrer a lista e renomear
    for nome_arquivo in arquivos:
        # Cria o novo nome do arquivo com a extensão .jpg
        novo_nome = nome_arquivo.replace('.jpeg', '.JPG')
        # Renomeia o arquivo
        os.rename(os.path.join(path, nome_arquivo), os.path.join(path, novo_nome))
    print("Arquivos renomeados com sucesso!")

input("(enter) ")
print()
convertendoParaJPG()
removendoNumeros()
print()
print("Processo finalizado!")
print()