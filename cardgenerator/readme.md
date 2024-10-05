Archivos Json

Objetos
Se forman en base a "Conceptos" del json de conceptos.
EJ:
  "Concepto": {
    "escala": 50,
    "max": 1000,
    "costo_unitario": 1,
    "contrario": "Estilo"
  }
Referencias
-----------
Escala: significa la unidad minima en la que suma ese concepto para un objeto.
Max: es el valor maximo el cual puede otorgar un objeto.
costo_unitario: es el costo en moneda que cuesta un objeto por cada unidad de atributo que suma dicho objeto.
contrario: significa el concepto que es opuesto a este concepto. En el caso de no haber opuesto, aqui ira el mismo concepto.


Clases y Criaturas
Los personajes y las criaturas se forman en base a clases o tipos de criaturas
Ej:
  "Clase": {
    "Vida_minima": 100,
    "Vida_maxima": 300,
    "Habilidad": ["Ninguna"],
    "Ataques": [{ "Palazo": 10 }]
  },
Vida minima y maxima son los limites minimo y maximo que puede tener ese personaje o criatura.
habilidad es el conjunto de habilidades que puede tener una persona
ataques es el conjunto de ataques que puede tener una persona