registro_trafego = []
# função para verificar peso do veículo
def verificar_peso(veiculo):
    if int(veiculo['peso']) > 10:
        print(f"ALERTA: Veículo {veiculo['modelo']} com peso excessivo detectado!")

# função para verificar acesso
def verificar_acesso():
    senha = 115211
    while True:
        tentativa = int(input("Digite a senha para acessar o sistema: "))
        if tentativa == senha:
            print("Acesso concedido. Bem-vindo ao sistema de monitoramento de tráfego!")
            break
        else:
            print("Senha incorreta. Tente novamente.")

# função para registrar um veículo
def registrar_veiculo():
    modelo = input("Digite o modelo do carro: ")
    peso = input("Digite o peso em toneladas do carro: ")
    setorOrigem = input("Digite o setor de origem do carro: ")

    veiculo = {"modelo": modelo, "peso": peso, "setorOrigem": setorOrigem}
    verificar_peso(veiculo)
    return veiculo

# função para mostrar relatório
def mostrar_relatorio(registro_trafego):
    for veiculo in registro_trafego:
        print(f"Modelo: {veiculo['modelo']}, Peso: {veiculo['peso']} toneladas, Setor de Origem: {veiculo['setorOrigem']}")

    setores = set(veiculo['setorOrigem'] for veiculo in registro_trafego)
    print("Setores de origem dos veiculos registrados:")
    for setor in setores:
        print(setor)


# função para verificar peso do veículo
for i in range(5):

    print(f"\nCadastro do veículo {i+1}")

    veiculo = registrar_veiculo()

    registro_trafego.append(veiculo)


verificar_acesso()
mostrar_relatorio(registro_trafego)