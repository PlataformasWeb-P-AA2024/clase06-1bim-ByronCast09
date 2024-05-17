from sqlalchemy.orm import sessionmaker

from crear_base import Saludo #importante
from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session() # parecido al cursor que me ayuda crear, y guardar ademas de consultas

# se crea un objeto de tipo
# Saludo

miSaludo = Saludo()# viene de crear_base.py, Saludo es la clase que creé
miSaludo.mensaje = "Hola que tal"
miSaludo.tipo = "informal"

miSaludo2 = Saludo()
miSaludo2.mensaje = "Buenas tardes"
miSaludo2.tipo = "formal"


# se agrega el objeto miSaludo
# a la entidad Saludo a la sesión
# a la espera de un commit
# para agregar un registro a la base de
# datos demobase.db
session.add(miSaludo)
session.add(miSaludo2)

# se confirma las transacciones
session.commit()
