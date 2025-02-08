import os
import re

azul = "\033[91m"
end_color = "\033[0m"

def ordenar_naturalmente(texto):
    return [int(t) if t.isdigit() else t for t in re.split(r'(\d+)', texto)]

def renomear_arquivos(pasta):
    try:
        arquivos = os.listdir(pasta)
        arquivos.sort(key=ordenar_naturalmente)

        numero_folha = 1
        
        for i, arquivo in enumerate(arquivos):
            parte = (i % 2) + 1

            novo_nome = f"RI-2CF {numero_folha}-{parte}.JPG"
            
            caminho_antigo = os.path.join(pasta, arquivo)
            caminho_novo = os.path.join(pasta, novo_nome)
            os.rename(caminho_antigo, caminho_novo)
            if parte == 2:
                numero_folha += 1

    except NameError:
        print("Erro --> ", NameError )

pasta = "C:\\Arquivos\\arquivos_py\\Remessa"
print()
i = input(f"{azul}(enter){end_color} ")
print()
renomear_arquivos(pasta)