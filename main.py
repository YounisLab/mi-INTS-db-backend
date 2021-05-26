import os
import pandas as pd
from fastapi import FastAPI

# Load mi-INTS-db data into a pandas dataframe
df = pd.read_excel(os.environ['MI_INTS_DB_FILE'], engine='openpyxl')

app = FastAPI()

@app.get("/")
def read_root():
  return "Hello, I serve mi-INTS-db data!"
