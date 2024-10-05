from flask import Flask, render_template
from src.cards import Personaje
import json
import random

#Agregar la funcion de costo

ROPAS = ["Remera","Pantalon", "Sweater", "Buzo", "Campera", "Tunica"]
ADJETIVOS = ["Fabulosa","Bella", "Ancestral", "Futuristica", "Brillante", "Legendaria","Surrealista","Bizarro","Irreal","Ancestral","Polemico","Berserker"]
NOMBRES = ["Jonathan","Joseph", "Jotaro", "Josuke", "Giorno", "Jolyne","Joshua","Jorge","Diego","William","Cesar","Trevor"]
APELLIDOS = ["Joestar","Kujo", "Higashikata", "Giovanna", "Brando", "Zepelli","Belmont","Sandiego"]
PROFESIONES = ["Arqueologo","Desempleado", "Estudiante", "Mafioso", "Abogado", "Empresario","Guardaespaldas","Policia","Preparador Fisico"]

nivel_global = 5

def generar_objetos(cant):
    objetos = []
    with open("static/json/conceptos.json", "r") as archconceptos:
        conceptos = json.load(archconceptos)
        lista_conceptos = list(conceptos.items())
    for c in range(1,cant):
        objeto = {}
        cant_atributos = round(nivel_global / 5) + 1
        atributos = []
        concepto_ant = ""
        for i in range(cant_atributos):
            atributo = []
            #Esta linea lista los tipos de conceptos que existen y elige uno
            concepto = random.choice(lista_conceptos)
            # Esto para que no repita un concepto
            while concepto == concepto_ant:
                concepto = random.choice(lista_conceptos)
            # concepto[0] El objeto, los datos

            # REVISAR ESTA CUENTA, Problema del cero
            cant_escala = round(random.randint(1, concepto[1]["Max"]) / concepto[1]["Escala"])
            if cant_escala == 0:
                cant_escala =1
            cant_att = cant_escala * concepto[1]["Escala"]
            atributo.append(concepto[0])
            atributo.append(str(cant_att))
            atributos.append(atributo)
            concepto_ant = concepto
        objeto["atributos"] = atributos
        tipo_ropa = random.choice(ROPAS)
        adjetivo = random.choice(ADJETIVOS)
        objeto["title"] = adjetivo + " " +  tipo_ropa + " de " + atributo[0]
        objeto["type"] = "Objeto - " + tipo_ropa
        objeto["cost"] = random.randint(1,500)
        objetos.append(objeto)

    return objetos

#Sacar este metodo de aca
#Pasar a clases
def crear_protagonista(clase,nro):
    protagonista = {}
    #Revisar, poner algo para identificar a summer
    if nro == 1:
        protagonista["nombre"] = "Summer Olivia Smith"
    else:
        protagonista["nombre"] = "Winter Wendy Walker"
    protagonista["Clase"] = "Elegida"
    protagonista["Vida"] = random.randint(clase["Vida_minima"], clase["Vida_maxima"])
    protagonista["Habilidades"] = clase["Habilidades"]
    protagonista["Ataques"] = clase["Ataques"]
    return protagonista



def generar_personajes(cant_personajes):
    aliados = []
    with open("static/json/clases.json", "r") as archclases:
        clases = json.load(archclases)
    for i in range(cant_personajes):
        aliade = {}
        #REVISAR, esto deberia cambiarlo a que a traves de las llaves te haga un random de la profesion
        #El problema es que te puede llegar a generar una mascota o un protagonista
        profesion = random.choice(PROFESIONES)
        aliade["nombre"] = random.choice(NOMBRES) + " " + random.choice(APELLIDOS)
        aliade["Clase"] = profesion
        aliade["Ataques"] = clases[profesion]['Ataques']
        aliade["Habilidades"] = clases[profesion]['Habilidades']
        aliade["Vida"] = random.randint(clases[profesion]["Vida_minima"], clases[profesion]["Vida_maxima"])
        aliados.append(aliade)
    return aliados

def generar_secretos():
    secretos = []
    with open("static/json/clases.json", "r") as archclases:
        clases = json.load(archclases)
    summer = crear_protagonista(clases["Summer"],1)
    winter = crear_protagonista(clases["Winter"],2)
    secretos.append(summer)
    secretos.append(winter)
    return secretos

def generar_criaturas(cant_criaturas):
    criaturas = []
    try:
        with open("static/json/criaturas.json", "r") as arch:
            # Leo los datos guardados
            tipos_criaturas = json.load(arch)
            # print(" Datos")
            # print(list(tipos_criaturas.keys()))
            #Lista los tipos de criaturas
            listado_tipos = list(tipos_criaturas.keys())

            # print(listado_tipos)
            # Actualizo los datos viejos con el nuevo ingreso
            # datos.update(nuevo_ingreso)
    except FileNotFoundError:
        pass
        # datos = nuevo_ingreso
    finally:
        for j in range(cant_criaturas):
            criatura = {}
            #Elijo un enemigo al azar
            tipo_criatura = random.choice(listado_tipos)
            enemigo_a_generar = tipos_criaturas[tipo_criatura]
            criatura["nombre"] = tipo_criatura + " " + random.choice(ADJETIVOS)
            criatura["Clase"] = tipo_criatura
            criatura["Vida"] = random.randint(enemigo_a_generar["Vida_minima"], enemigo_a_generar["Vida_maxima"])
            criatura["Ataques"] = [random.choice(enemigo_a_generar["Ataques"])]
            print(criatura["Ataques"])
            criatura["Habilidades"] = enemigo_a_generar["Habilidades"]
            criaturas.append(criatura)
        # loot = random.choice(enemigo_a_generar["Loot"])
    return criaturas

def crear_juegos(personajes,enemigos,objetos,secretos):
    juego = {}
    juego["personajes"]=personajes
    juego["enemigos"]=enemigos
    juego["objetos"]=objetos
    juego["secretos"]=secretos
    with open("static/json/juego.json", "w") as arch:
        # el dump inserta el primer campo en el archivo del 2do campo, se puede identar para que sea mas legible
        json.dump(juego, arch, indent=4)
    # with open("C:/Users/NAVI/Desktop/pruebas/Python/Propios/wintercome/static/json", "w") as arch:
    #     # el dump inserta el primer campo en el archivo del 2do campo, se puede identar para que sea mas legible
    #     json.dump(juego, arch, indent=4)


object_deck = []
creature_deck = []
allies_deck = []
card = {}
cant_objetos = 10
cant_personajes = 9
cant_criaturas = 20
html_cards = ""

object_deck = generar_objetos(cant_objetos)
allies_deck = generar_personajes(cant_personajes)
creature_deck = generar_criaturas(cant_criaturas)
secret_deck = generar_secretos()

# Agregar grabar JSON
crear_juegos(allies_deck,creature_deck,object_deck,secret_deck)

#__name es una libreria especial de
app = Flask(__name__)
num = random.randint(0,9)

#funcion decoradora
@app.route('/')
def hello_world():
    return render_template("card.html", cards=object_deck, ally_cards=allies_deck,c_cards=creature_deck )
    # return html_cards
@app.route('/magic')
def magic_cards():
    return render_template("magic.html",cards=object_deck, ally_cards=allies_deck,c_cards=creature_deck)

if __name__ == "__main__":
    app.run(debug=False)
