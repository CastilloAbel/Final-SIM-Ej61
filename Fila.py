from EtapaFundido import EtapaFundido
from EtapaForjado import EtapaForjado
from EtapaEnfriado import EtapaEnfriado
from EtapaTerminado import EtapaTerminado
from Pieza import Pieza
import random
class Fila:
    def __init__(self, id=0, reloj=0.0, eventos=[], etapa_fundido=EtapaFundido(), etapa_forjado=EtapaForjado(), etapa_enfriado=EtapaEnfriado(), etapa_terminado=EtapaTerminado(), objetos=[]) -> None:
        self.id = id
        self.reloj = reloj
        self.eventos = eventos
        self.etapa_fundido = etapa_fundido
        self.etapa_forjado = etapa_forjado
        self.etapa_enfriado = etapa_enfriado
        self.etapa_terminado = etapa_terminado
        self.objetos = objetos

    def get_objetos(self)->list:
        return self.objetos
    
    def set_objetos(self, obj):
        self.objetos = obj

    def distribucion_uniforme(self, rnd, inf, sup):
        return inf + (sup - inf) * rnd
    
    def llegada_pieza(self, rnd_llegada_pieza,prob_llegada_uno, prob_llegada_dos, prob_llegada_tres, prob_llegada_cuatro):
        if rnd_llegada_pieza < prob_llegada_uno:
            return 1
        elif prob_llegada_uno <= rnd_llegada_pieza < prob_llegada_uno + prob_llegada_dos:
            return 2
        elif prob_llegada_uno + prob_llegada_dos <= rnd_llegada_pieza < prob_llegada_uno + prob_llegada_dos + prob_llegada_tres:
            return 3
        else:
            return 4

    def simular(self, datos):
        [tiempo_total, prob_llegada_uno, prob_llegada_dos, prob_llegada_tres, prob_llegada_cuatro,
                 fin_fundido_inf, fin_fundido_sup, fin_forjado_inf, fin_forjado_sup, fin_enfriado, 
                 fin_terminado_inf, fin_terminado_sup] = datos
        
        if self.reloj == 0:
            self.nombre_evento = "Inicializacion"
            rnd_llegada_pieza = random.random()
            llegada_pieza = self.llegada_pieza(rnd_llegada_pieza, prob_llegada_uno, prob_llegada_dos, prob_llegada_tres, prob_llegada_cuatro)

            self.eventos = [[rnd_llegada_pieza, llegada_pieza, self.reloj + llegada_pieza], 
                            [None, None, None], [None, None, None], [None, None, None], [None, None, None]]
            reloj = min((evento[2] for evento in self.eventos if evento[2] is not None), default=None)
            return [reloj, self.eventos, self.etapa_fundido, self.etapa_forjado, self.etapa_enfriado, self.etapa_terminado, []]
        else:
            self.reloj = min((evento[2] for evento in self.eventos if evento[2] is not None), default=None)

            #llegada_pieza
            if self.reloj == self.eventos[0][2]:
                self.nombre_evento = "Llegada_pieza"
                rnd_llegada_pieza = random.random()
                llegada_pieza = self.llegada_pieza(rnd_llegada_pieza, prob_llegada_uno, prob_llegada_dos, prob_llegada_tres, prob_llegada_cuatro)

                self.eventos = [[rnd_llegada_pieza, llegada_pieza, self.reloj + llegada_pieza], 
                                self.eventos[1], self.eventos[2],self.eventos[3],self.eventos[4]]
                # Si la etapa de fundicion esta ocupada
                if self.etapa_fundido.get_estado():
                    pieza = Pieza(self.reloj , "Esperando Fundir")
                    cola = self.etapa_fundido.get_cola()
                    cola.append(pieza)
                    self.etapa_fundido.set_cola(cola)
                # Si la etapa de fundicion esta libre
                else:
                    pieza = Pieza(self.reloj , "Fundiendo")
                    self.etapa_fundido.set_estado(True)
                    rnd_fin_fundido = random.random()
                    tiempo_fundido = self.distribucion_uniforme(rnd_fin_fundido, fin_fundido_inf, fin_fundido_sup)
                    self.eventos = [self.eventos[0], 
                                [rnd_fin_fundido, tiempo_fundido, self.reloj + tiempo_fundido], self.eventos[2],self.eventos[3],self.eventos[4]]
                obj = self.get_objetos()
                obj.append(pieza)
                self.set_objetos(obj)
            #fin_fundicion
            elif self.reloj == self.eventos[1][2]:
                self.nombre_evento = "Fin_fundicion"
                cola = self.etapa_fundido.get_cola()
                if len(cola) > 0:
                    pieza = cola.pop(0)
                    self.etapa_fundido.set_estado(True)
                    rnd_fin_fundido = random.random()
                    tiempo_fundido = self.distribucion_uniforme(rnd_fin_fundido, fin_fundido_inf, fin_fundido_sup)
                    self.eventos = [self.eventos[0], 
                                [rnd_fin_fundido, tiempo_fundido, self.reloj + tiempo_fundido], self.eventos[2],self.eventos[3],self.eventos[4]]
                    obj = self.get_objetos()
                    for o in obj:
                        if o.get_minuto_llegada() == pieza.get_minuto_llegada():
                            o.set_estado("Fundiendo")
                            break
                    self.set_objetos(obj)
                else:
                    self.etapa_fundido.set_estado(False)
                if self.etapa_forjado.get_estado():
                    obj = self.get_objetos()
                    for o in obj:
                        if o.get_estado() == "Fundiendo":
                            o.set_estado("Esperando Forjar")
                            pieza = o
                            break
                    self.set_objetos(obj)
                    cola = self.etapa_forjado.get_cola()
                    cola.append(pieza)
                    self.etapa_forjado.set_cola(cola)
                else:
                    obj = self.get_objetos()
                    for o in obj:
                        if o.get_estado() == "Fundiendo":
                            o.set_estado("Forjando")
                            break
                    self.set_objetos(obj)
                    self.etapa_forjado.set_estado(True)
                    rnd_fin_forjado = random.random()
                    tiempo_forjado = self.distribucion_uniforme(rnd_fin_forjado, fin_forjado_inf, fin_forjado_sup)
                    self.eventos = [self.eventos[0], self.eventos[1], [rnd_fin_forjado, tiempo_forjado, self.reloj + tiempo_forjado], 
                                self.eventos[3],self.eventos[4]]

            #fin_forjado
            elif self.reloj == self.eventos[2][2]:
                self.nombre_evento = "Fin_forjado"
                cola = self.etapa_forjado.get_cola()
                if len(cola) > 0:
                    pieza = cola.pop(0)
                    obj = self.get_objetos()
                    for o in obj:
                        if o.get_minuto_llegada() == pieza.get_minuto_llegada():
                            o.set_estado("Forjando")
                            break
                    self.set_objetos(obj)
                    rnd_fin_forjado = random.random()
                    tiempo_forjado = self.distribucion_uniforme(rnd_fin_forjado, fin_forjado_inf, fin_forjado_sup)
                    self.eventos = [self.eventos[0], self.eventos[1], [rnd_fin_forjado, tiempo_forjado, self.reloj + tiempo_forjado], 
                                self.eventos[3],self.eventos[4]]
                else:
                    self.etapa_forjado.set_estado(False)
                obj = self.get_objetos()
                for o in obj:
                    if o.get_estado() == "Forjando":
                        o.set_estado("Enfriando")
                        break
                self.set_objetos(obj)
                self.etapa_enfriado.set_estado(True)
                self.etapa_enfriado.agregar_pieza()
                self.eventos = [self.eventos[0], self.eventos[1], self.eventos[2], [self.reloj, fin_enfriado, self.reloj + fin_enfriado],
                                self.eventos[4]]
            #fin_enfriado
            elif self.reloj == self.eventos[3][2]:
                self.nombre_evento = "Fin_enfriado"
                if self.etapa_terminado.get_estado():
                    obj = self.get_objetos()
                    for o in obj:
                        if o.get_estado == "Enfriando":
                            o.set_estado("Esperando Terminado")
                            pieza = o
                            break
                    cola = self.etapa_terminado.get_cola()
                    cola.append(pieza)
                    self.set_objetos(obj)
                    self.etapa_terminado.set_cola(cola)
                else:
                    obj = self.get_objetos()
                    for o in obj:
                        if o.get_estado == "Enfriando":
                            o.set_estado("Terminando")
                            pieza = o
                            break
                    self.etapa_terminado.set_estado(True)
                    rnd_fin_terminado = random.random()
                    tiempo_terminado = self.distribucion_uniforme(rnd_fin_terminado, fin_terminado_inf, fin_terminado_sup)
                    self.eventos = [self.eventos[0], self.eventos[1], self.eventos[2], self.eventos[3], 
                                    [rnd_fin_terminado, tiempo_terminado, self.reloj + tiempo_terminado]]
                    

            #fin_terminado
            elif self.reloj == self.eventos[4][2]:
                self.nombre_evento = "Fin_terminado"
                cola = self.etapa_terminado.get_cola()
                if len(cola) > 0:
                    pieza = cola.pop(0)
                    obj = self.get_objetos()
                    for o in obj:
                        if o.get_estado() == "Esperando Terminado":
                            o.set_estado("Terminando")
                            break
                    self.set_objetos(obj)
                    self.etapa_terminado.set_cola(cola)
                    rnd_fin_terminado = random.random()
                    tiempo_terminado = self.distribucion_uniforme(rnd_fin_terminado, fin_terminado_inf, fin_terminado_sup)
                    self.eventos = [self.eventos[0], self.eventos[1], self.eventos[2], self.eventos[3], 
                                    [rnd_fin_terminado, tiempo_terminado, self.reloj + tiempo_terminado]]
                else:
                    self.etapa_terminado.set_estado(False)
                obj = self.get_objetos()
                for o in obj:
                    if o.get_estado() == "Terminando":
                        obj.pop(o)
                        break
                self.set_objetos(obj)

            return [self.reloj, self.eventos, self.etapa_fundido, self.etapa_forjado, self.etapa_enfriado, self.etapa_terminado, self.objetos]
        
    def __str__(self) -> str:
        return f"Reloj: {self.reloj}, Eventos: {self.eventos}, Fundido: {self.etapa_fundido}, Forjado: {self.etapa_forjado}, Enfriado: {self.etapa_enfriado}, Terminado: {self.etapa_terminado}, Objetos: {self.objetos}"