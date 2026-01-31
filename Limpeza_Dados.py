# %%
import pandas as pd
# %% Chamando a tabala CSV para poder limpar os dados
df = pd.read_csv('Dados-profissao-dados.csv')
# %% Ver a tabela 
df.head()
# %% Apenas vê as colunas da tabala
df.columns
# %% Mudando os nomes das colunas para português
colunms_ptbr = {'work_year':'Ano',
           'experience_level' :'Senioridade',
           'employment_type': 'Contratos',
           'job_title': 'Cargo',
           'salary': 'Salario',
           'salary_currency': 'Moeda',
           'salary_in_usd': 'Dolar',
           'employee_residence': 'Residência',
           'remote_ratio': 'Modelo_trabalho',
           'company_location': 'Local',
           'company_size': 'Tamanho_empresa' }
df.rename(columns = colunms_ptbr, inplace=True)
print(df.columns)
# %% Olhar a tabala de Senioridade 
df['Senioridade'].value_counts()
# %% Trocando as definições de nomes da tabela 'Senioridade'
Senioridade = {'SE': 'Senior',
               'MI': 'Pleno',
               'EN': 'Junior',
               'EX': 'Executivo'}
df['Senioridade'] = df['Senioridade'].replace(Senioridade)
df['Senioridade'].value_counts()
# %% Olhando a tabela Contratos
df['Contratos'].value_counts()
# %%  Trocando as definições de nomes da tabela 'Contratos'
Contratos = {'FT': 'Tempo integral',
             'CT': 'Contrato',
             'PT': 'Tempo parcial',
             'FL': 'Freelance'}
df['Contratos'] = df['Contratos'].replace(Contratos)
df['Contratos'].value_counts()
# %% Olhando a tabela de tamanho das empresas
df['Tamanho_empresa'].value_counts()
# %% Trocando as definições de nomes da tabela de tamanho das empresas
Tamanho_empresa = {'M': 'Media',
                   'L': 'Grande',
                   'S': 'Pequena'}
df['Tamanho_empresa'] = df['Tamanho_empresa'].replace(Tamanho_empresa)
df['Tamanho_empresa'].value_counts()
# %% Olhando a tabela dos Modelos de trabalho 
df['Modelo_trabalho'].value_counts
# %% Trocando as definições de nomes da tabela de Modelos de trabalho
Modelo_trabalho = {100 :'Presencial',
                   50: 'Hibrido',
                   0: 'Remoto'}
df['Modelo_trabalho'] = df['Modelo_trabalho'].replace(Modelo_trabalho)
df['Modelo_trabalho'].value_counts()
# %% Olhando a tabala
df.head()
# %% Remove os dados nulos da tabela
df_limpo = df.dropna()
# %% Mostrar os Dados nulos para ver se tem algum
df_limpo.isnull().sum()
# %% Olhando como a tabala está
df_limpo.head()
# %% Mostrar as informações da tabela e os tipo de dados que tem
df_limpo.info()
# %% Troca o tipo do dados sobre o Dtype
df_limpo = df_limpo.assign(Ano = df_limpo['Ano'].astype('int64'))
# %%
df_limpo.head()
# %%
import seaborn as sns
# %% Grafico anual senioridade
sns.barplot(data = df_limpo, x='Senioridade', y= 'Dolar')
# %%
import matplotlib.pyplot as plt
# %%
plt.figure(figsize=(8,5))
sns.barplot(data = df_limpo, x='Senioridade', y= 'Dolar')
plt.title('Salario medio de Senioridade')
plt.xlabel('Senioridade')
plt.ylabel('Salario medio anual (Dolar)')
plt.show()
# %% Chama o dado limpo do grupo Senioriade com os dados em dolar,
# 'Mean' faz a media de todos os valores e ascending false vai do maior pro menor.
df_limpo.groupby('Senioridade')['Dolar'].mean().sort_values(ascending=False)
# %% Dando nome de ordem 
ordem = df_limpo.groupby('Senioridade')['Dolar'].mean().sort_values(ascending=False).index
ordem
# %%
plt.figure(figsize=(8,5))
sns.barplot(data = df_limpo, x='Senioridade', y= 'Dolar',order=ordem)
plt.title('Media salarial de senioridade')
plt.xlabel('Senioridade')
plt.ylabel('Salario medio anual (Dolar)')
plt.show()
# %%
plt.figure(figsize=(8,5))
sns.histplot(df_limpo['Dolar'], bins = 50, kde = True)
plt.title('Distribuiçâo dos salarios anuais')
plt.xlabel('Salario Dolar')
plt.ylabel('Frequencia)')
plt.show()
# %% trasformar os dados em CSV
df_limpo.to_csv('Dados-profissao-dados.csv', index=False)
# %%
 