import pandas as pd
from pathlib import Path

DIR = Path(__file__).parent

# ============================================================
# 1. Exploração e Saneamento
# ============================================================

pacientes = pd.read_csv(DIR / 'pacientes_v2.csv', sep=';')
atendimentos = pd.read_csv(DIR / 'atendimentos_v2.csv', sep=';')
custos = pd.read_csv(DIR / 'custos_exames_v2.csv', sep=';')

# Limpar nomes: remover espaços e padronizar para maiúsculas
pacientes['nome'] = pacientes['nome'].str.strip().str.upper()

# Remover duplicatas
pacientes = pacientes.drop_duplicates()

print("=" * 60)
print("SAÍDA 1 - CADASTRO LIMPO (após saneamento e remoção de duplicatas)")
print("=" * 60)
print(f"Número de linhas: {len(pacientes)}")
print(pacientes.head(10))
print()

# Tratar coluna oxigenacao: remover '%' e converter para float
atendimentos['oxigenacao'] = (
    atendimentos['oxigenacao'].astype(str).str.replace('%', '', regex=False).astype(float)
)

# Corrigir temperatura com valor inconsistente (380.0 -> 38.0)
atendimentos.loc[atendimentos['temperatura'] > 100, 'temperatura'] = (
    atendimentos.loc[atendimentos['temperatura'] > 100, 'temperatura'] / 10
)

# ============================================================
# 2. Integração de Dados (Merge)
# ============================================================

# Operação A — Inner Join: Pacientes + Atendimentos
df_inner = pd.merge(pacientes, atendimentos, on='id_paciente', how='inner')

print("=" * 60)
print("SAÍDA 2 - PRIMEIRO JOIN (Inner: Pacientes + Atendimentos)")
print("=" * 60)
print(f"Número de linhas: {len(df_inner)}")
print(df_inner.head(10))
print()
print("Explicação: o número de linhas diminuiu porque o Inner Join")
print("mantém apenas os pacientes que existem em AMBAS as tabelas.")
print("Pacientes sem atendimento e atendimentos sem cadastro (IDs 2000-2009)")
print("foram excluídos.")
print()

# Operação B — Left Join: resultado A + Custos
df_final = pd.merge(df_inner, custos, on='id_paciente', how='left')

print("=" * 60)
print("SAÍDA 3 - SEGUNDO JOIN (Left: resultado anterior + Custos)")
print("=" * 60)
print(f"Número de linhas: {len(df_final)}")
print(df_final.head(10))
print()
print("Pacientes sem exames (exame e valor_exame ficam como NaN):")
sem_exame = df_final[df_final['valor_exame'].isna()][['id_paciente', 'nome', 'exame', 'valor_exame']].drop_duplicates('id_paciente')
print(sem_exame.head(5))
print()

# ============================================================
# 3. Lógica de Negócio — Status Crítico
# ============================================================

df_final['Status_Critico'] = df_final.apply(
    lambda row: 'SIM' if row['temperatura'] > 38.5 or row['oxigenacao'] < 90 else 'NÃO',
    axis=1
)

criticos = df_final[df_final['Status_Critico'] == 'SIM']

# ============================================================
# 4. Relatório por Cidade
# ============================================================

relatorio = df_final.groupby('cidade').agg(
    media_idade=('idade', 'mean'),
    custo_total_exames=('valor_exame', 'sum')
).reset_index()

relatorio.to_csv(DIR / 'custoxcidade.csv', index=False)

print("=" * 60)
print("SAÍDA 4 - RELATÓRIO POR CIDADE (exportado: custoxcidade.csv)")
print("=" * 60)
print(relatorio.to_string(index=False))
print()

# ============================================================
# 5. Tabela de Auditoria de Fluxo
# ============================================================

print("=" * 60)
print("TABELA DE AUDITORIA DE FLUXO")
print("=" * 60)
print(f"{'Etapa de Processamento':<28} {'Comando Pandas':<26} {'Linhas Restantes'}")
print("-" * 75)
print(f"{'Carga e Limpeza':<28} {'drop_duplicates()':<26} {len(pacientes)}")
print(f"{'Integração Clínica':<28} {'merge(how=inner)':<26} {len(df_inner)}")
print(f"{'Integração Financeira':<28} {'merge(how=left)':<26} {len(df_final)}")
print(f"{'Filtro de Casos Críticos':<28} {'df[df[Status]==SIM]':<26} {len(criticos)}")
