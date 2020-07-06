import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import click

from model import Request, Offer

"""

-- Database structure

CREATE TABLE medication_request
(
    ID  SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    mobile VARCHAR(15) NOT NULL,
    city VARCHAR(20) NOT NULL,
    requirement text NOT NULL
);


CREATE TABLE medication_offer
(
    ID  SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    mobile VARCHAR(15) NOT NULL,
    city VARCHAR(20) NOT NULL,
    offer text NOT NULL
);

"""

# SAMPLE_DIR = 'sample'
# SAMPLE_REQUESTS_FILE = 'Форма для тех, кому что-то нужно (Ответы) - Ответы на форму.csv'
# SAMPLE_OFFERS_FILE = 'Форма для тех, кто может что-то дать (Ответы) - Ответы на форму.csv'


def reader(file):
    with open(file, encoding='utf8') as f:
        reader = csv.reader(f)
        next(reader)  # We do not need header, so let's skip it
        yield from reader


def request_mapper(row):
    return Request(name=row[1],
                   mobile=row[2],
                   city=row[3],
                   requirement=row[4])


def offer_mapper(row):
    return Offer(name=row[1],
                 mobile=row[2],
                 city=row[3],
                 offer=row[4])


dedupe_objs = {}


def deduplicate(objects):
    for obj in objects:
        dedupe_objs[obj.mobile] = obj
    yield from dedupe_objs.values()
    dedupe_objs.clear()


@click.command()
@click.option('--create-db/--no-create-db', default=False, help="Will try to create database before writing")
@click.option('--db-uri', help="Database URI. Example: postgresql://scott:tiger@localhost:5432/mydatabase",
              default="sqlite:///:memory:")
@click.argument('requests')
@click.argument('offers')
def parse(requests, offers, create_db, db_uri):
    """Simple program that migrates requests and offers data from CSV file to database"""

    engine = create_engine(db_uri)

    if create_db:
        from model import Base
        Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()

    request_rows = reader(requests)
    request_objects = map(request_mapper, request_rows)

    offer_rows = reader(offers)
    offer_objects = map(offer_mapper, offer_rows)

    for obj in deduplicate(request_objects):
        session.add(obj)

    for obj in deduplicate(offer_objects):
        session.add(obj)

    session.commit()

    click.echo("Migration complete!")
    click.echo(f"Requests: {session.query(Request).count()}")
    click.echo(f"Offers: {session.query(Offer).count()}")


if __name__ == '__main__':
    parse()
