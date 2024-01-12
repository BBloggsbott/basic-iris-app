from pandas import read_csv
import joblib
from sklearn.svm import SVC
# Load dataset

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)

# Split-out validation dataset
array = dataset.values
X = array[:,0:4]
y = array[:,4]

# Make predictions on validation dataset
model = SVC(gamma='auto')
model.fit(X, y)

# with open("model.joblib", "w+") as model_file:
joblib.dump(model, "model.joblib")