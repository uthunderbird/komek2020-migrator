# Komek2020 migration utility

## Installation

You need Python 3.6+. Install one.

1. Prepare virtualenv to wrap script:
`python3 -m venv komek2020-migration`
2. Activate your venv:
`source komek2020-migration/bin/activate`
3. Install requirements:
`pip install -r requirements.txt`
4. You're gorgeous!

NOTE:

You can read more about venv [here](https://docs.python.org/3.6/tutorial/venv.html).
Especially about how to use it in Windows.

## Usage

In your venv, run:

`python migrate.py`.

You will see some helpful info about how to use the script.

Typical usage does look like this:
`python migrate.py "sample\\Форма для тех, кому что-то нужно (Ответы) - 
Ответы на форму.csv" "sample\Форма для тех, кто может что-то дать (Ответы) - 
Ответы на форму.csv" --db-uri postgresql://scott:tiger@localhost:5432/mydatabase`

WARNING: Do not use sample data in your production inventory. The script is extremely
simple, so it can do nothing but write data from CSV again and again.

So you should use the script ONLY FOR INITIAL MIGRATION.

If you screwed up something in your production environment, just drop database and 
try again.