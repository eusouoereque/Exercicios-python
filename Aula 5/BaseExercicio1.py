import csv

def ler_estoque():
    try:
        with open('estoque.csv', mode='r', encoding='utf-8') as arquivo:
            leitor_csv = csv.DictReader(arquivo, delimiter=';')
            for linha in leitor_csv:
                print(f"Produto: {linha['produto']}, Quantidade: {linha['quantidade']}, Preço Unitário: {linha['preco_unitario']}")
    except FileNotFoundError:
        print("O arquivo não existe!")


def cadastrar_produtos():
    #Usar o Try/except para verificar se a quantidade informada é um valor válido
    try:
        n = int(input("Quantos produtos deseja cadastrar? "))
        for i in range(n):
            produto = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a quantidade do produto: "))
            preco_unitario = float(input("Digite o preço unitário do produto: "))

            with open('estoque.csv', mode='a', newline='', encoding='utf-8') as arquivo:
                escritor_csv = csv.writer(arquivo, delimiter=';')
                escritor_csv.writerow([produto, quantidade, preco_unitario])
    except ValueError:
        print("Erro: Por favor, digite números válidos para quantidades.")


print("\n\n=== GERENCIADOR DE ESTOQUE ===")
print("Antes de adiconar\n")
ler_estoque()
# Chamamos a função de cadastro primeiro
cadastrar_produtos()
print("Depois de adiconar\n")
# Depois tentamos ler para mostrar o resultado atualizado
ler_estoque()