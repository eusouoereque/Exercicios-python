import csv

def leitura_csv():
    try:
        with open('monitoramento.csv', mode='r', encoding='utf-8') as arquivo:
            inventario = csv.DictReader(arquivo, delimiter=';')
            linhas = list(inventario)  # Coleta tudo aqui, dentro do with
            for linha in linhas:
                print(f"IP: {linha['ip']}, Rede: {linha['rede']}, CPU: {linha['cpu']}%, Status: {linha['status']}, Setor: {linha['setor']}")
    except FileNotFoundError:
        print("O arquivo não existe!")
        linhas = []

    return linhas  # Retorna a lista coletada

# função para identificar o tipo de rede
def identificar_rede(ip):

    if ip.startswith("192."):
        return "Interno"
    else:
        return "Externo"


# função para avaliar carga de CPU
def avaliar_carga(cpu):

    if cpu > 80:
        return "CRÍTICO"
    else:
        return "ESTÁVEL"

# lista que armazenará os servidores
inventario = []

# set para armazenar setores únicos
setores = set()

leitura_csv()

# quantidade de servidores
while True:
    try:
        n = int(input("Quantos servidores deseja cadastrar? "))
        break
    except ValueError:
        print("Erro: Por favor, digite um número válido para a quantidade de servidores.")

# cadastro dos servidores
for i in range(n):

    print(f"\nCadastro do servidor {i+1}")
    while True:
        try:
            ip = input("IP: ")
            cpu = float(input("Carga de CPU (%): "))
            setor = input("Setor: ")
            rede = identificar_rede(ip)
            status = avaliar_carga(cpu)
            break
        except ValueError:
            print("Erro: Por favor, digite valores válidos para a carga de CPU.")
        
    servidor = {
        "ip": ip,
        "rede": rede,
        "cpu": cpu,
        "status": status,
        "setor": setor
    }

    inventario.append(servidor)
    setores.add(setor)


print("\nRELATÓRIO FINAL\n")

# percorre a lista de servidores
for servidor in inventario:

    print("Servidor:")

    # percorre as chaves do dicionário
    for chave in servidor:
        print(chave, ":", servidor[chave])

    print()


print("Setores monitorados:")
print(setores)

with open('monitoramento.csv', mode='w', newline='', encoding='utf-8') as arquivo:
    escritor_csv = csv.writer(arquivo, delimiter=';')
    escritor_csv.writerow(["ip", "rede", "cpu", "status", "setor"])
    for servidor in inventario:
        escritor_csv.writerow([servidor["ip"], servidor["rede"], servidor["cpu"], servidor["status"], servidor["setor"]])

leitura_csv()