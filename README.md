# mi-INTS-db-backend

The backend for serving mi-INTS-db data.

## Development

This project will be using python virtual envs.

```
cd mi-INTS-db-backend
source env/bin/activate
```

This activates the virtual env and dependencies can now be installed local to the repository.

```
pip install -r requirements.txt
```

Write the absolute filepaths to your local minor intron data and minor intron coordinate files inside of the .env file. 

To run the backend server in development mode:

```
uvicorn main:app --reload
```
