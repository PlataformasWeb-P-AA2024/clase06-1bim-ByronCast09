from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from crear_base import Docente

from configuracion import engine

Session = sessionmaker(bind=engine) #conectada  ala coneccion
session = Session()

# Obtener todos los registros de
# la entidad docentes
docentes = session.query(Docente).all() # [docente1, docente2, docente3] saca una lista de objetos que se crearon
# select * es parecido
# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Presentación de todos los Docentes")
for s in docentes:
    print("%s-%s" % (s.nombre,s.ciudad))
    print("---------")

# Obtener todos los registros de
# la tabla docentes que tengan como valor en
# el atributo especifico
docentes_dos = session.query(Docente).filter(Docente.ciudad=="Loja").all()
print(docentes_dos)
