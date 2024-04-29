from fastapi import FastAPI, HTTPException
from InputData import InputData
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the model and scaler
with open("/media/moraa/New Volume/Ontita/10Academy/Cohort B/Projects/Week1/User_Analytics_in_the_telecommunication_Industry/artifacts/models/kmeans_model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

# Function to standardize numerical values
def standardize_numerical_values(df):
    """
    Standardize numerical values using StandardScaler.
    """
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

@app.get("/")
async def root():
    return {"message": "Welcome to my FastAPI application!"}

@app.get("/predict/")
async def get_predict():
    return {"message": "Send a POST request to this endpoint with data to get predictions."}

@app.post("/predict/")
async def predict(data: InputData):
    try:
        # Convert input data to DataFrame
        input_data = pd.DataFrame([data.dict()])

        # Standardize input data
        input_data = standardize_numerical_values(input_data)

        # Extract features from the standardized data
        features = input_data.values

        # Make predictions
        prediction = model.predict(features)

        return {"prediction": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)