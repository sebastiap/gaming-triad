from src.utils import get_key
# todo list :

TEMPERATURA_FIEBRE = 40
TEMPERATURA_DEFENSAS = 33
VITAMINA_D_NECESARIA = 15

efecto_antigaseoso = "Temperatura a 0"
ATAQUE = {"Viento de Notos":{"Dam":0,"Efecto":efecto_antigaseoso}}
HABILIDAD = {"Fuego Sagrado":{"Temperatura":1}}

def get_key(dict):
    key = list(dict[0])
    return key

class Personaje():
    def __init__(self):
        self.nombre = ""
        self.profesion = ""
        self.estados = []
        #Las habilidades por ahora son lista pero deberian ser dict
        self.habilidades = []
        # Los ataques no son repetibles son un dict
        self.ataques = {}
        # Como un objeto es repetible tiene sentido que sea una lista
        self.objetos = [{"Papas Congeladas":{"Vida":100,"Temperatura":-2}}]
        #Cambiar por Icor,por ahora no hace nada
        self.mana = 0
        self.defensa = 0
        self.temperatura = 36
        self.plata = 0
        # Es para evaluar a que enemigo ataco por defecto.
        self.enemigo_enfocado = {}

    def generar_personaje(self,dict):
        #Genera un personaje dado un json
        self.nombre = dict["nombre"]
        self.ataques = dict["Ataques"][0]
        print(f"ataques {self.ataques}")
        #Solo test
        # self.ataques.update({"Pelazo": {'Dam': 10000, 'Efecto': 'ninguno'}})
        self.habilidades = dict["Habilidades"]

        self.profesion = dict["Clase"]
        self.vida = dict["Vida"]
        self.vida_max = dict["Vida"]

    def reset(self):
        self.vida = self.vida_max
        self.temperatura = 36

    def display_ataques(self):
        # print(list(self.ataques.keys()))
        Lista_ataques = list(self.ataques.keys())
        nro_ataque = 1
        for ataque in Lista_ataques:
            # print(f"{nro_ataque} - {ataque}")
            nro_ataque += 1
        opcion = 1000
        while opcion >= len(Lista_ataques):
            opcion = int(input("Selecciona una opcion:")) - 1
        if opcion < nro_ataque:
            ataque_elegido = Lista_ataques[opcion]
        return ataque_elegido

    # Metodos de estados

    def verificar_estado(self,estado):
        #Verificar si tengo estado
        tengoestado = False
        for estados in self.estados:
            if estados == estado:
                tengoestado = True
        return tengoestado

    def obtener_estado(self,estado):
        #Agrego el estado si no lo tengo
        if not self.verificar_estado(estado):
            self.estados.append(estado)

    def aplicar_estados(self):
        # REVISAR por ahora los estados son solo una palabra y el juego los interpreta
        mensaje = ""
        for estados in self.estados:
            if estados == "Sangrado":
                self.aplicar_sangrado()
                mensaje = "Tu herida esta sangrando. Pierdes 10 puntas de vida."
            if estados == "Hipotermia":
                mensaje = "Tu temperatura corporal ha bajado dramaticamente. Tus sentidos empiezan a nublarse."
            if estados == "Hipotermia Grave":
                mensaje = "Sientes que te desvaneces. Te cuesta mantenerte en pie"

        return mensaje
        #mas estados

    # Metodos de habilidad
    def aprender_habilidad(self,habilidad):
        agregar = True
        for hab in self.habilidades:
            if hab == habilidad:
                agregar = False
        if agregar:
            self.habilidades.append(habilidad)
        # self.habilidades[0].update()

    def usar_habilidad(self,habilidad):
        #Lee la habilidad y la interpreta para ejecutarla
        for atrib in habilidad.values():
            for concepto, cantidad in atrib.items():
                #Revisar , agregar mas habilidades
                if concepto == "Temperatura":
                    self.cambiar_temperatura(cantidad)

    # Metodos de objetos
    def obtener_objeto(self,objeto):
        self.objetos.append(objeto)

    def usar_objeto(self,objeto,num):
        mensaje = ""
        for atrib in objeto.values():
            for concepto, cantidad in atrib.items():
                # Cambiar if por algo mas serio
                if concepto == "Vida":
                    self.ganar_vida(cantidad)
                    mensaje += f"Recuperas {cantidad} de {concepto}."
                elif concepto == "Mana":
                    self.mana += cantidad
                    mensaje += f"Recuperas {cantidad} de {concepto}."
                elif concepto == "Temperatura":
                    self.cambiar_temperatura(cantidad)
                    mensaje += f"Tu {concepto} cambia en {cantidad} grados."
                elif concepto == "Estados":
                    #Aplicar curaciones
                    if cantidad == "Cura Todo":
                        self.estados = []
                        mensaje += "Se han curado todos tus estados alterados."
                elif concepto == "Aprender":
                    self.aprender_ataques(cantidad)
                    mensaje += f"{self.nombre} ha aprendido {cantidad}."
                elif concepto == "Adquirir":
                    #Cambiar por habiliades
                    mensaje += f"{self.nombre} ha adquirido la habilidad {cantidad}."
                    # Generalizar para aprender habilidades
                    self.aprender_habilidad(HABILIDAD)
        # Ver como sacar objetos
        self.objetos.pop(int(num))
        return mensaje

    # Metodos de cambios de salud
    def ganar_vida(self, cantidad):
        nueva_vida = self.vida + cantidad
        if (nueva_vida) > self.vida_max:
            self.vida = self.vida_max
        else:
            self.vida = nueva_vida

    def cambiar_temperatura(self,temperatura):
        #Evalua si sos uno de los elegidos p sino te cambia normalmente
        if self.nombre == "Summer Olivia Smith":
            self.temperatura += temperatura * 1.5
        elif self.nombre == "Winter Wendy Walker":
            self.temperatura = 36
        else:
            self.temperatura += temperatura

    def verificar_temperatura(self):
        mensaje = "Tu temperatura se mantiene en niveles normales."
        if self.temperatura <= 20:
            self.vida = 0
            mensaje = "Tu temperatura ha bajado abruptamente. Tu cuerpo colapsa."
        elif self.temperatura < 30 and not self.verificar_estado("Hipotermia Grave"):
            mensaje = "Tu temperatura sigue bajando. Tienes hipotermia grave."
            self.obtener_estado("Hipotermia Grave")
        elif self.temperatura < 32  and not self.verificar_estado("Hipotermia"):
            mensaje = "Tu temperatura sigue bajando. Tienes hipotermia."
            self.obtener_estado("Hipotermia")
        elif self.temperatura < 35 and not self.verificar_estado("Resfrio"):
            mensaje = "Tu temperatura baja. Te has resfriado."
            self.obtener_estado("Resfrio")
        return mensaje

    def aplicar_sangrado(self):
        self.vida -= 10

    # Metodos de Combate
    def aprender_ataques(self,ataque):
        #REVISAR PARA SACAR ATAQUES DE UNA BASE DE ATAQUES
        # ataque_aprendido = get
        if ataque == "Viento de Notos":
            self.ataques.update(ATAQUE)
        else:
            self.ataques.update(ataque)

    def atacar(self,enemigo,ataque,mana):
        danio = self.ataques[ataque]["Dam"]
        if mana:
            danio = danio * 2
        efecto = self.ataques[ataque]["Efecto"]
        danio_cambiado = False
        for habilidad in enemigo["Habilidades"]:
            if habilidad == "Resistencia al DaÃ±o Fisico" or habilidad == "Inmunidad al DaÃ±o Fisico":
                danio_cambiado = True
        # El fuego tiene prioridad al danio cambiado.
        #REVISAR imprimir ataques de fuego.
        if efecto == "fuego" and (enemigo["Clase"] == "Nieve" or enemigo["Clase"] == "Hielo"):
            danio = danio * 2
            danio_cambiado = False
        if danio_cambiado:
            if habilidad == "Resistencia al DaÃ±o Fisico":
                enemigo["Vida"] -= danio/2
            elif habilidad == "Inmunidad al DaÃ±o Fisico":
                if efecto == efecto_antigaseoso:
                    enemigo["Vida"] = 0
        else:
            enemigo["Vida"] -= danio

    def recibir_ataque(self,ataque):
        for value in ataque.values():
            danio = value["Dam"]
            efecto = value["Efecto"]
        self.vida -= danio - self.defensa
        if efecto != "ninguno":
            if efecto == "Sangrado":
                self.obtener_estado("Sangrado")
                self.cambiar_temperatura(-1)
            if efecto == "Congelar":
                self.cambiar_temperatura(-2)
            if efecto == "Helar":
                self.cambiar_temperatura(-3)

