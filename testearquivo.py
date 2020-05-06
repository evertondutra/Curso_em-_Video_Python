arquivo = open('arquivo', 'w')
arquivo.write('Este texto será gravado!\n')
arquivo.write("Bóson Treinamentos\n")
arquivo.write("Criando um arquivo de texto com Python\n")
arquivo.write("Arquivo criado por Fábio dos Reis\n")
arquivo.write("É isso ai pessoal!\n")
arquivo.close()
arquivo = open('arquivo', 'r')
for linha in arquivo:
    print(linha)
    if'texto' in linha:
        print('pessoal')
        break
arquivo.close()