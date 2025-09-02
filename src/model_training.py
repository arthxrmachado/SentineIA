from data_preparation import get_prepared_data
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

def main():
    # pega os dados preparados
    X, y = get_prepared_data()

    # divide os dados em conjuntos de treinamento e teste
    # 80% para treinamento e 20% para teste
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # criando o cérebro do modelo e treinando-o
    # 'random_state=42' garante que os resultados serão os mesmos a cada vez.
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # fazendo previsões
    # o método 'predict' usa o modelo treinado para fazer previsões em dados que ele nunca viu
    y_pred = model.predict(X_test)

    # avaliando o desempenho
    # a acurácia mede a porcentagem de previsões corretas do modelo
    accuracy = accuracy_score(y_test, y_pred)

    return accuracy


if __name__ == "__main__":
    accuracy = main()
    print(f"\nAcurácia do Modelo: {accuracy:.4f}")