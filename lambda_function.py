import joblib
import json

model = joblib.load("model.joblib")

def handler(event, context):
    if event["httpMethod"] == "POST" and event["body"]:
        body = json.loads(event["body"])
        prediction = {
            "iris_class": model.predict([[body["sepal_length"], body["sepal_width"], body["petal_length"], body["petal_width"]]])[0]
        }
        return {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps(prediction)
        }
    else:
        return {
            "statusCode": 400,
            "body": "Invalid Request"
        }
    