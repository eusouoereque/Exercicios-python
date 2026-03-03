saida = 1
equipamentos = []

while saida != 0:
    nomeEquipamento = input("Digite o nome do equipamento: ")
    consumoEnergia = float(input("Digite o consumo de energia do equipamento em W: "))
    equipamento = (nomeEquipamento, consumoEnergia)
    equipamentos.append(equipamento)

    if consumoEnergia > 800:
        print(f"Atenção: Equipamento {nomeEquipamento} requer inspeção.")

    saida = int(input("Digite 0 para sair ou 1 para continuar: "))

soma = 0
for equipamento in equipamentos:
    soma += equipamento[1]

print(f"Consumo total de energia: {soma} W")