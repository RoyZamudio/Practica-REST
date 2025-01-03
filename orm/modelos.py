from orm.config import BaseClass
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Float
import datetime

# Clase Alumno
class Alumno(BaseClass):
    __tablename__="alumnos"
    id=Column(Integer, primary_key=True)
    nombre=Column(String(100))
    edad=Column(Integer)
    domicilio=Column(String(100))
    carrera=Column(String(100))
    trimestre=Column(String(100))
    email=Column(String(100), unique=True)
    password=Column(String(100))
    fecha_registro=Column(DateTime(timezone=True),default=datetime.datetime.now)

# Clase Calificaciones
class Calificacion(BaseClass):
    __tablename__="calificaciones"
    id=Column(Integer, primary_key=True)
    id_alumno=Column(Integer, ForeignKey(Alumno.id))
    uea=Column(String(100))
    calificacion=Column(String(100))

# Clase Fotos
class Foto(BaseClass):
    __tablename__="fotos"
    id=Column(Integer, primary_key=True)
    id_alumno=Column(Integer, ForeignKey(Alumno.id))
    titulo=Column(String(100))
    descripcion=Column(String(100))
    ruta=Column(String(50))