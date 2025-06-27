# 🌙 Clustering Inteligente com KMeans, DBSCAN e Hierárquico

> Um experimento visual e interativo com algoritmos de agrupamento usando dados não lineares em forma de lua 🌕

---

### 🔍 Visão Geral

Neste projeto, exploramos o poder dos algoritmos de **agrupamento (clustering)** aplicados a dados não triviais. Usamos o conjunto **`make_moons`** do `scikit-learn`, ideal para testar modelos em situações onde formas não esféricas e a presença de ruído desafiam técnicas tradicionais.

🎯 **Objetivo:** Comparar visualmente os resultados dos modelos de clustering, **KMeans**, **DBSCAN** e **Agglomerative Clustering**, e entender suas características, vantagens e limitações na identificação de padrões complexos.

---

### 🚀 Algoritmos Utilizados

| Algoritmo               | Tipo                      | Destaques                                                                 |
|-------------------------|---------------------------|--------------------------------------------------------------------------|
| `KMeans`                | Particional               | Simples e eficiente, mas sensível a formas não circulares e outliers.    |
| `AgglomerativeClustering` | Hierárquico            | Cria hierarquias naturais de agrupamentos, bom para estruturas aninhadas. |
| `DBSCAN`                | Densidade (Density-Based) | Excelente com formas arbitrárias, detecção de outliers e clusters de densidade variável. |

---

### 📊 Resultados Visuais: A Jornada dos Agrupamentos

Acompanhe a transformação dos nossos dados "lua" à medida que cada algoritmo tenta desvendar sua estrutura interna. Para uma experiência completa, **clique nas imagens** para explorar os gráficos interativos!

#### 🌑 O Desafio: Nossos Dados Originais
O ponto de partida: como os dados se apresentam, com as duas "luas" entrelaçadas e o ruído.

[![Dataset Original](images/original_dataset_moon.png)](original_dataset_moon.html)

---

#### ✨ A Busca por Centros: K-Means em Ação
O K-Means tenta dividir os dados em 2 grupos baseando-se em seus centroides. Observe sua dificuldade em lidar com formas não-esféricas.

[![K-Means Clustering](images/kmeans_clusters_and_centroids.png)](kmeans_clusters_and_centroids.html)

---

#### 🌳 A Construção de Hierarquias: Agglomerative Clustering
Este método hierárquico agrupa os pontos passo a passo, formando clusters com base na proximidade.

[![Agglomerative Clustering](images/agglomerative_clusters.png)](agglomerative_clusters.html)

---

#### 🌌 Encontrando Densidades e Ruídos: O Poder do DBSCAN
O DBSCAN se destaca por identificar clusters de diferentes formas e densidades, além de conseguir isolar o ruído (pontos em cinza/roxo). Para o dataset `make_moons`, ele geralmente revela a estrutura real com maestria.

[![DBSCAN Clustering](images/dbscan_clusters.png)](dbscan_clusters.html)

---

### 🧠 Aprendizados Esperados

- Compreensão das **diferenças fundamentais** entre agrupamentos particionais, hierárquicos e baseados em densidade.
- **Visualização clara** de como diferentes modelos lidam com a complexidade de dados não lineares e com ruído.
- Critérios para **escolher o algoritmo** mais adequado com base na forma e densidade dos seus dados.

---

### 📦 Instalação

Para rodar este projeto localmente, siga estes passos:

1.  Clone o repositório:

    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    cd seu-repositorio
    ```

2.  Instale as dependências. Certifique-se de que o `kaleido` esteja incluído para salvar os gráficos como imagem:

    ```bash
    pip install -r requirements.txt
    ```
    (Crie um arquivo `requirements.txt` com: `pandas`, `numpy`, `scikit-learn`, `plotly`, `kaleido`)

3.  Execute o notebook Jupyter para gerar os gráficos e os resultados:

    ```bash
    jupyter notebook clustering_algorithms.ipynb
    ```

---

### 🧰 Tecnologias & Bibliotecas

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/python/)
[![Numpy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-333333?style=for-the-badge&logo=pandas)](https://pandas.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![K-Means](https://img.shields.io/badge/K--Means-blue?style=for-the-badge&logo=appveyor&logoColor=white)](https://scikit-learn.org/stable/modules/clustering.html#k-means)
[![DBSCAN](https://img.shields.io/badge/DBSCAN-red?style=for-the-badge&logo=appveyor&logoColor=white)](https://scikit-learn.org/stable/modules/clustering.html#dbscan)
[![Agglomerative](https://img.shields.io/badge/Agglomerative-green?style=for-the-badge&logo=appveyor&logoColor=white)](https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering)

---

### 👨‍💻 Autor

**Daniel Coelho**  
💼 [LinkedIn](https://www.linkedin.com/in/daniel-coelho-818381293/) • 💻 [GitHub](https://github.com/danccoelho)  

---

### 🌟 Contribua!

Se você curtiu o projeto, deixe uma ⭐ no repositório e contribua com novas ideias ou melhorias!

---