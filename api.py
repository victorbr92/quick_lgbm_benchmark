import lightgbm as lgb
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class PredictionInput(BaseModel):
    data: List[List[float]]

models = [lgb.Booster(model_file=f'model_{i}.txt') for i in range(4)]

@app.post("/predict/{variant}")
async def predict(variant: int, input_data: PredictionInput):
    data = np.array(input_data.data)
    predictions = models[variant].predict(data)
    return {"prediction": predictions.tolist()}
