#importando bibliotecas

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#importando dados

df = pd.read_csv("student_habits_performance.csv")

#visualizando dados

df

#tipo de dados

#colunas numéricas

cols = ['study_hours_per_day','social_media_hours','netflix_hours','exam_score','mental_health_rating','exercise_frequency' ]

#plotar o mapa de calor

sns.heatmap(df[cols].corr(), annot=True, cmap='coolwarm')
plt.title('correlação entre hábitos de estudo e desempenho em exames')
plt.show

#alunos que estudam mais tem melhor desempenho?
#o gráfico de dispersão mostra uma correlação positiva entre horas de estudo por dia e pontuação em exames, indicando que alunos que estudam mais tendem a ter um desempenho melhor nos exames.

#grafico de dispersão com linha de regressão.

sns.lmplot(data=df,x='study_hours_per_day', y='exam_score')
plt.title('mais estudos ➔ notas mais altas?')
plt.show()

#comparando médias de notas entre alunos que estudam mais de 5 horas por dia e menos de 2 horas por dia.

filtro_estudo_alto = df[df['study_hours_per_day'] > 5]
filtro_estudo_baixo = df[df['study_hours_per_day'] < 2]

grupo_estudo_alto = filtro_estudo_alto['exam_score'].mean()
grupo_estudo_baixo = filtro_estudo_baixo['exam_score'].mean()

print ('média de notas dos alunos que estudam mais de 5 horas por dia:', grupo_estudo_alto)
print ('média de notas dos alunos que estudam menos de 2 horas por dia:', grupo_estudo_baixo)
# --- IGNORE É SO PRA DEIXAR BONITO ---

#tempo gasto em rede socias vs notas

sns.histplot(data=df,x='social_media_hours')
plt.title('distribuição de horas em redes sociais')
plt.show()

#avaliando notas médias
#por diferentes intervalos (bins) de tempo gasto em redes sociais
#('0-2' horas, '2-4' horas, '4-6' horas, '6h+')

df['social_media_bins'] = pd.cut(df['social_media_hours'], bins=[0,2,4,6,float('inf')], labels=['0-2h','2-4','4-6','6h+'])

#plotar gráfico em caixa (boxplot)

sns.boxplot(data=df, x='social_media_bins', y='exam_score')
plt.title('notas médias por tempo gasto em redes sociais')
plt.show()

#frequência de exercícios físicos vs notas em exames

#plotar gráfico em caixa (boxplot)

sns.boxplot(data=df, x='exercise_frequency_bins', y='exam_score')
plt.title('frequência de exercícios físicos vs notas em exames')
plt.show()

#hábitos saudáveis vs notas em exames

sns.boxplot(data=df, x='diet_quality', y='exam_score')
plt.title('qualidade da dieta vs notas em exames')
plt.show()

#frequencia de exercicios fisicos
for col in ['exercise_frequency','mental_health_rating','diet_quality']:
    sns.boxplot(data=df, x=col, y='exam_score')
    plt.title(f'{col.replace("_"," ").title()} vs notas em exames')
    plt.show()

#há diferença nas notas de homens e mulheres?
#estatistica por genero (média e desvio padrão)
df.groupby('gender')['exam_score'].agg(['mean', 'std'])
