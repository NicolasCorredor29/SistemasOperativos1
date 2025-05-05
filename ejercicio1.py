
from random import *
import time
import threading
l=[]

def insertarFifo(proceso):
    l.append(proceso)
    

def finalizarProceso(prioridad):
    del l[len(l)-1]
    print(f"Finalizó el proceso {prioridad}")

def funcionGeneral(proceso,prioridad):
    insertarFifo(proceso)
    finalizarProceso(prioridad)

for i in range(5):

    proceso=threading.Thread(target=funcionGeneral,args=(f"proceso_{i}",i),name=f"proceso{i}")
    proceso.start()
    time.sleep(randint(3,6))