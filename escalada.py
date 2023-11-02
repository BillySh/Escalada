#Escalada 

import numpy as np
import random
from sorting_techniques import pysort

# Creating the Sort Object
sortObj = pysort.Sorting()

#----------------------------------------------
class EscaladaT:
  def __init__(self, id,utilidad, actividad, conclusion):
    self.id = id
    self.utilidad = utilidad
    self.actividad= actividad
    self.conclusion = conclusion


    def __str__(self):
        return f"Object {self.id}: Utilidad={self.utilidad}, Actividad={self.actividad}, Conclusion={self.conclusion}"

    def __repr__(self):
        return str(self)
        

#----------------------------------------------

N = 7
utilidades = np.random.rand(N)
actividades = np.random.rand(N)
conclusion = np.random.rand(N)



def main():
  Objetos = []

  for objeto in range(N):
        id = objeto + 1
        utilidad = random.randint(1, 100)
        actividad = random.randint(1, 100)
        conclusion = random.randint(1, 100)
        
        obj = EscaladaT( id, utilidad, actividad, conclusion)
        Objetos.append(obj)

  sortResult = sortObj.heapSort(Objetos)
  for obj in sortResult:
        print(obj)





if __name__ == "__main__":
    main()
    





# Performing Insertion Sort

