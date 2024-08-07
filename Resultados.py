import tkinter as tk
from tkinter import Toplevel, ttk
from tkinter import Scrollbar
class ResultadosVentana:
    def __init__(self, root ):
        self.root = root
        #self.frame = frame
        self.root.title("Resultados de la Simulación")

        # Crear un Frame para contener el Treeview y los scrollbars
        self.frame = ttk.Frame(root)
        self.frame.pack(expand=True, fill=tk.BOTH)

        # Crear el Treeview para mostrar los resultados de la simulación
        self.tree = ttk.Treeview(self.frame, columns=("ID", "Evento", "Reloj","rnd_l", "llegada_p","proxima_l", 
                                "rnd_fun", "tiempo_fun","fin_fundido", "rnd_for", "tiempo_for","fin_forjado",
                                "comienzo_enf", "tiempo_enf","fin_enfriado",
                                "rnd_term", "tiempo_term","fin_terminado",
                                "Estado Fundido", "Cola Fundido","Estado Forjado",
                                "Cola Forjado", "Estado Enfriado", "Cantidad enfriando",
                                "Estado Terminado", "Cola Terminado", "Objeto1", "Objeto2", "Objeto3", "Objeto4"), show="headings")
        
        # Configurar encabezados y anchos de columna
        columns = [
            ("ID", 50), ("Evento", 270), ("Reloj", 90), ("rnd_l", 80), ("llegada_p", 80), ("proxima_l", 80),
            ("rnd_fun", 80), ("tiempo_fun", 80), ("fin_fundido", 80), ("rnd_for", 80), ("tiempo_for", 80), ("fin_forjado", 80),
            ("comienzo_enf", 80), ("tiempo_enf", 120), ("fin_enfriado", 120),
            ("rnd_term", 80), ("tiempo_term", 120), ("fin_terminado", 120),
            ("Estado Fundido", 80), ("Cola Fundido", 120), ("Estado Forjado", 120),
            ("Cola Forjado", 80), ("Estado Enfriado", 120), ("Cantidad enfriando", 80),
            ("Estado Terminado", 120), ("Cola Terminado", 60), 
            ("Objeto1", 480),("Objeto2", 480),("Objeto3", 480),("Objeto4", 480)
        ]

        for col, width in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, minwidth=width, width=width, anchor='center')
    
        #self.tree.column("Estado Cancha", width=120, anchor='w')
        self.tree.column("Evento", width=270, anchor='w')
        self.tree.column("Objeto1", width=480, anchor='w')
        self.tree.column("Objeto2", width=480, anchor='w')
        self.tree.column("Objeto3", width=480, anchor='w')
        self.tree.column("Objeto4", width=480, anchor='w')

        # Crear los scrollbars y asociarlos con el Treeview
        self.vsb = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
        self.hsb = ttk.Scrollbar(self.frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)

        # Empaquetar el Treeview y los scrollbars
        self.vsb.pack(side=tk.RIGHT, fill=tk.Y)
        self.hsb.pack(side=tk.BOTTOM, fill=tk.X)
        self.tree.pack(expand=True, fill=tk.BOTH)



    def mostrar_resultados(self, tabla_resultados, hora_especifica, cantidad_filas):

        # Truncar
        def truncar(numero, decimales=3):
            if numero is not None:
                factor = 10 ** decimales
                return int(numero * factor) / factor
            else:
                return ""
            
        # Limpiar el Treeview antes de insertar nuevos datos
        for row in self.tree.get_children():
            self.tree.delete(row)

        if hora_especifica == 0 and cantidad_filas != 0:
            for i, fila in enumerate(tabla_resultados[0:cantidad_filas]):
                objeto1, objeto2, objeto3, objeto4 = "", "", "", ""
                # if len(objetos[fila.id]) > 0:
                #     if len(objetos[fila.id]) == 1:
                #         o1 = objetos.get(fila.id)[0]
                #         o1.set_estado(estados[fila.id][0])
                #         objeto1 = str(o1)
                #     elif len(objetos[fila.id]) == 2:
                #         o1 = objetos.get(fila.id)[0]
                #         o1.set_estado(estados[fila.id][0])
                #         objeto1 = str(o1)
                #         o2 = objetos.get(fila.id)[1]
                #         o2.set_estado(estados[fila.id][1])
                #         objeto2 = str(o2)
                #     elif len(objetos[fila.id]) == 3:
                #         o1 = objetos.get(fila.id)[0]
                #         o1.set_estado(estados[fila.id][0])
                #         objeto1 = str(o1)
                #         o2 = objetos.get(fila.id)[1]
                #         o2.set_estado(estados[fila.id][1])
                #         objeto2 = str(o2)
                #         o3 = objetos.get(fila.id)[2]
                #         o3.set_estado(estados[fila.id][2])
                #         objeto3 = str(o3)
                #     else:
                #         o1 = objetos.get(fila.id)[0]
                #         o1.set_estado(estados[fila.id][0])
                #         objeto1 = str(o1)
                #         o2 = objetos.get(fila.id)[1]
                #         o2.set_estado(estados[fila.id][1])
                #         objeto2 = str(o2)
                #         o3 = objetos.get(fila.id)[2]
                #         o3.set_estado(estados[fila.id][2])
                #         objeto3 = str(o3)
                #         o4 = objetos.get(fila.id)[3]
                #         o4.set_estado(estados[fila.id][3])
                #         objeto4 = str(o4)
                
                self.tree.insert("", "end", values=(fila.id, fila.nombre_evento, truncar(fila.reloj),
                                truncar(fila.eventos[0][0]), truncar(fila.eventos[0][1]),truncar(fila.eventos[0][2]), 
                                truncar(fila.eventos[1][0]), truncar(fila.eventos[1][1]),truncar(fila.eventos[1][2]),
                                truncar(fila.eventos[2][0]), truncar(fila.eventos[2][1]),truncar(fila.eventos[2][2]),
                                truncar(fila.eventos[3][0]),truncar(fila.eventos[3][1]), truncar(fila.eventos[3][2]),
                                truncar(fila.eventos[4][0]),truncar(fila.eventos[4][1]), truncar(fila.eventos[4][2]),
                                fila.etapa_fundido.get_estado(), fila.etapa_fundido.get_cola(), fila.etapa_forjado.get_estado(), fila.etapa_forjado.get_cola(),
                                fila.etapa_enfriado.get_estado(), fila.etapa_enfriado.get_piezas(), fila.etapa_terminado.get_estado(), fila.etapa_terminado.get_cola(),
                                objeto1, objeto2, objeto3, objeto4))

            self.tree.insert("", "end", values=(tabla_resultados[-1].id, tabla_resultados[-1].nombre_evento, truncar(tabla_resultados[-1].reloj),
                                truncar(tabla_resultados[-1].eventos[0][0]), truncar(tabla_resultados[-1].eventos[0][1]),truncar(tabla_resultados[-1].eventos[0][2]), 
                                truncar(tabla_resultados[-1].eventos[1][0]), truncar(tabla_resultados[-1].eventos[1][1]),truncar(tabla_resultados[-1].eventos[1][2]),
                                truncar(tabla_resultados[-1].eventos[2][0]), truncar(tabla_resultados[-1].eventos[2][1]),truncar(tabla_resultados[-1].eventos[2][2]),
                                truncar(tabla_resultados[-1].eventos[3][0]),truncar(tabla_resultados[-1].eventos[3][1]), truncar(tabla_resultados[-1].eventos[3][2]),
                                truncar(tabla_resultados[-1].eventos[4][0]),truncar(tabla_resultados[-1].eventos[4][1]), truncar(tabla_resultados[-1].eventos[4][2]),
                                tabla_resultados[-1].etapa_fundido.get_estado(), tabla_resultados[-1].etapa_fundido.get_cola(), tabla_resultados[-1].etapa_forjado.get_estado(), tabla_resultados[-1].etapa_forjado.get_cola(),
                                tabla_resultados[-1].etapa_enfriado.get_estado(), tabla_resultados[-1].etapa_enfriado.get_piezas(), tabla_resultados[-1].etapa_terminado.get_estado(), tabla_resultados[-1].etapa_terminado.get_cola()))

                                                
        elif hora_especifica != 0 and cantidad_filas != 0:

            for i, fila in enumerate(tabla_resultados[0:cantidad_filas]):
                if fila.reloj >= hora_especifica:
                    objeto1, objeto2, objeto3, objeto4 = "", "", "", ""
                    # if len(objetos[fila.id]) > 0:
                    #     if len(objetos[fila.id]) == 1:
                    #         objeto1 = str(objetos.get(fila.id)[0])
                    #     elif len(objetos[fila.id]) == 2:
                    #         objeto1 = str(objetos.get(fila.id)[0])
                    #         objeto2 = str(objetos.get(fila.id)[1])
                    #     elif len(objetos[fila.id]) == 3:
                    #         objeto1 = str(objetos.get(fila.id)[0])
                    #         objeto2 = str(objetos.get(fila.id)[1])
                    #         objeto3 = str(objetos.get(fila.id)[2])
                    #     else:
                    #         objeto1 = str(objetos.get(fila.id)[0])
                    #         objeto2 = str(objetos.get(fila.id)[1])
                    #         objeto3 = str(objetos.get(fila.id)[2])
                    #         objeto4 = str(objetos.get(fila.id)[3])
                    self.tree.insert("", "end", values=(fila.id, fila.nombre_evento, truncar(fila.reloj),
                                truncar(fila.eventos[0][0]), truncar(fila.eventos[0][1]),truncar(fila.eventos[0][2]), 
                                truncar(fila.eventos[1][0]), truncar(fila.eventos[1][1]),truncar(fila.eventos[1][2]),
                                truncar(fila.eventos[2][0]), truncar(fila.eventos[2][1]),truncar(fila.eventos[2][2]),
                                truncar(fila.eventos[3][0]),truncar(fila.eventos[3][1]), truncar(fila.eventos[3][2]),
                                truncar(fila.eventos[4][0]),truncar(fila.eventos[4][1]), truncar(fila.eventos[4][2]),
                                fila.etapa_fundido.get_estado(), fila.etapa_fundido.get_cola(), fila.etapa_forjado.get_estado(), fila.etapa_forjado.get_cola(),
                                fila.etapa_enfriado.get_estado(), fila.etapa_enfriado.get_piezas(), fila.etapa_terminado.get_estado(), fila.etapa_terminado.get_cola(),
                                objeto1, objeto2, objeto3, objeto4))

            self.tree.insert("", "end", values=(tabla_resultados[-1].id, tabla_resultados[-1].nombre_evento, truncar(tabla_resultados[-1].reloj),
                                truncar(tabla_resultados[-1].eventos[0][0]), truncar(tabla_resultados[-1].eventos[0][1]),truncar(tabla_resultados[-1].eventos[0][2]), 
                                truncar(tabla_resultados[-1].eventos[1][0]), truncar(tabla_resultados[-1].eventos[1][1]),truncar(tabla_resultados[-1].eventos[1][2]),
                                truncar(tabla_resultados[-1].eventos[2][0]), truncar(tabla_resultados[-1].eventos[2][1]),truncar(tabla_resultados[-1].eventos[2][2]),
                                truncar(tabla_resultados[-1].eventos[3][0]),truncar(tabla_resultados[-1].eventos[3][1]), truncar(tabla_resultados[-1].eventos[3][2]),
                                truncar(tabla_resultados[-1].eventos[4][0]),truncar(tabla_resultados[-1].eventos[4][1]), truncar(tabla_resultados[-1].eventos[4][2]),
                                tabla_resultados[-1].etapa_fundido.get_estado(), tabla_resultados[-1].etapa_fundido.get_cola(), tabla_resultados[-1].etapa_forjado.get_estado(), tabla_resultados[-1].etapa_forjado.get_cola(),
                                tabla_resultados[-1].etapa_enfriado.get_estado(), tabla_resultados[-1].etapa_enfriado.get_piezas(), tabla_resultados[-1].etapa_terminado.get_estado(), tabla_resultados[-1].etapa_terminado.get_cola()))
        else:
            self.tree.insert("","end",values="")           