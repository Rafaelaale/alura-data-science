# 📊 Regressão Linear aplicada ao Desempenho Acadêmico (ENADE)

Este repositório contém o projeto desenvolvido ao longo do **curso de Regressão Linear**, utilizando como base o dataset **Student Performance** (Kaggle), adaptado para um **contexto educacional brasileiro**, no qual o objetivo é **prever o desempenho acadêmico dos alunos por meio de uma nota simulada do ENADE (`enade_score`)**.

O projeto foi construído de forma incremental, com notebooks correspondentes a cada aula, culminando em um **notebook final com a solução completa**, integrando teoria, preparação dos dados, modelagem, otimização e avaliação.

---

## 🎯 Objetivo do Projeto

Prever o **`enade_score`** dos alunos a partir de características socioeducacionais, respondendo a perguntas como:

- Quais variáveis socioeducacionais mais influenciam o desempenho acadêmico?
- Como modelos de regressão podem apoiar decisões pedagógicas e institucionais?

---

## 📁 Estrutura do Repositório


---

## 📚 Descrição das Pastas

### 📂 `dataset/`
Contém o conjunto de dados utilizado no projeto:

- **StudentsPerformance.csv**  
  Dataset original do Kaggle com informações socioeducacionais dos alunos e suas notas, utilizado como base para a construção da variável alvo `enade_score`.
---

### 📂 `notebooks/`
Contém os notebooks desenvolvidos ao longo do curso, organizados por aula:

- **01 – Introdução ao problema de negócio**  
  Contextualização educacional e definição do problema de regressão.

- **02 – Análise Exploratória dos Dados (EDA)**  
  Estatísticas descritivas, visualizações e entendimento das variáveis.

- **03 – Preparação dos Dados**  
  Tratamento de variáveis categóricas, normalização e divisão treino/teste.

- **04 – Regressão Linear Baseline**  
  Criação de um modelo baseline para comparação.

- **05 – Avaliação do Modelo**  
  Uso das métricas MAE, MSE, RMSE e R², com interpretação dos resultados.

- **06 – Otimização com Ridge e Lasso**  
  Regularização, controle de overfitting e análise viés × variância.

- **07 – Projeto Final**  
  Notebook consolidado com todo o pipeline:
  - Preparação dos dados  
  - Treinamento do modelo  
  - Otimização  
  - Avaliação final  
  - Discussão dos resultados  

---

## 🧠 Modelos Utilizados

- Regressão Linear Simples
- Regressão Linear Múltipla
- Regressão Ridge (L2)
- Regressão Lasso (L1)

---

## 📊 Métricas de Avaliação

Os modelos foram avaliados utilizando:

- **MAE (Mean Absolute Error)**
- **MSE (Mean Squared Error)**
- **RMSE (Root Mean Squared Error)**
- **R² (Coeficiente de Determinação)**

As métricas foram interpretadas considerando o contexto educacional, onde variabilidade natural dos dados impacta diretamente os resultados.

---

## Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib / Seaborn
- Jupyter Notebook

##  Observações Finais

Este projeto foi desenvolvido com fins educacionais, buscando demonstrar boas práticas em projetos de Ciência de Dados, desde a formulação do problema até a avaliação e otimização de modelos de regressão.


