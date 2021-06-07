import os
import pandas as pd
from typing import List, Optional
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# load mi-INTS-db data into a pandas dataframe
df = pd.read_excel(os.environ['MI_INTS_DB_FILE'], engine='openpyxl')

app = FastAPI()

frontend_origin = 'http://localhost:3000'

app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_origin],
    allow_methods=["*"],
    allow_headers=["*"],
)


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
