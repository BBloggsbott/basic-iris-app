from fastapi import FastAPI
import joblib

app = FastAPI()
model = joblib.load("model.joblib")


@app.get("/healthz")
async def predict():
    return {
        "status": "healthy"
    }

@app.post("/predict")
async def predict(sepal_length: float = 0.0, sepal_width: float = 0.0, petal_length: float = 0.0, petal_width: float = 0.0):
    return {
        "iris_class": model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
    }