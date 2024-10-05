from flask import Flask, render_template,request
from src.personajes import Personaje
import json
import random
from src.nivel import Nivel

VITAMINA_D_NECESARIA = 15
nivel_global = 5
fase = 0
app = Flask(__name__)

def generar_juego():
    objetos = []
    # with open("..\CardGenerator\static\json\juego.json", "r") as arch:
    with open(r"C:\Users\NAVI\Desktop\pruebas\Python\Propios\CardGenerator\static\json\juego.json", "r") as arch:
        json_archivo = json.load(arch)
        personajes =json_archivo["personajes"]
        enemigos =json_archivo["enemigos"]
        # Por ahora no se usan
        objetos =json_archivo["objetos"]
        secretos =json_archivo["secretos"]

    protagonista = random.choice(personajes)
    panteon = enemigos
    items = random.sample(objetos,3)

    juego = []
    juego.append(protagonista)
    juego.append(panteon)
    juego.append(items)
    juego.append(secretos)
    return juego

def crear_progonista(dict_prota):
    protagonista = Personaje()
    protagonista.generar_personaje(dict_prota)
    return protagonista

def calcular_valor(ataque,propiedad):
    valor = list(ataque[0].values())[0][propiedad]
    return valor

# REVISAR EN DESUSO
# def simular_combate(combatiente1,combatiente2):
#     ataquesc1 = combatiente1["Ataques"]
#     ataquesc2 = combatiente2["Ataques"]
#     # buscar_mejor_ataque
#     dam1 = calcular_valor(ataquesc1,"Dam")
#     efecto1 =calcular_valor(ataquesc1,"Efecto")
#     dam2 = calcular_valor(ataquesc2,"Dam")
#     efecto2 =calcular_valor(ataquesc2,"Efecto")
#     print(dam1)
#     print(efecto1)
#     print(ataquesc2)
#     print(combatiente1["vida"])
#     combatiente1["vida"] -= dam2
#     combatiente2["vida"] -= dam1
#     print(combatiente1["vida"])

# Renderear la pagina
@app.route('/')
def logo():
    return render_template("logo.html")

@app.route('/intro')
def intro():
    global protagonista
    global nivel
    if protagonista.vida <=0:
        print("RESETEANDO")
        protagonista = crear_progonista(random.choice(personajes_secretos))
        juego = generar_juego()
        protagonista = crear_progonista(juego[0])
        grupo_enemigos = juego[1]
        nivel.__init__()
        nivel.generar_nivel(grupo_enemigos, 1)
    return render_template("intro.html")
    # return html_cards

@app.route("/winter", methods=["GET", "POST"])
def winter():
    eleccion = "Ver Estadisticas"
    nombre = nivel.nombre
    display = nivel.descripcion
    bolufrase = nivel.frase_aleatoria()
    menu = nivel.armar_menu_general(protagonista)
    protagonista.display()
    return render_template("winter.html", display=display,frase=bolufrase,nombre=nombre, menu=menu,personaje=protagonista, eleccion=eleccion,submenu = False)

@app.route("/winter/<opt>")
def accion(opt):
    nombre = f"{nivel.nombre}"
    eleccion = opt
    display = "Puedo visitar las tiendas Disponibles... La mayoria estan cubiertas de nieve... A Cual deberia ir?"
    bolufrase = nivel.frase_aleatoria()
    menu = nivel.armar_menu(opt,protagonista)
    return render_template("winter.html", display=display,frase=bolufrase,nombre=nombre, menu=menu, personaje=protagonista, eleccion=eleccion,submenu = True )

# Con esta funcion uso las cosas
@app.route("/personaje/<opt>")
def usar_algo(opt):
    titulo = nivel.submenu_activo
    if titulo == "tienda" or titulo == "dojo":
        titulo = titulo.capitalize()
    else:
        titulo = "Has utilizado " + nivel.submenu_activo.capitalize()
    mensaje = nivel.aplicar_cambios_por_menu(protagonista,opt)
    return render_template("personaje.html", personaje=protagonista, titulo=titulo ,accion_realizada=mensaje )

@app.route("/batalla")
def batalla():
    # nivel.display_enemigos()
    display_batalla = "Enemigos Salvajes Atacan!!!"
    enemigos_nivel = nivel.enemigos
    return render_template("batalla.html",display=display_batalla, personaje=protagonista, enemigos=enemigos_nivel,fin=False )

