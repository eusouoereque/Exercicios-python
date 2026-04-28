import csv
import math

residuos = []
residuos_com_preco = []

def leitura_csv():
    try:
        with open('./aula6ma1/residuos2.csv', mode='r', encoding='utf-8') as arquivo:
            print("Lendo dados do arquivo...")
            leitor_csv = csv.DictReader(arquivo)
            for linha in leitor_csv:
                residuos.append(linha)
    except FileNotFoundError:
        print("O arquivo não existe!")

def calcular_preco(residuo):
    try:
        material = residuo['material']
        material = material.title()
        peso_str = residuo['peso'].strip()
        if peso_str.upper() == 'NAN':
             raise ValueError(f"Peso NaN para {residuo['material']}")
        
        peso = float(peso_str)
        if math.isnan(peso) or peso <= 0:
            raise ValueError(f"Peso inválido para {residuo['material']}: {peso}")
         

        if material == 'Químico':
            return peso * 15
        elif material == 'Metal':
            return peso * 5
        elif material == 'Papel':
            return peso * 2
        elif material == 'Plástico':
            return peso * 2
        else:
            raise ValueError(f"Tipo de resíduo desconhecido: {material}")
        
    except ValueError as e:
        print(f"Erro ao calcular preço para {residuo['material']}: {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado ao calcular preço para {residuo['material']}: {e}")
        return None


def gravar_dicionario(residuo, preco):
    try:
        import os
        arquivo_existe = os.path.exists('./aula6ma1/residuos3.csv')
        with open('./aula6ma1/residuos3.csv', mode='a', encoding='utf-8', newline='') as arquivo:
            escritor_csv = csv.DictWriter(arquivo, fieldnames=['material', 'peso', 'preco'])
            if not arquivo_existe:
                escritor_csv.writeheader()
            escritor_csv.writerow({'material': residuo['material'], 'peso': residuo['peso'], 'preco': preco})
    except Exception as e:
        print(f"Erro ao gravar no arquivo: {e}")

def analise_residuos():
    try:
        with open('./aula6ma1/residuos3.csv', mode='r', encoding='utf-8') as arquivo:
            print("Lendo dados do arquivo...")
            leitor_csv2 = csv.DictReader(arquivo)
            for linha in leitor_csv2:
                residuos_com_preco.append(linha)
    except FileNotFoundError:
        print("O arquivo não existe!")

    total_custo = 0
    total_quimico = total_metal = total_papel = total_plastico = 0
    count_quimico = count_metal = count_papel = count_plastico = 0
    for residuo in residuos_com_preco:
        try:
            material = residuo['material'].strip().title()
            peso_val = residuo['peso'].strip()
            preco_val = residuo['preco'].strip()

            if peso_val.upper() == 'NAN' or preco_val.upper() == 'NAN':
                continue
            
            peso = float(peso_val)
            preco = float(preco_val)

            if math.isnan(peso) or math.isnan(preco):
                continue

            total_custo += preco
            if material == 'Químico':
                total_quimico += peso
                count_quimico += 1
            elif material == 'Metal':
                total_metal += peso
                count_metal += 1
            elif material == 'Papel':
                total_papel += peso
                count_papel += 1
            elif material == 'Plástico':
                total_plastico += peso
                count_plastico += 1
        except ValueError as e:
            print(f"Erro ao converter valores: {residuo} - {e}")

    print(f"\n--- TOTAIS DE PESO ---")
    print(f"Total de resíduos químicos: {total_quimico:.2f} kg")
    print(f"Total de resíduos metálicos: {total_metal:.2f} kg")
    print(f"Total de resíduos de papel: {total_papel:.2f} kg")
    print(f"Total de resíduos plásticos: {total_plastico:.2f} kg")
    
    print(f"\n--- MÉDIAS DE PESO POR TIPO ---")
    if count_quimico > 0:
        print(f"Média de peso - Químico: {total_quimico/count_quimico:.2f} kg")
    if count_metal > 0:
        print(f"Média de peso - Metal: {total_metal/count_metal:.2f} kg")
    if count_papel > 0:
        print(f"Média de peso - Papel: {total_papel/count_papel:.2f} kg")
    if count_plastico > 0:
        print(f"Média de peso - Plástico: {total_plastico/count_plastico:.2f} kg")
    
    # Encontrar o material com maior volume de descarte
    materiais = {
        'Químico': total_quimico,
        'Metal': total_metal,
        'Papel': total_papel,
        'Plástico': total_plastico
    }
    
    material_maior_volume = max(materiais, key=materiais.get)
    maior_volume = materiais[material_maior_volume]
    
    print(f"\n--- MATERIAL COM MAIOR VOLUME DE DESCARTE ---")
    print(f"Material: {material_maior_volume}")
    print(f"Volume total: {maior_volume:.2f} kg")
    
    print(f"\nCusto total dos resíduos: R$ {total_custo:.2f}")


leitura_csv()
for residuo in residuos:
    preco = calcular_preco(residuo)
    if preco is not None:
        gravar_dicionario(residuo, preco)
analise_residuos()

