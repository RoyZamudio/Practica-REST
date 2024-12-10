from fastapi import FastAPI, UploadFile, File, Form, Depends
from typing import Optional
from pydantic import BaseModel
import shutil
import os
import uuid
import orm.repo as repo #funciones para hacer consultas a la BD
from sqlalchemy.orm import Session
from orm.config import generador_sesion #generador de sesiones
import orm.esquemas as esquemas

# Creación del servidor
app = FastAPI()

@app.get("/")
def hola_mundo():
    print("invocando a ruta /")
    respuesta = {
        "mensaje": "hola mundo!"
    }

    return respuesta

# ---------- Peticiones a Alumnos ----------

# GET '/alumnos'
@app.get("/alumnos")
def lista_alumnos(sesion:Session=Depends(generador_sesion)):
    print("API consultando todos los alumnos")
    return repo.devuelve_alumnos(sesion)

# GET '/alumnos/{id}
@app.get("/alumnos/{id}")
def alumno_por_id(id ,sesion:Session=Depends(generador_sesion)):
    print("API consultando alumno por id")
    return repo.alumno_por_id(sesion, id)

#PUT
@app.put("/alumnos/{id}")
def actualiza_alumno(id:int, info_alumno:esquemas.AlumnoBase, sesion:Session=Depends(generador_sesion)):
    repo.actualiza_alumno(sesion, id, info_alumno)

# DELETE '/alumnos/{id}'
@app.delete("/alumnos/{id}")
def borrar_alumno(id:int, sesion:Session=Depends(generador_sesion)):
    # repo.borrar_calificaciones_por_id_alumno(sesion,id)
    # repo.borrar_fotos_por_id_alumno(sesion,id)
    repo.borra_alumno_por_id(sesion,id)
    return {"alumno_borrado", "ok"}

# ---------- Peticiones a Calificaciones ----------

# GET '/calificaciones'
@app.get("/calificaciones")
def lista_calificaciones(sesion:Session=Depends(generador_sesion)):
    print("API consultando todas las calificaciones")
    return repo.devuelve_calificaciones(sesion)

# GET '/calificaciones/{id}'
@app.get("/calificaciones/{id}")
def calificacion_por_id(id:int, sesion:Session=Depends(generador_sesion)):
    print("Buscando calificacion por id")
    return repo.calificacion_por_id(sesion, id)

# GET '/alumnos/{id}/calificaciones'
@app.get("/alumnos/{id}/calificaciones")
def calificaciones_por_id_alm(id:int,sesion:Session=Depends(generador_sesion)):
    print("API consultando calificaciones del alumno ", id)
    return repo.calificaciones_por_id_alumno(sesion, id)

@app.put("/calificaciones/{id}")
def actualiza_alumno(id:int, info_calificacion:esquemas.CalificacionBase, sesion:Session=Depends(generador_sesion)):
    repo.actualiza_calificacion(sesion, id, info_calificacion)

# DELETE '/alumnos/{id}/calificaciones'
@app.delete("/alumnos/{id}/calificaciones")
def borrar_calificaciones(id: int, sesion: Session = Depends(generador_sesion)):
    print(f"API eliminando calificaciones del alumno {id}")
    repo.borrar_calificaciones_por_id_alumno(sesion, id)
    return {"calificaciones_alumno_borradas", "ok"}

# ---------- Peticiones a Fotos ----------

# GET '/fotos'
@app.get("/fotos")
def lista_fotos(sesion:Session=Depends(generador_sesion)):
    print("API consultando todas las fotos")
    return repo.devuelve_fotos(sesion)

# GET '/fotos/{id}'
@app.get("/fotos/{id}")
def foto_por_id(id:int, sesion:Session=Depends(generador_sesion)):
    print("Buscando foto por id")
    return repo.foto_por_id(sesion,id)

# GET '/alumnos/{id}/fotos
@app.get("/alumnos/{id}/fotos")
def fotos_por_id_alm(id:int,sesion:Session=Depends(generador_sesion)):
    print("API consultando fotos del alumno ", id)
    return repo.fotos_por_id_alumno(sesion, id)

# PUT '/fotos/{id}'
@app.put("/fotos/{id}")
def actualiza_alumno(id:int, info_foto:esquemas.FotoBase, sesion:Session=Depends(generador_sesion)):
    repo.actualiza_foto(sesion, id, info_foto)

# DELETE '/alumnos/{id}/fotos'
def borrar_fotos(id: int, sesion: Session = Depends(generador_sesion)):
    print(f"API eliminando fotos del alumno {id}")
    repo.borrar_fotos_por_id_alumno(sesion, id)
    return {"fotos_alumno_borradas", "ok"}