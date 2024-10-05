from src.utils import get_key,get_value
import random

ENEMIGOS_SEGUN_NIVEL = ['Persona','Persona', 'Animal', 'Animal Artico', 'Hielo', 'Nieve', 'Gaseoso']
TIENDAS_SEGUN_NIVEL = ['BipBip FastFood','BipBip FastFood', 'ThaMart', 'Horus Pet Shop', 'Monguitown', 'TeaNah', 'Templo']
DESCRIPCIONES_SEGUN_NIVEL = ['Bienvenido','Te encuentras frente al puesto de una reconocida cadena de comidas. Recuerdas haber hecho un pedido, pero todavia no sabes donde esta tu hamburguesa. Todas las demas tiendas estan congeladas y los pasillos parecen estar cubiertos de una neblina espesa. Puede ser peligroso avanzar...',
                             'Luego de saltearte a la gente enloquecida por el hielo, encuentras un mercado local que parece tener de todo incluso cosas que no deberian existir. La puerta del Dojo ha sido descongelada, con tantos enemigos rondando puede serte util aprender unos movimientos',
                             'La tienda de mascotas parece haber sido descongelada, probablemente muchos de los animales que escaparon provenian de aqui. Pero que clase de animales exoticos eran?',
                             'Habiendo sobrevivido los horrores de aquella tienda, llegas a la pequeña Mongolia, donde tienen esa sopa que no puedes dejar pasar.',
                             'A tu paso, el hielo sigue retrocediendo, pero criaturas mas y mas extrañas aparecen en tu camino. Llegas al rincon mas recondito del Shopping, la cafeteria (o Teeria de moda) esta aqui.',
                             'Llegas al origen del problema. Vislumbras una salida y algo un local de lo mas extraño. Que hace un Templo en medio de un Shopping?']
FRASES_RANDOM = ["El invierno esta llegando","Hoy es un buen dia para dormir","¿De qué sirve el calor del verano, sin el frío del invierno para darle dulzura?","Una persona dice muchas cosas en verano que no tienen ningún significado en invierno.",
                 "Si el invierno llega, ¿Podrá la primavera estar tan lejos?","En invierno nos acurrucamos con un buen libro y soñamos alejados del frío.","El invierno está sobre mi cabeza pero en mi corazón hay una eterna primavera",
                 "La primavera del espíritu florece en invierno","Mantener un corazón cálido en invierno es la verdadera victoria.","En las profundidades del invierno finalmente aprendí que en mi interior habitaba un verano invencible",
                 "La gente no se da cuenta si es invierno o verano cuando están felices","Una palabra amable puede calentar tres meses de invierno","Los veranos vuelan siempre, los inviernos caminan.","La risa es el sol que ahuyenta el invierno del rostro humano.",
                 "Si no tuviéramos invierno, la primavera no resultaría tan agradable; si de vez en cuando no conociéramos la adversidad, la prosperidad no sería tan bienvenida.","La primavera, el verano y el otoño nos llenan de esperanza; Solo el invierno nos recuerda nuestra condición humana.",
                 "Es como si de alguna forma necesitáramos la oscuridad de los meses de invierno para reponer nuestro espíritu interior...","Necesito un cafe"]
# https://www.exitoysuperacionpersonal.com/frases-de-invierno/
OBJETOS = [{"Coco Cola":{"Vida":50}},{"Coco Cola":{"Vida":70}},{"Hambrosia":{"Vida":50,"Adquirir":"Fuego Sagrado"}},{"Bepis Max":{"Temperatura":-1,"Mana":50}},{"Calditos Mongoles":{"Temperatura":+3,"Vida":180}},
           {"Limon con Te":{"Estados":'Cura Todo',"Vida":150,"Temperatura":+3}},{"Verano en Polvo":{"Aprender":'Viento de Notos'}}]
DUMMY = {'nombre': 'Dummy', 'Clase': 'Dummy', 'Vida': 1, 'Ataques': [{ "Quedarse Quieto": {"Dam":0,"Efecto":"ninguno"} }], 'Habilidades': ['Ninguna']}
ATAQUES_DOJO = [{"Porrazo": {'Dam': 150, 'Efecto': 'ninguno'}},{"Golpe Doble": {'Dam': 200, 'Efecto': 'ninguno'}},{"Rompehuesos": {'Dam': 2000, 'Efecto': 'ninguno'}},
                {"Rompehielos": {'Dam': 1500, 'Efecto': 'fuego'}},{"Golpe Serio": {'Dam': 10000, 'Efecto': 'ninguno'}}]


# Borrar los prints de mas xx
# Agregar opcion de usar habilidad una vez por turno

