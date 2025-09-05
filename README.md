# 📊 Data Science Estudos — Notebooks & Análises

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)
![Pandas](https://img.shields.io/badge/Library-pandas-%23150458.svg)
![NumPy](https://img.shields.io/badge/Library-NumPy-013243.svg)
![Matplotlib](https://img.shields.io/badge/Library-Matplotlib-ffffff.svg)
![License](https://img.shields.io/badge/license-MIT-blue)

> Repositório com **notebooks e scripts** de **Ciência de Dados**: EDA, estatística, visualização.  
> Conteúdo comentado **em português** e organizado para reprodutibilidade.

---

## 📚 Conteúdo do curso concluído (Udemy)

**Curso:** Bootcamp PYTHON e Inteligência Artificial: Do Zero ao Expert - parte de Ciência de Dados ✅

- **Fundamentos & Ambiente**
  - Objetivo do curso, o que é Data Science, rotina do Engenheiro de DS
  - Onde conseguir datasets (ex.: Kaggle)

- **Pandas (leitura, transformação e exportação)**
  - Abrindo arquivos com `pandas` (CSV/Excel/…)
  - Lendo dados, `loc`, `sort_values`
  - Adicionando colunas, modificando dados
  - Filtrando com condições e com **Regex + Conditions**
  - `groupby` para agregações
  - **Exportando dados** (CSV/Excel)

- **NumPy (arrays)**
  - Introdução ao NumPy
  - Criando arrays 1D/2D/3D
  - Somando arrays
  - Selecionando itens (slice/indexing)

- **Matplotlib (visualização)**
  - O que é Matplotlib · Documentação
  - Importando dataset e **criando o primeiro gráfico**
  - Legenda e ticks · formatando labels e cores
  - Loop (`for`) para múltiplas séries
  - **Salvando o gráfico** (figura)

> Esses tópicos guiam os notebooks deste repositório.

---

## 🖼️ Exemplo de gráfico

<p align="center">
  <img src="img/country.png" alt="Distribuição por país — gráfico country.png" width="700">
  <br/>
  <sub><i>Figura gerada nos notebooks de visualização.</i></sub>
</p>

---

## 📂 Estrutura do repositório
```
data_science_estudos/
├─ notebooks/ # exercícios / análises (ipynb)
├─ data/ # dataframes (raw/processed)
├─ img/ # figuras exportadas pelos notebooks
├─ requirements.txt
└─ README.md
```

---

## ▶️ Como executar

```bash
git clone https://github.com/MiguelReisM/data_science_estudos.git
cd data_science_estudos

python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

---

## 👨‍💻 Autor
- Miguel Reis Milan Lopes


