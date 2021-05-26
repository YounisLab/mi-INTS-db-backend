# mi-INTS-db-backend

The backend for serving mi-INTS-db data.

## Development

We will be using python virtual envs.

```
cd mi-INTS-db-backend
python3 -m venv env
source env/bin/activate
```

This activates the virtual env and dependencies can now be installed local to the repository.

```
pip install -r requirements.txt
```

To run the backend server in development mode:

```
uvicorn main:app --reload
```
