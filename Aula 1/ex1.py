tamDisco = int(input("Digite o Tamanho do disco em GB: "))
tamSistema = int(input("Digite o Tamanho do sistema operacional em GB: "))

if tamSistema > tamDisco:
    print("O sistema operacional é maior que o disco, não é possível armazenar.")
else:
    print("O espaço disponível para armazenamento é de: ", tamDisco - tamSistema, "GB")