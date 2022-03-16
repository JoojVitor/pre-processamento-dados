import numpy as np
import pandas as pd

doenca_pre = pd.read_csv('casos_obitos_doencas_preexistentes.csv', sep=';', encoding='utf-8')
doenca_pre.head()
doenca_pre.shape

from collections import Counter
Counter(doenca_pre.cs_sexo)
doenca_pre['cs_sexo'].value_counts()

doenca_pre.isnull().sum()

# Excluir valor NAN de cs_sexo
doenca_pre.dropna(subset=['cs_sexo'], inplace=True)

# Excluir Ignorado
relacao = doenca_pre.loc[doenca_pre.cs_sexo != 'IGNORADO']

# Excluir Indefinido
relacao = relacao.loc[relacao.cs_sexo != 'INDEFINIDO']
relacao['cs_sexo'].value_counts()
import plotly.express as px
px.pie(relacao, names="cs_sexo")

# Análise dos óbitos
relacao.obito.value_counts()
px.pie(relacao, names="obito")

# Análise da classificação dos atributos
relacao.dtypes

# Renomeando os registros da variável obito
relacao["obito"] = relacao["obito"].replace({0:"nao", 1:"sim"})
relacao.head()
relacao.dtypes
relacao.obito.value_counts()

# Transformando em variáveis categóricas
relacao['cs_sexo'] = relacao['cs_sexo'].astype('category')
relacao['obito'] = relacao['obito'].astype('category')