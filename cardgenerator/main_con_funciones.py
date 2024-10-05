from flask import Flask, render_template
from src.cards import Personaje
import json
import random


ROPAS = ["Remera","Pantalon", "Sweater", "Buzo", "Campera", "Tunica"]
ADJETIVOS = ["Fabulosa","Bella", "Ancestral", "Futuristica", "Brillante", "Legendaria"]
NOMBRES = ["Jonathan","Joseph", "Jotaro", "Josuke", "Giorno", "Jolyne","Joshua","Jorge","Diego","William","Cesar","Trevor"]
APELLIDOS = ["Joestar","Kujo", "Higashikata", "Giovanna", "Brando", "Zepelli","Belmont",]
PROFESIONES = ["Arqueologo","Desempleado", "Estudiante", "Mafioso", "Abogado", "Empresario","Guardaespaldas","Policia","Preparador Fisico"]
TEMPERATURA_FIEBRE = 40
TEMPERATURA_DEFENSAS = 33
VITAMINA_D_NECESARIA = 15
nivel_global = 7

def generar_objetos(cant):
    objetos = []
    with open("static/json/conceptos.json", "r") as archconceptos:
        conceptos = json.load(archconceptos)
    for c in range(1,cant):
        objeto = {}

        cant_atributos = round(nivel_global / 5) + 1
        atributos = []
        for i in range(cant_atributos):
            atributo = []
            concepto = random.choice(list(conceptos.items()))
            # concepto[0] El objeto, los datos
            # print(concepto[0])
            cant_att = random.randint(1, concepto[1]["Max"]) * concepto[1]["Escala"]
            atributo.append(concepto[0])
            atributo.append(str(cant_att))
            atributos.append(atributo)
        objeto["atributos"] = atributos
        # card_cant_att = random.randint(1, card_att["Max"]) * card_att["Escala"]
        tipo_ropa = random.choice(ROPAS)
        adjetivo = random.choice(ADJETIVOS)
        objeto["title"] = adjetivo + " " +  tipo_ropa + " de " + atributo[0]
        objeto["type"] = "Objeto - " + tipo_ropa
        # objeto["att"] = f"{card_att['nombre']}"
        # objeto["qty"] = card_cant_att
        # print(card["att"])
        objeto["cost"] = random.randint(1,500)
        objetos.append(objeto)
    return objetos
# country, capital = random.choice(list(d.items()))

#Sacar este metodo de aca
#Pasar a clases
def crear_protagonista(clase):
    # "Summer": {
    #     "Vida_minima": 1000,
    #     "Vida_maxima": 10000,
    #     "Habilidad": ["Subir 1 Grado"],
    #     "Ataques": [{"Palazo": 10, "Lanzallamas": 10000}]
    # }
    protagonista = {}
    protagonista["nombre"] = "Summer Olivia Smith"
    protagonista["vida"] = random.randint(clase["Vida_minima"], clase["Vida_maxima"])
    protagonista["habilidad"] = clase["Habilidad"]
    protagonista["ataques"] = clase["Ataques"]
    print(protagonista["ataques"])
    return protagonista



def generar_personajes():
    aliados = []
    with open("static/json/clases.json", "r") as archclases:
        clases = json.load(archclases)
    for i in range(3):
        aliade = {}
        profesion = random.choice(PROFESIONES)
        aliade["nombre"] = random.choice(NOMBRES) + " " + random.choice(APELLIDOS) + " - " + "Profesion: " + profesion
        # print(random.choice(NOMBRES) + " " + random.choice(APELLIDOS) + " - " + "Profesion: " + profesion)
        aliade["ataques"] = clases[profesion]['Ataques']
        aliade["habilidad"] = clases[profesion]['Habilidad']
        aliade["vida"] = random.randint(clases[profesion]["Vida_minima"], clases[profesion]["Vida_maxima"])
        print(aliade["ataques"])
        # print(aliade["ataques"].values))
        aliados.append(aliade)
    #Sacar este metodo de aca
    summer = crear_protagonista(clases["Summer"])
    aliados.append(summer)
    return aliados

def generar_criaturas():
    criatura = {}
    try:
        with open("static/json/criaturas.json", "r") as arch:
            # Leo los datos guardados
            datos = json.load(arch)
            # Actualizo los datos viejos con el nuevo ingreso
            # datos.update(nuevo_ingreso)
    except FileNotFoundError:
        pass
        # datos = nuevo_ingreso
    finally:
        enemigogral = datos["Persona"]
        criatura["nombre"] = "Bicho"
        criatura["vida"] = random.randint(enemigogral["Vida_minima"], enemigogral["Vida_maxima"])
        criatura["ataques"] = random.choice(enemigogral["Ataques"])
        criatura["habilidades"] = enemigogral["Habilidad"]
        # loot = random.choice(enemigogral["Loot"])
    # print(random.choice(NOMBRES) + " " + random.choice(APELLIDOS) + " - " + "Profesion: " + random.choice(PROFESIONES))
    # print(criatura)
    return criatura

object_deck = []
creature_deck = []
allies_deck = []
card = {}
cant = 10
html_cards = ""

object_deck = generar_objetos(cant)
allies_deck = generar_personajes()
#Cambiar urgente
creature_deck.append(generar_criaturas())
print(creature_deck)




# print(object_deck)



#__name es una libreria especial de
app = Flask(__name__)
# print(__name__)
num = random.randint(0,9)

#funcion decoradora
@app.route('/')
def hello_world():
    return render_template("card.html", cards=object_deck, ally_cards=allies_deck,c_cards=creature_deck )
    # return html_cards


if __name__ == "__main__":
    app.run(debug=True)
