from models.user import User
from typing import Dict



database_users = Dict[str,User]

database_users = {

    "Jhon": User(**{
                     "name":"Michael",
                     "passw":"root1",
                     "email":"ing@gmail.co",
                     "username":"Jhon"  })
                        ,

   "Ana": User(**{
                    "name":"Oscar",
                    "passw":"root1",
                    "email":"ing@gmail.co",
                    "username":"Ana"  }), 
                                                                        

}

def get_user(username:str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def set_user(user_in_db: User):
    database_users[user_in_db.username] = user_in_db
    return user_in_db 