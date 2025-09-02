# SentineIA

## Sistema de Detecção de Intrusões em Rede (Análise de Tráfego)

### 1. Introdução

Este projeto, denominado SentineIA, é um sistema de detecção de intrusões em rede que demonstra meu domínio em Engenharia e Ciência de Dados aplicadas à Cibersegurança. 

O objetivo foi construir um modelo de Machine Learning capaz de analisar o tráfego de rede e classificar automaticamente as conexões como normais ou ataques cibernéticos.

O projeto demonstra meu domínio sobre o ciclo de vida completo de um projeto de dados, desde a ingestão e preparação de dados brutos até a construção e avaliação de um modelo preditivo.

### 2. Funcionalidades

O SentineIA foi desenvolvido em um fluxo modular, com cada etapa do processo de dados separada para garantir clareza e manutenibilidade.

1. **Ingestão de Dados**: carregamento de dados de tráfego de rede em um DataFrame, com tratamento inicial para valores nulos e strings vazias.

2. **Preparação de Dados**: processamento de dados de forma escalável e eficiente, incluindo:

    - Codificação de colunas categóricas (One-Hot Encoding).

    - Normalização de features (Feature Scaling).

    - Análise de correlação para identificar redundâncias.

3. **Treinamento e Avaliação do Modelo**: construção e treinamento de um modelo de Machine Learning (RandomForestClassifier) para prever a ocorrência de ataques.

4. **Avaliação de Desempenho**: avaliação da acurácia do modelo em um conjunto de dados de teste que o modelo nunca viu, provando sua capacidade de generalização.

### 3. Tecnologias Utilizadas

- **Linguagem**: Python
- **Bibliotecas**:
    - **pandas**: para manipulação e análise de dados.
    - **scikit-learn**: para pré-processamento de dados e construção do modelo.
    - **Matplotlib**: para visualização de dados.
    - **seaborn**: para a criação de mapas de calor e visualizações estatísticas.
    - **NumPy**: para operações numéricas de alta performance.

### 4. Estrutura do Projeto

A estrutura do projeto segue as melhores práticas para garantir a modularidade e a clareza.

| Diretório/Arquivo       | Descrição                                                                 |
|--------------------------|---------------------------------------------------------------------------|
| `src/`                  | Contém os scripts principais do projeto                                   |
| ├── `data_ingestion.py` | Script para ingestão dos dados                                             |
| ├── `data_preparation.py` | Script para preparação e limpeza dos dados                              |
| └── `model_training.py` | Script para treinamento do modelo de IA                                   |
| `data/`                 | Diretório para armazenar datasets                                         |
| └── `UNSW_NB15.csv`     | Dataset UNSW-NB15 usado no treinamento/teste                              |
| `requirements.txt`      | Lista de dependências do projeto                                          |
| `README.md`             | Documentação principal do projeto                                         |

### 5.  Como Executar o Projeto
Para executar este projeto, siga os seguintes passos:

1. Clone este repositório:

```bash
git clone [link do seu repositório]
```

2. Navegue até o diretório do projeto:

```bash
cd [diretório do seu projeto]
```

3. Crie um ambiente virtual e ative-o (recomendado):

```bash
# windows
python -m venv .venv
.venv\Scripts\activate

# macOS/linux
python3 -m venv .venv
source .venv/bin/activate
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Execute o script de treinamento do modelo:

```bash
python src/model_training.py
```

**Sugestão**: Você pode utilizar outras bases de dados para o treinamento do modelo. No entanto, é altamente recomendado o uso de datasets bem formatados do Kaggle, pois a escolha de uma base não formatada exigirá um maior foco na etapa de Engenharia de Dados/ETL.

### 6. Resultados e Conclusão

Após o treinamento e validação, o modelo demonstrou um desempenho robusto, atingindo uma acurácia superior a 91%.

Isso demonstra que o modelo é altamente eficaz na detecção de intrusões em dados não vistos.

### 7. Próximos Passos Previstos

- **Análise de Erros**: investigar os casos em que o modelo falhou para entender os motivos e melhorar a sua performance.

- **Otimização do Modelo**: explorar outros modelos ou ajustar os hiperparâmetros do RandomForestClassifier para uma acurácia ainda maior.

Este projeto é uma prova da minha paixão em aplicar o poder dos dados para resolver problemas complexos no mundo real, com foco em segurança da informação.