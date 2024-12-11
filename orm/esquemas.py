from pydantic import BaseModel

#Esquema alumno
class AlumnoBase(BaseModel):
    nombre:str
    edad:int
    domicilio:str
    carrera:str
    trimestre:str
    email:str
    password:str

 #Esquema calificaciones   
class CalificacionBase(BaseModel):
    uea:str
    calificacion:str

#Esquema foto
class FotoBase(BaseModel):
    titulo:str
    descripcion:str
    ruta:str