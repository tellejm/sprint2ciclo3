# ---------------------------------- Import usuario
from db.user_db import UserInDB
from typing import Dict
from db.user_db import update_user, get_user, database_users, verificador
from models.user_models import UserIn, UserOut

# -------------------------------------import formulario preguntas
from db.user_q_db import User
from models.user import User
from db.user_q_db import database_users_q, get_user_q, set_user_q

#--------------------------------------

import datetime
from fastapi import FastAPI
from fastapi import HTTPException
api = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080",
]

#----------------------------------- Consultas usuario
api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

@api.get("/",)
def inicio():
    return "Pagina de inicio"

@api.get("/users/all/", response_model=Dict[str, UserInDB])
async def get_users():
    return database_users

@api.post("/users/user/data/create/{username}")      
async def update_user(username: str, user_in_db: UserInDB):
    user_in_db2 = verificador(username) 
    if user_in_db2 == None:
        database_users[username] = user_in_db
        return user_in_db
    return {"Usuario ya existe"}
    # return database_users[username]
    

@api.post("/users/user/auth/")
async def auth_user(user_in: UserIn):
    user_in_db = get_user(user_in.username)
    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    if user_in_db.password != user_in.password:
        return {"Autenticado": False}
    return {"Autenticado correctamente"}

@api.get("/users/user/data/{username}")
async def get_balance(username: str):
    user_in_db = get_user(username)
    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())
    return user_out

@api.put("/users/user/data/update/{username}")      
async def update_user(username: str, user_in_db: UserInDB):
    
    try:
        database_users[username] = user_in_db
        return database_users[username]
    
    except:
        raise HTTPException(status_code=404, detail="No existe el usuario")
        
    
    return user_in_db

@api.delete("/users/user/delete/{username}")
async def delete_user(username: str):
    
    try:
        del database_users[username]
        return database_users, {"Usuario " + username + " Eliminado"}
    
    except:
        raise HTTPException(status_code=404, detail="Usuario no existe")
        
#------------------------------------------ Consultas formulario preguntas
@api.get("/users/question/", response_model=Dict[str, User])
async def get_q_user():
    return database_users_q


@api.post("/users/question/crear/")      
def savequestion(user:User):
    set_user_q(user)
    return "Gracias por su colaboracion"
#-------------------------------------------



