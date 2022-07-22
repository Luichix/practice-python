from datetime import time, timedelta, datetime
from horario import leer, actualizar

datos = leer()
retorno = []

for h in datos:

    t1 = time.fromisoformat(h[1])
    t2 = time.fromisoformat(h[2])
    e = datetime.combine(datetime.min, t1) - datetime.min
    s = datetime.combine(datetime.min, t2) - datetime.min
    i = h[0]

    tiempo = s - e

    retorno.append((str(tiempo), i))


actualizar(retorno)
