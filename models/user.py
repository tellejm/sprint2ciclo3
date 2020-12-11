from pydantic import BaseModel

class User(BaseModel):
    name:str
    passw:str
    email:str
    username:str