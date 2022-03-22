import numpy as np
import pandas as pd
import plotly.express as px

from collections import Counter
from regressao_logistica import logistic_regression

doenca_pre = pd.read_csv('casos_obitos_doencas_preexistentes.csv', sep=';', encoding='utf-8')

# Excluir valor NAN de cs_sexo
doenca_pre.dropna(subset=['cs_sexo'], inplace=True)

# Excluir Ignorado
relacao = doenca_pre.loc[doenca_pre.cs_sexo != 'IGNORADO']

# Excluir Indefinido
relacao = relacao.loc[relacao.cs_sexo != 'INDEFINIDO']

relacao = relacao.loc[relacao.idade != 'NA']

# Renomeando os registros da variável obito
relacao["cs_sexo"] = relacao["cs_sexo"].replace({'MASCULINO': 0, 'FEMININO': 1})
relacao["diagnostico_covid19"] = relacao["diagnostico_covid19"].replace({'CONFIRMADO': 1})

X = relacao[["cs_sexo", "diagnostico_covid19"]]
y = relacao["obito"]

logistic_regression(X, y)
