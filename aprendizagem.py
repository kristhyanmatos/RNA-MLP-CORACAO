import pandas
import tensorflow
import matplotlib.pyplot as plt
from tensorflow import keras
from sklearn.model_selection import train_test_split


class Aprendizagem:
    def __init__(self, numero_epocas) -> None:
        self.dados = pandas.read_csv("heart.csv")
        self.entradas = self.dados[
            [
                "age",
                "sex",
                "cp",
                "trestbps",
                "chol",
                "fbs",
                "restecg",
                "thalach",
                "exang",
                "oldpeak",
                "slope",
                "ca",
                "thal",
            ]
        ].to_numpy()
        self.saidas = self.dados["target"]

        (
            self.entradas_treino,
            self.entradas_teste,
            self.saidas_treino,
            self.saidas_teste,
        ) = train_test_split(
            self.entradas,
            self.saidas,
            test_size=0.3,
        )

        self.modelo = keras.Sequential(
            [
                keras.layers.Dropout(0.14),
                keras.layers.Dense(6, input_shape=(13,), activation=tensorflow.nn.relu),
                keras.layers.Dense(2, activation=tensorflow.nn.softmax),
            ]
        )
        self.modelo.compile(
            optimizer="adam",
            loss="sparse_categorical_crossentropy",
            metrics="accuracy",
        )

        self.hist = self.modelo.fit(
            self.entradas_treino,
            self.saidas_treino,
            batch_size=106,
            epochs=numero_epocas,
            verbose=0,
            validation_data=(self.entradas_teste, self.saidas_teste),
        )

        plt.plot(self.hist.history["accuracy"])
        plt.plot(self.hist.history["val_accuracy"])
        plt.title("Acurácia por épocas")
        plt.xlabel("Épocas")
        plt.ylabel("Acurácia")
        plt.legend(["Treino", "Valores de Teste"])
        plt.show()

        plt.plot(self.hist.history["loss"])
        plt.plot(self.hist.history["val_loss"])
        plt.title("Taxa de perda por época")
        plt.xlabel("Épocas")
        plt.ylabel("Taxa de perda")
        plt.legend(["Treino", "Valores de Teste"])
        plt.show()
