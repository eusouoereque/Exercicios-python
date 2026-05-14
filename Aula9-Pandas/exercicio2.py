import pandas as pd
import os

path = os.path.join(os.path.dirname(__file__), 'residuos.csv')
df_residuos = pd.read_csv(path)
df_residuos = df_residuos.rename(columns={'preco': 'custo'})

print("Resíduos > 30kg:")
print(df_residuos[df_residuos['peso'] > 30])

custo_plastico = df_residuos[df_residuos['material'] == 'Plástico']['custo'].sum()
print(f"\nCusto Plástico: {custo_plastico}")

print("\nInfo custo:")
df_residuos['custo'].info()

print(f"\nMaior peso: {df_residuos['peso'].max()}")