@app.route("/batalla/<ataque>")
def batalla1(ataque):
    display_batalla = ""
    fase = nivel.fase
    imbuido_en_mana = False
    if ataque == '999':
        int_atk = int(len(protagonista.ataques))-1
        protagonista.mana = 0
        imbuido_en_mana = True
    else:
        int_atk = int(ataque) -1
    enemigos_nivel = nivel.enemigos
    ataque_elegido = list(protagonista.ataques.keys())[int_atk]
    ataque_elegido_efec = protagonista.ataques[ataque_elegido]["Efecto"]

    danio_atk = list(protagonista.ataques.values())[int_atk]["Dam"]
    enemigo_a_atacar = protagonista.enemigo_enfocado
    protagonista.atacar(enemigo_a_atacar,ataque_elegido,imbuido_en_mana)
    display_batalla += f" {protagonista.nombre} ataca con {ataque_elegido} "
    if imbuido_en_mana:
        display_batalla += "usando todo su mana"
        danio_atk = danio_atk * 2
    display_batalla += f" , causa {danio_atk} de daño"
    display_batalla += ". \n"
    #Por ahora todos los enemigos atacan iguales y hacen el mismo ataque
    for enemigo in enemigos_nivel:
        ataque_enemigo = enemigo["Ataques"][0]
        #REVISAR Mandar a una funcion
        #Poder de Winter
        if enemigo == protagonista.enemigo_enfocado and ataque_elegido_efec == "Hielo" and (enemigo["Clase"] != "Hielo" or enemigo["Clase"] != "Nieve" or enemigo["Clase"] != "AguaNieve" or enemigo["Clase"] != "Gaseoso"):
            display_batalla += f" {enemigo['nombre']} esta congelado, no puede moverse. " + '\n'
        else:
            #descomponer ataque enemigo para el display
            for key, value in ataque_enemigo.items():
                nombre_ataque = key
                danio = value['Dam']
                efecto = ""
                if value['Efecto'] != 'ninguno':
                    efecto += f", causa {value['Efecto']}"
                efecto += "."
            protagonista.recibir_ataque(ataque_enemigo)
            display_batalla += f" {enemigo['nombre']} usa {nombre_ataque}. Recibes {danio} de daño {efecto} " + '\n'

    display_batalla += nivel.limpiar_enemigos()
    display_batalla += protagonista.verificar_temperatura()
    fin_combate = nivel.verificar_fin_batalla(protagonista)
    print(fin_combate)
    display_batalla += protagonista.aplicar_estados()
    muerto = False
    if protagonista.vida <= 0:
        muerto = True
    if fin_combate:
        if not muerto:
            fase += 1
            print(f"NUEVA FASE {fase}")
            if fase < 7:
                nivel.generar_nivel(grupo_enemigos, fase)
            else:
                pass
        else:
            fase = 1
            nivel.__init__()
            nivel.generar_nivel(grupo_enemigos, fase)
        # agregar a Jack Frost y mas historia, pasar fase a 7
    if fase < 7 and not muerto:
        return render_template("batalla.html",display=display_batalla, personaje=protagonista, enemigos=enemigos_nivel, fin=fin_combate )
    elif muerto:
         return render_template("batalla.html",display=display_batalla, personaje=protagonista, enemigos=enemigos_nivel, fin=fin_combate )
    else:
        return render_template("finale.html")

@app.route("/ataques/<enemy>")
def atacar(enemy):
    enemy_int = int(enemy) -1
    enemigos_nivel = nivel.enemigos
    protagonista.enemigo_enfocado = enemigos_nivel[enemy_int]
    return render_template("ataques.html", personaje=protagonista, enemigos=enemigos_nivel  )

@app.route("/newgame")
def newgamemas():
    global protagonista
    protagonista = crear_progonista(random.choice(personajes_secretos))
    juego = generar_juego()
    grupo_enemigos = juego[1]
    nivel.__init__()
    nivel.mododificil = True
    nivel.generar_nivel(grupo_enemigos, 1)
    return render_template("newgame.html", personaje=protagonista  )

#### EMPIEZA EL PROGRAMA ORIGINAL ###
card = {}
cant_objetos = 10
cant_personajes = 5
cant_criaturas = 9
html_cards = ""

juego = generar_juego()
nivel = Nivel()

#REVISAR  son variables para pasar info entre paginas
# tipo del submenu a modificar
tipo_submenu = ""

protagonista = crear_progonista(juego[0])
grupo_enemigos = juego[1]
Objetos_comprables = juego[2]
personajes_secretos = juego[3]

print(personajes_secretos)
# Genera los niveles del 1
fase = 1
nivel.generar_nivel(grupo_enemigos, 1)
if __name__ == "__main__":
    app.run(debug=False)




