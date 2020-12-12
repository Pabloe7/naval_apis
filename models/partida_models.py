from pydantic import BaseModel


class PartidaIn(BaseModel):
    nombre: str
    value: int


class PartidaOut(BaseModel):
    id_partida: int
    nombre: str
    turnopropio: bool 
    fin: bool 
    