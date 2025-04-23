# model.py
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Cargar datos
data = load_iris()
X, y = data.data, data.target

# Entrenar modelo
model = RandomForestClassifier()
model.fit(X, y)

# Guardar modelo
joblib.dump(model, "app/model.joblib")
