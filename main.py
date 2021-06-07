import os
import pandas as pd
from typing import List, Optional
from fastapi import FastAPI, Query, HTTPException

# load mi-INTS-db data into a pandas dataframe
df = pd.read_excel(os.environ['MI_INTS_DB_FILE'], engine='openpyxl')

app = FastAPI()

@app.get('/')
def lookup(gene: str, columns: Optional[List[str]] = Query(None)):
  # standard lookup using first 10 columns of gene data
  if columns == None:
    data = df.loc[df['Gene_name'] == gene].iloc[:, :10]

    if data.empty:
      raise HTTPException(status_code=404, detail='Gene not found')

    return data.to_dict('records')
  # advanced lookup using specified columns of gene data
  else:
    data = df.loc[df['Gene_name'] == gene].filter(items=columns)

    if data.empty:
      raise HTTPException(status_code=404, detail='Gene not found')

    return data.to_dict('records')