# Agregar ataques a aprender - Fase 2
# Agregar habilidades a adquirir -  Fase 2
# Armar listado de estados Sangrado, resfrio, Hipotermia , Hipotermia Grave QUE HACEN?
class Nivel():
    def __init__(self):
        self.nombre = ""
        self.enemigos = []
        self.tiendas = []
        self.objetos = []
        self.submenu_activo = ""
        self.fase = 0
        self.descripcion = ""
        # Evalua si se usaron Habilidades, Objetos o se Visitaron tiendas H.O.T.D.
        self.acciones_usadas = [False,False,False,False]
        #Evalua si se activo el newgamemas
        self.mododificil = False

    def generar_nivel(self,dict,fase):
        #Genera un personaje dado un json
        self.fase = fase
        self.nombre = f"Nivel {self.fase}"
        self.tiendas.append(TIENDAS_SEGUN_NIVEL[fase])
        self.enemigos = self.generar_enemigos(dict)
        self.descripcion = DESCRIPCIONES_SEGUN_NIVEL[fase]
        self.acciones_usadas = [False, False, False,False]

    def generar_enemigos(self,dict):
        enemigos_del_nivel = []
        enemigos_dict = dict
        #filtrar enemigos
        enemigos_filtrados = [enemigo for enemigo in enemigos_dict if enemigo["Clase"] == ENEMIGOS_SEGUN_NIVEL[self.fase]]

        # Cantidad de enemigos maximos de un nivel, hacer funcion despues

        if not self.mododificil:
            if self.fase == 4:
                enemigos_x_nivel = 1
            elif self.fase > 4:
                enemigos_x_nivel = 2
            else:
                enemigos_x_nivel = 3
        else:
            if self.fase == 4:
                enemigos_x_nivel = 2
            else:
                enemigos_x_nivel = 4

        cantidad_enemigos = len(enemigos_filtrados)

        if enemigos_x_nivel > cantidad_enemigos:
            enemigos_del_nivel = enemigos_filtrados
        else:
            for i in range(enemigos_x_nivel):
                enemigos_del_nivel.append(enemigos_filtrados[i])
        if len(enemigos_filtrados) == 0:
            enemigos_del_nivel.append(DUMMY)
        return enemigos_del_nivel

    def limpiar_enemigos(self):
        nro = 0
        mensaje = ""
        for enemigo in self.enemigos:
            if enemigo["Vida"] <= 0:
                self.enemigos.pop(nro)
                nombre = enemigo["nombre"]
                mensaje += f' {nombre} ha muerto.'
                #Reinicio a Dummy
                if nombre == "Dummy":
                    DUMMY["Vida"] = 1
            nro += 1
        return mensaje

    def verificar_fin_batalla(self,personaje):
        fin = False
        if len(self.enemigos) == 0 or personaje.vida <= 0:
            if personaje.vida == 0:
                personaje.estados = ["Muerto"]
            fin = True
        return fin

    def display(self):
        display = ""
        return display

    def frase_aleatoria(self):
        frase = random.choice(FRASES_RANDOM)
        return frase

    def armar_menu_general(self, personaje):
        opciones = ["Ver Estadisticas"]
        tiendas_sin_visitar = self.tiendas
        if self.fase >= 2 and not self.acciones_usadas[3]:
            opciones.append("Visitar el Dojo Ofiuco Do")
        if len(self.tiendas) > 0 and not self.acciones_usadas[2]:
            opciones.append("Visitar una tienda")
        # REVISAR si conviene validar objetos   and not self.acciones_usadas[1]
        if len(personaje.objetos) > 0 :
            opciones.append("Usar objeto")
        if len(personaje.habilidades) > 0 and not self.acciones_usadas[0]:
            opciones.append("Usar habilidad")
        opciones.append("Avanzar de nivel")
        return opciones

    def armar_submenu(self,tipo_menu,personaje):
        menu = []
        if tipo_menu == "Usar objeto":
            for objeto in personaje.objetos:
                menu.append(objeto)
            self.submenu_activo = "objeto"
        elif tipo_menu == "Usar habilidad":
            for habilidad in personaje.habilidades:
                menu.append(habilidad)
            self.submenu_activo = "habilidad"
        elif tipo_menu == "Visitar una tienda":
            for tienda in self.tiendas:
                menu.append((tienda))
            self.submenu_activo = "tienda"
        elif tipo_menu == "Visitar el Dojo Ofiuco Do":
            ataque = ATAQUES_DOJO[self.fase-2]
            menu.append(ataque)
            self.submenu_activo = "dojo"
        else:
            pass
        return menu

    def armar_menu(self,menu_elegido,personaje):
        menu = []
        if menu_elegido == "Ver Estadisticas":
            menu = self.armar_menu_general(personaje)
        elif menu_elegido == "Avanzar de nivel":
            pass
        else:
            menu = self.armar_submenu(menu_elegido,personaje)
        return menu

    def visitar_tienda(self,nro_tienda,personaje):
        # por ahora las tiendas son una porqueria con un solo objeto
            nro = int(nro_tienda)
            personaje.obtener_objeto(OBJETOS[nro])
            # self.tiendas.pop(nro)

    def aplicar_cambios_por_menu(self,personaje,cambio):
        print(f"cambio{cambio} ")
        indice = int(cambio) - 1
        mensaje = ""
        if self.submenu_activo == "tienda":
            self.visitar_tienda(indice+1,personaje)
            self.acciones_usadas[2] = True
            objeto_comprado = get_key(OBJETOS[indice+1])
            mensaje = f"Has Visitado {TIENDAS_SEGUN_NIVEL[indice+1]}, compraste {objeto_comprado}!"
        elif self.submenu_activo == "objeto":
            objeto = personaje.objetos[indice]
            mensaje = personaje.usar_objeto(objeto,indice)
            self.acciones_usadas[1] = True
        elif self.submenu_activo == "habilidad":
            habilidad = personaje.habilidades[indice]
            personaje.usar_habilidad(habilidad)
            mensaje = f"Has usado {get_key(habilidad)}!"
            self.acciones_usadas[0] = True
        elif self.submenu_activo == "dojo":
            ataque = ATAQUES_DOJO[self.fase-2]
            personaje.aprender_ataques(ataque)
            personaje.cambiar_temperatura(1)
            mensaje = f"Luego de un duro entrenamiento, has aprendido {get_key(ataque)}!"
            self.acciones_usadas[3] = True
        self.submenu_activo = ""
        return mensaje

