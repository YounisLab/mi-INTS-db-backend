import os
import ast
import pandas as pd
from dotenv import load_dotenv
from typing import List, Optional
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# load environment variables from .env file
load_dotenv()

# load mi-INTS-db data into a pandas dataframe
db_df = pd.read_excel(os.environ['MI_INTS_DB_FILE'], engine='openpyxl')
coord_df = pd.read_excel(os.environ['MI_INTS_COORDS_FILE'], engine='openpyxl')

app = FastAPI()

frontend_origin = 'http://localhost:3000'

app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_origin],
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get('/gene')
def gene_lookup(gene: str, cols: Optional[List[str]] = Query(None)):
    # standard lookup using default columns of gene data
    if cols == None:
      default_cols = [
        'Gene_name',
        'Gene_Aliases',
        'Chromosome',
        'Gene_start',
        'Gene_end',
        'Strand',
        'Transcript_IDs',
        'Longest_Transcript',
        'longest_transcript',
        'Protein_ID',
        'MI_number'
      ]
      data = db_df.loc[db_df['Gene_name'] == gene].filter(items=default_cols)
        
      if data.empty:
        raise HTTPException(status_code=404, detail='Gene not found')
          
      return data.to_dict('records')
    # advanced lookup using specified columns of gene data
    else:
      data = db_df.loc[db_df['Gene_name'] == gene].filter(items=cols)

      if data.empty:
        raise HTTPException(status_code=404, detail='Gene not found')

      return data.to_dict('records')

@app.get('/coordinates')
def coord_lookup(gene: str):
    # lookup and parse data
    data = coord_df.loc[coord_df['gene'] == gene]
    data['exon_coords'] = data['exon_coords'].str.strip('[]')
    data['intron_coords'] = data['intron_coords'].str.strip('[]')

    if data.empty:
      raise HTTPException(status_code=404, detail='Gene not found')
    else:
      return data.to_dict('records')
