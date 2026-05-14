**Desafio de Engenharia de Dados: Integração e Auditoria Hospitalar (ODS 3\)** 

No Centro de Saúde a fragmentação de dados impede uma visão clara da saúde da população. Sua missão como Engenheiro de Dados é unificar as bases de Cadastro, Triagem e Financeiro, gerando um relatório de prioridade clínica e auditando o fluxo dos pacientes. 

**Requisitos da Atividade:** 

1\. **Exploração e Saneamento:** 

○ Carregar os arquivos: pacientes.csv, atendimentos.csv e custos\_exames.csv. ○ Limpar nomes (remover espaços e padronizar para maiúsculas) e tratar duplicatas. 2\. **Integração de Dados (Merge):** 

○ **Operação A (Inner Join):** Unir *Pacientes* com *Atendimentos*. 

○ **Operação B (Left Join):** Unir o resultado da Operação A com a base de *Custos*. 3\. **Lógica de Negócio (Status Crítico):** 

○ Criar a coluna Status\_Critico: **"SIM"** se Temperatura \> 38.5 **OU** Oxigenação \< 90\. Caso contrário, **"NÃO"**. 

4\. **Relatório e Agrupamento:** 

○ Calcular a média de idade e o custo total de exames por Cidade e exportar para um arquivo .csv chamado: **custoxcidade.csv**. 

**O que deve ser entregue?** 

Para cada etapa abaixo, no **relatório** deve conter o **número de linhas** e o **print/exibição das 10 primeiras linhas** (df.head()) do resultado: 

1\. **Saída do Cadastro Limpo:** Demonstrar que os nomes foram padronizados e duplicatas removidas. 

2\. **Saída do Primeiro Join (Inner):** Exibir os dados combinados de Paciente \+ Atendimento. Explicar por que o número de linhas diminuiu ou aumentou. 

3\. **Saída do Segundo Join (Left):** Exibir a tabela final integrando os custos. Mostrar como ficaram os pacientes que não realizaram exames (colunas de custo vazias). 

4\. **Tabela de Auditoria de Fluxo:** 

| Etapa de Processamento  Carga e Limpeza  Integração Clínica  | Comando Pandas  drop\_duplicates()  merge(how='inner')  | Linhas Restantes  ...  ... |
| :---- | :---- | :---- |
| **Integração Financeira**  | merge(how='left')  | ... |

**Filtro de Casos Críticos** df\[df\['Status'\]=='SIM'\] ...