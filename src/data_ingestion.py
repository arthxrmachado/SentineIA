import pandas as pd
import numpy as np

def load_raw_data(file_path='data/UNSW_NB15.csv'):
    """
    Carrega o dataset bruto de um arquivo CSV.
    
    Parâmetros:
    file_path (str): Caminho para o arquivo CSV.
    
    Retorna:
    pd.DataFrame: dataframe contendo os dados carregados e tratados
    """
    # carrega o dataframe do arquivo csv
    df = pd.read_csv(file_path)
    
    # substitui strings vazias ou apenas com espaços por NaN em todo o dataframe
    # assim, logo abaixo na hora de verificar valores nulos, esses casos serão contabilizados
    df.replace(r'^\s*$', np.nan, regex=True, inplace=True)
    
    return df


if __name__ == "__main__":
    # define a opção para exibir todas as colunas
    pd.set_option('display.max_columns', None)

    # carrega o dataframe
    df = load_raw_data()
    
    # exibe as primeiras 5 linhas do dataframe para uma inspeção inicial
    print("Cabeçalho do dataset:")
    print(df.head())
    
    # exibe informações sobre o dataset (tipos de dados e valores nulos)
    print("\nInformações sobre o dataset:")
    print(df.info())
    
    # exibe a quantidade de valores ausentes por coluna
    print("\nValores ausentes por coluna:")
    print(df.isnull().sum())