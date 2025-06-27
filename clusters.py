# %%
# Importação das bibliotecas necessárias para o projeto de Clustering (Agrupamento).
# pandas (pd): Usado para manipulação e análise de dados tabulares.
import pandas as pd
# numpy (np): Essencial para computação numérica de alto desempenho, especialmente com arrays e matrizes.
import numpy as np
# Função do Scikit-learn para gerar um dataset sintético.
from sklearn.datasets import make_moons
# Algoritmos de Clustering do Scikit-learn:
from sklearn.cluster import DBSCAN, KMeans, AgglomerativeClustering
# plotly.express (px): Uma biblioteca de alto nível para criar gráficos interativos rapidamente.
import plotly.express as px
# plotly.graph_objects (go): Uma biblioteca de baixo nível para controle mais fino sobre os gráficos Plotly.
import plotly.graph_objects as go

# %%
# Geração do dataset sintético 'make_moons'.
# n_samples=1500: Define o número total de pontos de dados a serem gerados.
# noise=0.09: Adiciona ruído gaussiano aos dados.
X_random, y_random = make_moons(n_samples=1500, noise=0.09)

# %%
X_random

# %%
y_random

# %%
# Verificação dos valores únicos e suas contagens nos rótulos verdadeiros (y_random).
np.unique(y_random)

# %%
# Visualização inicial do dataset 'make_moons' sem agrupamento.
# Este gráfico de dispersão mostra a forma original dos dados, com as duas "luas" entrelaçadas.
# É importante para entender a complexidade do problema que os algoritmos de clustering tentarão resolver.
grafico = px.scatter(x= X_random[:,0], y= X_random[:,1])
grafico.show()
grafico.write_image("images/original_dataset_moon.png")

# %%
# Aplicação do algoritmo K-Means.
# n_clusters=2: Define que o algoritmo deve tentar encontrar 2 clusters.
#               Este valor é escolhido porque sabemos (pelo make_moons) que existem 2 estruturas principais.
# rotulos_kmeans: Armazena os rótulos de cluster atribuídos pelo K-Means a cada ponto de dados.
kmeans = KMeans(n_clusters=2)
rotulos_kmeans = kmeans.fit_predict(X_random)

# %%
# Visualização dos resultados do K-Means, incluindo os centroides.
# centroides_kmeans: Coordenadas dos centroides de cada cluster encontrados pelo K-Means.
# grafico_kmeans1: Gráfico de dispersão dos pontos, coloridos pelos rótulos do K-Means.
# grafico_kmeans2: Gráfico de dispersão dos centroides, com tamanho maior para destaque.
# grafico_kmeans3: Combina os dois gráficos anteriores em uma única figura interativa.
#                  Isso permite ver os clusters e seus respectivos centros juntos.
centroides_kmeans = kmeans.cluster_centers_
grafico_kmeans1 = px.scatter(x= X_random[:,0], y= X_random[:,1], color= rotulos_kmeans)
grafico_kmeans2 = px.scatter(x= centroides_kmeans[:,0], y= centroides_kmeans[:,1], size= [2,2])
grafico_kmeans3 = go.Figure(data= grafico_kmeans1.data + grafico_kmeans2.data)
grafico_kmeans3.show()
grafico_kmeans3.write_image("images/kmeans_clusters_and_centroids.png")

# %%
# Aplicação do algoritmo Agglomerative Clustering (Agrupamento Hierárquico).
# n_clusters=2: Define que o algoritmo deve formar 2 clusters.
# linkage='ward': Critério usado para mesclar os clusters. 'ward' minimiza a variância dentro de cada cluster.
# rotulos_hc: Armazena os rótulos de cluster atribuídos pelo Agglomerative Clustering.
hc = AgglomerativeClustering(n_clusters=2, linkage='ward')
rotulos_hc = hc.fit_predict(X_random)
grafico_hc = px.scatter(x= X_random[:,0], y= X_random[:,1], color= rotulos_hc)
grafico_hc.show()
grafico_hc.write_image("images/agglomerative_clusters.png")

# %%
# Aplicação do algoritmo DBSCAN (Density-Based Spatial Clustering of Applications with Noise).
# eps=0.1: Raio de vizinhança. Define a distância máxima entre duas amostras para que uma seja considerada
#          vizinha da outra. A escolha de 'eps' é crucial e depende da densidade dos dados.
# min_samples=5: Número mínimo de amostras em uma vizinhança para que um ponto seja considerado um ponto central (core point).
# rotulos_dbscan: Armazena os rótulos de cluster atribuídos pelo DBSCAN.
#                 Pontos de ruído (outliers) são atribuídos ao rótulo -1.
dbscan = DBSCAN(eps=0.1)
rotulos_dbscan = dbscan.fit_predict(X_random)

# %%
# Verificação dos valores únicos e suas contagens nos rótulos do DBSCAN.
# É comum ver o rótulo '-1' aqui, que representa os pontos classificados como ruído pelo DBSCAN.
# A contagem mostra quantos pontos foram atribuídos a cada cluster, incluindo o ruído.
np.unique(rotulos_dbscan, return_counts=True)

# %%

# Visualização dos resultados do DBSCAN.
# Os pontos são coloridos de acordo com os clusters encontrados.
# Pontos em -1 (ruído) terão uma cor distinta se Plotly os mapear.grafico_dbscan = px.scatter(x= X_random[:,0], y= X_random[:,1], color= rotulos_dbscan)
grafico_dbscan = px.scatter(x= X_random[:,0], y= X_random[:,1], color= rotulos_dbscan)
grafico_dbscan.show()
grafico_dbscan.write_image("images/dbscan_clusters.png")


