#from datetime import datetime
from pydantic import BaseModel
import random

class PartidaInDB(BaseModel):
	

    id_partida: int = 0
    nombre: str
    tableroenemigo: str = "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    tableropropio: str ="000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    turnopropio: bool = random.choice([False,True])
    fin: bool = False


    
database_partidas = []
generator = {"id":0}
def save_partida(partida_in_db: partidaInDB):
    generator["id"] = generator["id"] + 1
    partida_in_db.id_partida = generator["id"]
    database_partidas.append(partida_in_db)
    return partida_in_db

def update_partida(partida_in_db: PartidaInDB):
    database_partidas[partida_in_db.usuarioname] = partida_in_db
    return partida_in_db