from pydantic import BaseModel
class UserIn(BaseModel):
    username: str
    password: str
class UserOut(BaseModel):
    username: str
    nombre:str
    apellido:str
    correo:str
    ciudad:str
    edad:str
    estrato:str
    ocupacion:str
    estado_civil:str
    numero_hijos:str