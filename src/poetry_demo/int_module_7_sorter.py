# 1. Importar librerías
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

X = [
    "futbol",
    "book",
    "tennis",
    "library",
]
y = ["good", "bad", "good", "bad"]

vectorizer = CountVectorizer()
X_vect = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_vect, y, test_size=0.25, random_state=42
)

clf = MultinomialNB()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print("Exactitud:", accuracy_score(y_test, y_pred))


phrase = input("Dame una frase:\n")
nuevo = [phrase]
nuevo_vect = vectorizer.transform(nuevo)
print("Predicción:", clf.predict(nuevo_vect))


X = [
    "me gusta los podcast",
    "no es buena la avena",
    "me gusta el helado",
    "no es bueno gritar",
]
y = [1, 0, 1, 0]
vectorizer = CountVectorizer()
X_vect = vectorizer.fit_transform(X)


clf = RandomForestClassifier(random_state=42)
clf.fit(X_vect, y)

joblib.dump((vectorizer, clf), "modelo_rf.pkl")

vectorizer_cargado, modelo_cargado = joblib.load("modelo_rf.pkl")

ejemplo = input("Dame una frase:\n")
nuevo = [ejemplo]
ejemplo_vect = vectorizer_cargado.transform(nuevo)
prediccion = modelo_cargado.predict(ejemplo_vect)

print("Predicción:", prediccion)
