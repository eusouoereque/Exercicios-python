import pandas as pd

df = pd.read_csv('Aula9-Pandas/residuos.csv')

residuos_quimicos = df[df['material'] == 'Químico']
print("--- Resíduos do tipo 'Químico' ---")
print(residuos_quimicos.head())
print("\n")

soma_peso = df['peso'].sum()
print(f"Soma total do peso: {soma_peso:.2f}")

media_custo = df['preco'].mean()
print(f"Média de custo de descarte: {media_custo:.2f}")
