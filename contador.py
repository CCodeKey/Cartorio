import os
import re

verde = "\033[92m"
amarelo = "\033[93m"
vermelho = "\033[31m"
end_color = "\033[0m"

def generate_expected_filenames(nomeDLivro):
    expected_files = []
    for i in range(1, 201): 
        for j in range(1, 3):  
            expected_files.append(f"{nomeDLivro} {i}-{j}.JPG")  
    return expected_files

def find_missing_images(directory, nomeDoLivro):
    expected_files = set(generate_expected_filenames(nomeDoLivro))

    present_files = set()
    pattern = re.compile(f"{nomeDoLivro} \d+-[12]\.JPG")

    for file in os.listdir(directory):
        if pattern.match(file):
            present_files.add(file)

    missing_files = expected_files - present_files

    return missing_files
nome_do_livro = str(input("Digite o nome do Livro: "))

directory_path = "C:\\Arquivos\\arquivos_py\\Remessa renomeada" # <- caminho da pasta "Remessa renomeada"

missing_images = find_missing_images(directory_path, nome_do_livro)

if missing_images:
    print()
    print(f"{amarelo} As seguintes imagens estão faltando: {end_color}")
    for img in sorted(missing_images):
        print(f"{vermelho} {img} {end_color}")
    print()

else:
    print()
    print(f" {verde} Nenhuma imagem faltando. Todas as imagens estão presentes. {end_color}")
    print()