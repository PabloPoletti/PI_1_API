#coding: utf-8
from sqlalchemy import Column, Float, Integer, Table, String
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine




t_circuits2 = Table(
    'circuits2', meta,
    Column('circuitId', Integer),
    Column('name', String),
    Column('location', String),
    Column('country', String)
)


t_constructors = Table(
    'constructors', meta,
    Column('constructorId', Integer),
    Column('name', String),
    Column('nationality', String)
)


t_drivers = Table(
    'drivers', meta,
    Column('driverId', Integer),
    Column('driverRef', String),
    Column('code', String),
    Column('nationality', String)
)


t_races2 = Table(
    'races2', meta,
    Column('raceId', Integer),
    Column('year', Integer),
    Column('round', Integer),
    Column('circuitId', Integer),
    Column('name', String)
)


t_results = Table(
    'results', meta,
    Column('resultId', Integer),
    Column('raceId', Integer),
    Column('driverId', Integer),
    Column('constructorId', Integer),
    Column('grid', Integer),
    Column('positionOrder', Integer),
    Column('points', Float),
    Column('laps', Integer),
    Column('statusId', Integer)
)
meta.create_all(engine)