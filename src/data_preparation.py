from data_ingestion import load_raw_data
import pandas as pd
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def get_prepared_data():
    """
    Prepara os dados para o treinamento do modelo.
    
    Retorna:
    X_scaled_df (pd.DataFrame): DataFrame com as features escalonadas.
    target (pd.Series): Série com a variável target ('label').
    """
    # carrega o dataframe
    df = load_raw_data()
    
    # remove as colunas que não serão usadas como features ('attack_cat' e 'label'), afinal essas duas colunas mostram o tipo de ataque e se é ataque ou não.
    # vamos focar em 'label' que mostra se a conexão é normal (0) ou um ataque (1). o modelo tentará prever esse valor.
    df_features = df.drop(columns=['attack_cat', 'label'])
    
    # identifica as colunas categóricas para codificação
    # basicamente são colunas que possuem valores não numéricos, como 'tcp', 'udp', etc.
    categorical_cols = ['proto', 'service', 'state']
    
    # usa o pd.get_dummies para aplicar o one-hot encoding
    # o parâmetro drop_first=True evita a multicolinearidade, que pode confundir o modelo.
    df_features_encoded = pd.get_dummies(df_features, columns=categorical_cols, drop_first=True)

    # define a variável target (a coluna 'label')
    target = df['label']

    # lida com valores infinitos
    df_features_encoded.replace([float('inf'), -float('inf')], 0, inplace=True)
    df_features_encoded.fillna(0, inplace=True)
    
    # o escalonador normaliza os dados para que todas as colunas tenham a mesma escala.
    # assim, o modelo não será tendencioso por causa de colunas com valores muito altos ou muito baixos.
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df_features_encoded)
    
    # X_scaled vira um array numpy
    # o array numpy é uma estrutura de dados super rápida e eficiente para realizar cálculos matemáticos, mas não têm os nomes das colunas
    # assim, vamos converter de volta para dataframe do pandas, com os nomes das colunas originais
    X_scaled_df = pd.DataFrame(X_scaled, columns=df_features_encoded.columns)
    
    return X_scaled_df, target


if __name__ == "__main__":
    # define a opção para exibir todas as colunas
    pd.set_option('display.max_columns', None)

    # pega os dados preparados
    X_scaled_df, target = get_prepared_data()

    # mostra as primeiras 5 linhas do dataframe escalonado
    print("Primeiras 5 linhas do DataFrame escalonado:")
    print(X_scaled_df.head())

    # mostra a média e o desvio padrão de todas as colunas escalonadas
    print("\nVerificando Média e Desvio Padrão das colunas escalonadas:")
    print(X_scaled_df.mean().round(2))
    print(X_scaled_df.std().round(2))

    # calcula a matriz de correlação
    corr_matrix = X_scaled_df.corr().abs()

    # pega o triângulo superior da matriz
    # basicamente esse trecho de código pega só metade da matriz de correlação, porque a outra metade é redundante
    upper_triangle = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))

    # encontra as colunas com alta correlação
    highly_correlated_cols = [
        column for column in upper_triangle.columns
        if any(upper_triangle[column] > 0.5)
    ]

    print("Colunas com correlação maior que 0.5:")
    print(highly_correlated_cols)

    # analisa a correlação da coluna 'proto_udp'
    # pode analisar qualquer coluna, mas escolhi 'proto_udp' porque é uma das colunas categóricas mais comuns
    print("\nCorrelação da coluna 'proto_udp' com as outras colunas:")
    print(corr_matrix['proto_udp'].sort_values(ascending=False))

    # cria um mapa de calor para visualizar a matriz de correlação
    plt.figure(figsize=(12, 10))
    sns.heatmap(corr_matrix, annot=False, cmap='coolwarm')
    plt.title('Mapa de Calor da Matriz de Correlação')
    plt.show()

    print("Dados preparados e escalonados com sucesso!")