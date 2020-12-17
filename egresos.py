from fastapi import APIRouter, HTTPException

from db.egre_db import EgresoInDb, database_egresos, set_egreso
from models.egresos import Egresos

router = APIRouter()

@router.post("/egresos")
def saveEgresos(egresos: Egresos):
    set_egreso(egresos)
    return database_egresos

@router.get('/egresos/{username}')
def get_egresos(username: str): 
    egresos = {}
    for i in database_egresos:
        if database_egresos[i].username == username:
            egresos[i] = database_egresos[i]
    return egresos

@router.delete('/egresos/{Idegresos}')
def delete_egreso(Idegresos: int):
    try:
        print(database_egresos[Idegresos])
        del database_egresos[Idegresos]
        return database_egresos, {"Usuario " + Idegresos + " Eliminado"}
    
    except:
        raise HTTPException(status_code=404, detail="Egreso no encontrado")