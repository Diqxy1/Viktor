# Viktor API

## Requirements

install the virtual machine in the main folder
- Windowns
```
python -m venv .venv
```
- Linux
```
python3 -m venv venv
```
- Then install the dependencies
```
pip install -r requirements.txt
```

## Clone this repository

```
https://github.com/hardcode-express/MEGASONHO-API.git
```

## Start the server

- Windowns
```
python runserver.py
```
- Linux
```
python3 runserver.py
```

## Some Commands

- Create Migration
-> alembic -c migrations/alembic.ini revision -m "migration name"
- Run Migration
-> alembic -c migrations/alembic.ini upgrade head
- History migration
-> alembic -c migrations/alembic.ini history
