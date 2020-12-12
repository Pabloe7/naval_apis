from typing import  Dict
from pydantic import BaseModel

class UsuarioInDB(BaseModel):
    nombre: str
    mejorpuntaje: int
    ultimopuntaje: int



database_usuarios= Dict[str, UsuarioInDB]

database_usuarios = {
    "Pablo": UsuarioInDB(**{"nombre":"Pablo", 
                            "mejorpuntaje":1000, 
                            "ultimopuntaje":100}),

    "Pedrito": UsuarioInDB(**{"nombre":"Pedrito", 
                            "mejorpuntaje":1300, 
                            "ultimopuntaje":40}),}


def get_usuario(usuarioname: str):
    if nombre in database_usuarios.keys():
        return database_usuarios[nombre]
    else: 
        return None
    
def update_usuario(usuario_in_db: usuarioInDB):
    database_usuarios[usuario_in_db.nombre] = usuario_in_db
    return usuario_in_db


