import glob

def main():
    # olhar todos os arquivos que tem .txt em um diretório
    # ter uma lista de paths + nome do arquivo + extensão
    paths = glob.glob('data/*.txt')

    # iterar sobre a lista, e para cada iterável, exibir seu conteúdo e printar na tela
    for file_path in paths:
        file = open(file_path, 'r')
        print(file.read())

main()