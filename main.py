
from db.usuario_db import UsuarioInDB
from db.usuario_db import update_usuario, get_usuario
from db.partida_db import PartidsaInDB
from db.partida_db import update_partida
from models.usuario_models import UsuarioIn, UsuarioOut
from models.partida_models import PartidaIn, PartidaOut

from fastapi import FastAPI, HTTPException

api = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost", 
    "http://localhost:8080",
    "https://naval-apis.herokuapp.com" #TODO Actualizar el Heroku
]
api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)


@api.post("/usuario/auth/")
async def auth_usuario(usuario_in: UserIn):
    
    usuario_in_db = get_usuario(usuario_in.nombre)

    if usuario_in_db == None:
        return{"Autentificado": True,"Mensaje": "Cuenta creada...En desarrollo"}
    
    else:
        return {"Autentificado": True,"Mensaje": "Bienvenido...De nuevo"}

    


'''
@api.get("/usuario/balance/{username}")
async def get_balance(username: str):
    
    user_in_db = get_user(username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    
    user_out = UserOut(**user_in_db.dict())

    return  user_out



@api.put("/user/transaction/")
async def make_transaction(transaction_in: TransactionIn):
    
    user_in_db = get_user(transaction_in.username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    
    if user_in_db.balance < transaction_in.value:
        raise HTTPException(status_code=400, detail="No se tienen los fondos suficientes")

    user_in_db.balance = user_in_db.balance - transaction_in.value
    update_user(user_in_db)

    transaction_in_db = TransactionInDB(**transaction_in.dict(), actual_balance = user_in_db.balance)
    transaction_in_db = save_transaction(transaction_in_db)

    transaction_out = TransactionOut(**transaction_in_db.dict())

    return  transaction_out
    
'''
