import glob

PATH_PREFIX = 'data/'
FILE_PREFIX = '*.txt'


def main():
    # busca um preixo, e gera uma lista de todos os arquivos .txt que encontrar no diretório
    file_paths = glob.glob("".join([PATH_PREFIX, FILE_PREFIX]))

    # itera sobre cada file_path, abre o arquivo e printa seus respectivos conteúdos
    for file_path in file_paths:
        file = open(file_path, 'r')
        print(file.read())


if __name__ == "__main__":
    main()
