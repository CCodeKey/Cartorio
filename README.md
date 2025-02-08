
# Altomação de Processos
Esses scripts foram desenvolvidos com o objetivo de altomatizar o processo validação, organização, renomeio e integridade de dados de arquivos de um Cartório de Registro de Imóveis.
## Autores 
- [@CodeKey](https://www.github.com/ccodekey)
- [@Hellenilda](https://www.github.com/hellenilda)
## Estrutura do Projeto

```bash
├── contador.py            # Verifica se todos os 400 arquivos estão presentes e validos na pasta
├── converter_1.py         # Captura todos o arquivos ´peg e converte para JPG
├── converter_2.py         # Captura todos os arquivos JPG e converte para TIFF
├── rename.py              # Captura todos os arquivos e os renomeia em ordem crescente
└── README.md              # Documentação do projeto 
```

## Como executar

- Criar o `virtualenv`
  ```bash
  python -m venv venv
  ```
- Ativar o `virtualenv`
  - Windows
     ```bash
      .\venv/Scripts/Activate.ps1
      ```
  - Linux
    ```bash
    source venv/Scripts/bin/activate
    ```
- Instalar o Selenium com `pip`
  ```bash
  pip install pillow
  ```
## Stack utilizada
- Python
- Pillow
- os
- re