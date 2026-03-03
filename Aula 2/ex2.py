nomes = []
cargasCPU = []
setores = []

for i in range(3):
    nome = input("Digite o nome do servidor: ")
    cargaCPU = input("Digite a carga de CPU do servidor: ")
    setor = input("Digite o setor do servidor: ")

    nomes.append(nome)
    cargasCPU.append(cargaCPU)
    setores.append(setor)

    if int(cargaCPU) > 80:
        print(f"ALERTA: O servidor {nome} está em nível crítico!")

for i in range(3):
    print(f"Servidor: {nomes[i]}, Carga de CPU: {cargasCPU[i]}%, Setor: {setores[i]}")

setores = set(setores)
print("Setores dos servidores registrados:")
for setor in setores:
    print(setor)