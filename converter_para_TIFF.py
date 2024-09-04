import os
from PIL import Image

verde = "\033[92m"
amarelo = "\033[93m"
azul = "\033[34m"
end_color = "\033[0m"

def renomear_arquivos(pasta, num_inicial, num_digitos=9):
    # Obter todos os arquivos da pasta
    arquivos = sorted([f for f in os.listdir(pasta) if f.endswith('.tiff') or f.endswith('.tiff')])
    
    # Iterar pelos arquivos e renomeá-los
    for i, arquivo in enumerate(arquivos, start=num_inicial):
        # Construir o novo nome de arquivo
        numero_formatado = str(i).zfill(num_digitos)

        novo_nome = f"{numero_formatado}.tiff"
        
        # Caminho completo para o arquivo atual e o novo
        caminho_atual = os.path.join(pasta, arquivo)
        caminho_novo = os.path.join(pasta, novo_nome)
        
        # Renomear o arquivo
        os.rename(caminho_atual, caminho_novo)
        print(f"( {amarelo}{arquivo}{end_color} ) renomeado para ( {amarelo}{novo_nome}{end_color} ) - [{verde}sucesso{end_color}]")

    print(f"{verde}    Processo finalizado com sucesso!{end_color}")
    print()
    print()

def processar_imagens(input_folder, output_folder):
    # Verifica se a pasta de saída existe, se não, cria
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Varre todos os arquivos JPG na pasta de entrada
    files = sorted([f for f in os.listdir(input_folder) if f.endswith('.jpg') or f.endswith('.jpg')])

    # Dicionário para armazenar todas as imagens por base_name
    images_groups = {}

    # Organiza os arquivos em grupos baseados no nome (antes do sufixo '-x')
    for file in files:
        base_name = file.rsplit('-', 1)[0]  # Exemplo: "RI 4"
        
        if base_name not in images_groups:
            images_groups[base_name] = []
        
        images_groups[base_name].append(file)

    # Processa os grupos e converte para TIFF
    for base_name, images in images_groups.items():
        images_sorted = sorted(images, key=lambda x: int(x.rsplit('-', 1)[1].split('.')[0]))  # Ordena por sufixo (1, 2, 3, ...)

        # Abre todas as imagens do grupo
        images_opened = [Image.open(os.path.join(input_folder, img)) for img in images_sorted]
        
        # Calcula a largura máxima e soma a altura de todas as imagens
        width = max(img.width for img in images_opened)
        total_height = sum(img.height for img in images_opened)

        # Cria uma nova imagem para concatenar todas verticalmente
        combined_image = Image.new('RGB', (width, total_height))

        # Cola todas as imagens na imagem combinada
        y_offset = 0
        for img in images_opened:
            combined_image.paste(img, (0, y_offset))
            y_offset += img.height

        # Salva o arquivo TIFF
        output_file = os.path.join(output_folder, f"{base_name}.tiff")
        combined_image.save(output_file)

        print(f"   criando arquivo ({amarelo} {base_name}.tiff {end_color}) - [{verde}sucesso{end_color}]")

    print(f"{verde}    Etapa 1 concluída com sucesso!{end_color}")


# Função principal para renomear e processar as imagens
def renomear_e_processar(input_folder, output_folder, num_inicial, num_digitos):
    print()
    print()
    print(f"{azul} TRANSFORMANDO EM TIFF{end_color}")
    print()
    processar_imagens(input_folder, output_folder,)
    print()
    print()
    print(f"{azul} RENOMEANDO OS ARQUIVOS{end_color}")
    print()
    renomear_arquivos(output_folder, num_inicial, num_digitos)


# Exemplo de uso:
input_folder = "C:\\Arquivos\\arquivos_py\\xx"
output_folder = "C:\\Arquivos\\arquivos_py\\yy"
num_digitos = 9  # Número de dígitos no nome do arquivo (ex: 000000034)
num_inicial = int(input("Digite o número TIFF> ")) # Número inicial da sequência

# Renomeia e processa as imagens
renomear_e_processar(input_folder, output_folder, num_inicial, num_digitos)
