
from fastapi import FastAPI
from models.user import User
from db.user_db import set_user, database_users

from models.ingresos import Ingresos
from db.ingre_db import set_ingresos, database_ingresos


api = FastAPI()

@api.post("/users")
def saveUser(user: User):
    set_user(user)
    return database_users


@api.post("/ingresos")

def saveIngresos(ingresos: Ingresos):
    set_ingresos(ingresos)
    return database_ingresos
