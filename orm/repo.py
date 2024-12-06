import orm.modelos as modelos
from sqlalchemy.orm import Session
from sqlalchemy import and_

# ---------- Peticiones a Alumnos ----------

# SELECT * FROM  app.alumnos
# GET '/alumnos'
def devuelve_alumnos(sesion:Session):
    print("SELECT * FROM  app.alumnos")
    return sesion.query(modelos.Alumno).all()

# SELECT * FROM app.alumnos WHERE id={id_al}
# GET '/alumnos/{id}'
def alumno_por_id(sesion:Session, id_al:int):
    print("SELECT * FROM app.alumnos WHERE id={id_al}", id_al)
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id==id_al).first()

# DELETE FROM app.alumnos WHERE id_alumno={id_al}
# DELETE '/alumnos/{id}'
def borra_alumno_por_id(sesion:Session, id_al:int):
    print("DELETE FROM app.alumnos WHERE id_alumno={id_al}")
    alm = alumno_por_id(sesion, id_al)
    if alm is not None:
        sesion.delete(alm)
        sesion.commit()
    respuesta = {
        "mensaje":"alumno eliminado"
    }
    return respuesta

# ---------- Peticiones a Calificaciones ----------

# SELECT * FROM app.calificaciones
# GET '/calificaciones'
def devuelve_calificaciones(sesion:Session):
    print("SELECT * FROM  app.calificaciones")
    return sesion.query(modelos.Calificacion).all()

# SELECT * FROM app.calificaciones WHERE id={id_cal}
# GET '/calificaciones/{id}'
def calificacion_por_id(sesion:Session, id_cal:int):
    print("SELECT * FROM app.calificaciones WHERE id={id_cal}", id_cal)
    return sesion.query(modelos.Calificacion).filer(modelos.Calificacion.id==id_cal).first()

# SELECT * FROM app.calificaciones WHERE id_alumno={id_al}
# GET '/alumnos/{id}/calificaciones'
def calificaciones_por_id_alumno(sesion:Session, id_al:int):
    print("SELECT * FROM app.calificaciones WHERE id_alumno={id_al}", id_al)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id_alumno==id_al).all()

# DELETE FROM app.calificaciones WHERE id_alumno={id_al}
# DELETE '/alumnos/{id}/calificaciones'
def borrar_calificaciones_por_id_alumno(sesion:Session,id_al:int):
    print("DELETE FROM app.calificaciones WHERE id_alumno={id_al}",id_al)
    cal_alm = calificaciones_por_id_alumno(sesion, id_al)
    if cal_alm is not None:
        for calificacion_alumno in cal_alm:
            sesion.delete(calificacion_alumno)
        sesion.commit()

# ---------- Peticiones a Fotos ----------

# SELECT * FROM app.fotos
# GET '/fotos'
def devuelve_fotos(sesion:Session):
    print("SELECT * FROM app.fotos")
    return sesion.query(modelos.Foto).all()

# SELECT * FROM app.fotos WHERE id={id_fo}
# GET '/fotos/{id}'
def foto_por_id(sesion:Session, id_fo:int):
    print("SELECT * FROM app.fotos WHERE id={id_fo}", id_fo)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id==id_fo).first()

# SELECT * FROM app.fotos WHERE id_alumnos={id_al}
# GET '/alumnos/{id}/fotos
def fotos_por_id_alumno(sesion:Session,id_al:int):
    print("SELECT * FROM app.fotos WHERE id_alumnos={id_al}", id_al)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_alumno==id_al).all()

# DELETE FROM app.fotos WHERE id_alumno={id_al}
# DELETE '/alumnos/{id}/fotos'
def borrar_fotos_por_id_alumno(sesion:Session,id_al:int):
    print("DELETE FROM app.fotos WHERE id_alumno={id_al}",id_al)
    fotos_alm = fotos_por_id_alumno(sesion, id_al)
    if fotos_alm is not None:
        for foto_alumno in fotos_alm:
            sesion.delete(foto_alumno)
        sesion.commit()