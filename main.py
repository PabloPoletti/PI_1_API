from fastapi import FastAPI
from fastapi import APIRouter
from config.db import conn
from models.models import t_drivers,t_races2, t_results,t_constructors,t_circuits2
from sqlalchemy import  select, func, desc , or_ , and_
import uvicorn

app = FastAPI()

@app.get('/races')
def get_races():
    return conn.execute(select(func.count(t_races2.c.raceId).label('Cantidad_de_Carreras'),
    t_races2.c.year).group_by(t_races2.c.year).order_by(desc('Cantidad_de_Carreras'))).first()

@app.get('/Piloto')
def get_Piloto():
    return conn.execute(select(t_results.c.driverId, t_drivers.c.driverRef.label('Piloto'),
        func.count(t_results.c.positionOrder).label('Cantida_de_Primeros_Puestos')).
        join(t_drivers, t_results.c.driverId==t_drivers.c.driverId).where(t_results.c.positionOrder==1).
        group_by(t_results.c.driverId).order_by(desc('Cantida_de_Primeros_Puestos'))).first()

@app.get('/Circuito')
def get_Circuito():
    return conn.execute(select(func.count(t_races2.c.circuitId), t_races2.c.name).
    group_by(t_races2.c.circuitId).order_by(desc(func.count(t_races2.c.circuitId)))).first()



@app.get('/MejorPiloto')
def get_MejorPiloto():
    return conn.execute(select(func.sum(t_results.c.points).label('Puntos'), t_drivers.c.driverRef.label('Piloto')).
        join(t_drivers, t_results.c.driverId==t_drivers.c.driverId).
        join(t_constructors, t_results.c.constructorId==t_constructors.c.constructorId).
        where(or_(t_constructors.c.nationality=='British',t_constructors.c.nationality=='American')).
        group_by(t_results.c.driverId).order_by(desc('Puntos'))).first()
