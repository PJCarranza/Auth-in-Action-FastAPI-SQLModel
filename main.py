from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel
app = FastAPI()
class User(SQLModel):
    username: str
    password: str
db_users = [
    User(username="john", password="secret"),
    User(username="pepe", password="123"),
    User(username="ana", password="abc")
]
def encotra_usua(username: str):
    for user in db_users:
        if user.username == username:
            return user
    return None
@app.post("/login")
def login(user: User):
    db_user = encotra_usua(user.username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    if db_user.password != user.password:
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")
    return {"message": f"Bienvenido {user.username}"}