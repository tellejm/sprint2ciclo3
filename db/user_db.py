from typing import Dict
from pydantic import BaseModel
class UserInDB(BaseModel):
    username: str
    password: str
    nombre:str
    apellido:str
    correo:str
    ciudad:str
    edad:str
    estrato:str
    ocupacion:str
    estado_civil:str
    numero_hijos:str

database_users = Dict[str, UserInDB]
database_users = {
    "JavierFV": UserInDB(**{"username":"JavierFV",
                            "password":"root",
                            "nombre":"Javier",
                            "apellido":"Villamizar",
                            "correo":"javierfer_1998@hotmail.com",
                            "ciudad":"Bucaramanga",
                            "edad":"22",
                            "estrato":"3",
                            "ocupacion":"empleado",
                            "estado_civil":"soltero",
                            "numero_hijos":"0"}),
    "Alvarado5": UserInDB(**{"username":"Alvarado5",
                            "password":"hola",
                            "nombre":"Alvaro",
                            "apellido":"Alvarado",
                            "correo":"alvaalva@hotmail.com",
                            "ciudad":"Bogota",
                            "edad":"26",
                            "estrato":"4",
                            "ocupacion":"empleado",
                            "estado_civil":"casado",
                            "numero_hijos":"2"}),
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None
def update_user(user_in_db: UserInDB,contrasena_in_db: UserInDB,
                nombre_in_db : UserInDB,apellido_in_db: UserInDB,
                correo_in_db : UserInDB,ciudad_in_db : UserInDB,
                edad_in_db : UserInDB,estrato_in_db: UserInDB,
                ocupacion_in_db: UserInDB,estado_civil_in_db: UserInDB,
                numero_hijos_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    database_users[contrasena_in_db.password] = contrasena_in_db
    database_users[nombre_in_db.nombre] = nombre_in_db
    database_users[apellido_in_db.apellido] = apellido_in_db
    database_users[correo_in_db.correo] = correo_in_db
    database_users[ciudad_in_db.ciudad] = ciudad_in_db
    database_users[edad_in_db.edad] = edad_in_db
    database_users[estrato_in_db.estrato] = estrato_in_db
    database_users[ocupacion_in_db.ocupacion] = ocupacion_in_db
    database_users[estado_civil_in_db.estado_civil] = estado_civil_in_db
    database_users[numero_hijos_in_db.numero_hijos] = numero_hijos_in_db
    return user_in_db