
registro_trafego = []

for i in range(5):
    modelo = input("Digite o modelo do carro: ")
    peso = input("Digite o peso em toneladas do carro: ")
    setorOrigem = input("Digite o setor de origem do carro: ")

    carro = (modelo, peso, setorOrigem)
    
    registro_trafego.append(carro)

    if int(peso) > 10:
        print(f"ALERTA: Veículo {modelo} com peso excessivo detectado!")

senha = 115211

while True:
    tentativa = int(input("Digite a senha para acessar o sistema: "))
    if tentativa == senha:
        print("Acesso concedido. Bem-vindo ao sistema de monitoramento de tráfego!")
        break
    else:
        print("Senha incorreta. Tente novamente.")

for carro in registro_trafego:
    print(f"Modelo: {carro[0]}, Peso: {carro[1]} toneladas, Setor de Origem: {carro[2]}")

setores = set(carro[2] for carro in registro_trafego)
print("Setores de origem dos carros registrados:")
for setor in setores:
    print(setor)