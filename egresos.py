from fastapi import APIRouter, HTTPException

from db.egre_db import EgresoInDb, database_egresos, get_user_egresos, set_egreso
from models.egresos import Egresos

router = APIRouter()

@router.post("/egresos")
def saveEgresos(egresos: Egresos):
    set_egreso(egresos)
    return database_egresos

@router.get('/egresos/{username}')
def get_egresos(username: str): 
    egresos = {}
    n = 0
    for i in database_egresos:
        if database_egresos[i].username == username:
            egresos[n] = database_egresos[i]
            n+=1
    return egresos
    
