# 1. Importar librerías
import os
from typing import List

import joblib  # type: ignore
from sklearn.ensemble import RandomForestClassifier  # type: ignore
from sklearn.feature_extraction.text import CountVectorizer  # type: ignore
from sklearn.metrics import accuracy_score  # type: ignore
from sklearn.model_selection import train_test_split  # type: ignore
from sklearn.naive_bayes import MultinomialNB  # type: ignore

from poetry_demo.utils import base_dir

URL = f"{os.path.join(base_dir.url_dir(), 'data', 'modelo_rf.pkl')}"

first_list = [
    "futbol",
    "book",
    "tennis",
    "library",
]
first_list_outcomes = ["good", "bad", "good", "bad"]

vectorizer = CountVectorizer()
X_vect = vectorizer.fit_transform(first_list)

X_train, X_test, y_train, y_test = train_test_split(
    X_vect, first_list_outcomes, test_size=0.25, random_state=42
)

clf = MultinomialNB()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print("Exactitud:", accuracy_score(y_test, y_pred))


phrase = input("Dame una frase:\n")
nuevo = [phrase]
nuevo_vect = vectorizer.transform(nuevo)
print("Predicción:", clf.predict(nuevo_vect))


X: List[str] = [
    "me gusta los podcast",
    "no es buena la avena",
    "me gusta el helado",
    "no es bueno gritar",
]
y: List[int] = [1, 0, 1, 0]
vectorizer = CountVectorizer()
X_vect = vectorizer.fit_transform(X)


clf = RandomForestClassifier(random_state=42)
clf.fit(X_vect, y)

joblib.dump((vectorizer, clf), URL)

vectorizer_cargado, modelo_cargado = joblib.load(URL)

ejemplo = input("Dame una frase:\n")
nuevo = [ejemplo]
ejemplo_vect = vectorizer_cargado.transform(nuevo)
prediccion = modelo_cargado.predict(ejemplo_vect)

print("Predicción:", prediccion)
