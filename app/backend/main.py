from fastapi import FastAPI
import joblib
import numpy as np
import xgboost as xgb
import pickle
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score, f1_score
import pandas as pd

# Load the iris dataset
# Initialize FastAPI app
app = FastAPI()

# Load the trained model 
# with open("RandomForestClassifiermodel.pkl", "rb") as file:
#     model = pickle.load(file) 

with open("RandomForestClassifierpipeline2.pkl", "rb") as file1:
    pipeline = pickle.load(file1)

# pipeline = Pipeline(steps=[
#             ("preprocessor", preprocessor),
#             ("classifier", model)
#         ])
# Define FastAPI endpoints
@app.get("/")
async def read_root():
    return {"message": "Welcome to the model API!"}

@app.post("/predict/")
async def predict_species(data: dict):
    # Implement your prediction logic here using the loaded model
    features = np.array(data['features']).reshape(1, -1)
    cols = ['age', 'workclass', 'fnlwgt', 'education', 'education_num',
       'marital_status', 'occupation', 'relationship', 'race', 'sex',
       'capital_gain', 'capital_loss', 'hours_per_week', 'native_country']
    df = pd.DataFrame(features, columns=cols)
    prediction = pipeline.predict(df)
    class_name = ["<=50", ">50"]
    return {"class": class_name[int(prediction)]}