# função para identificar o tipo de rede
def identificar_rede(ip):
    if ip.startswith("192"):    
        return "Interno"
    else:
        return "Externo"

# função para avaliar carga de CPU
def avaliar_carga(cpu):
    if int(cpu) > 80:
        return "CRÍTICO"
    else:
        return "ESTÁVEL"


# lista que armazenará os servidores
inventario = []
# set para armazenar setores únicos
setores = set()

# quantidade de servidores
n = int(input("Quantos servidores deseja cadastrar? "))

# cadastro dos servidores
for i in range(n):
    #Capturar os dados do servidor
    ip = input("Digite o endereço IP do servidor: ")
    rede = identificar_rede(ip)
    cargaCPU = int(input("Digite a carga de CPU do servidor: "))
    status = avaliar_carga(cargaCPU)
    setor = input("Digite o setor do servidor: ")
    
    #Armanezar no dicionário servidor
    servidor = {
        "ip": ip,
        "rede": rede,
        "cargaCPU": cargaCPU,
        "status": status,
        "setor": setor
    }

    #Adicinar a lista de servidores (lista de dicionários)
    inventario.append(servidor)

    #Atualizar o set dos setores que possuem servidores
    setores.add(setor)



print("\nRELATÓRIO FINAL\n")

# percorre a lista de servidores
for servidor in inventario:

    print("Servidor:")

    # percorre as chaves do dicionário
    for chave in servidor:
        print(chave, ":", servidor[chave])


print("Setores monitorados:")
#Imprimir o set com os setores
for setor in setores:
    print("-", setor)