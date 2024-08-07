import tkinter as tk
from tkinter import ttk

class VentanaMetalurgica:
    def __init__(self, root):
        self.root = root
        self.root.title("Metalurgica")
        
        # Crear un frame principal
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Etiquetas y entradas para la carga de datos
        self.labels_texts = [
            "Cantidad de tiempo (min):", "Probabilidad de que llegue una pieza en 1 minuto:",
            "Probabilidad de que llegue una pieza en 2 minutos:", "Probabilidad de que llegue una pieza en 3 minutos:",
            "Probabilidad de que llegue una pieza en 4 minutos:", "Intervalo inferior de fin de fundición (min):",
            "Intervalo superior de fin de fundición (min):", "Intervalo inferior de fin de forjado (min):",
            "Intervalo superior de fin de forjado (min):", "Tiempo de espera de enfriado (min):",
            "Intervalo inferior de fin de terminado (min):", "Intervalo superior de fin de terminado (min):",
            "Cantidad de filas a mostrar (i):", "Minuto específico a mostrar (j):"
        ]
        
        self.default_values = [
            1000, 0.3, 0.2, 0.2, 0.3, 2, 4, 3, 6, 10, 3, 7, 100, 10
        ]
        
        self.entries = {}
        
        for i, (text, default_value) in enumerate(zip(self.labels_texts, self.default_values)):
            label = ttk.Label(self.main_frame, text=text)
            label.grid(row=i, column=0, sticky=tk.W, pady=5)  # Incrementar el padding vertical
            entry = ttk.Entry(self.main_frame, width=30)
            entry.grid(row=i, column=1, pady=5)  # Incrementar el padding vertical
            entry.insert(0, str(default_value))  # Insertar el valor por defecto
            self.entries[text] = entry
        
        # Botón para iniciar la simulación
        self.iniciar_button = ttk.Button(self.main_frame, text="Iniciar simulación", command=self.iniciar_simulacion)
        self.iniciar_button.grid(row=len(self.labels_texts), column=0, columnspan=2, pady=20)
        
        # Ajustar el tamaño de las columnas
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        
    def iniciar_simulacion(self):
        # Aquí puedes agregar la lógica para iniciar la simulación
        datos = {label: entry.get() for label, entry in self.entries.items()}
        datos = [entry.get() for entry in self.entries.values()]

        tiempo_total = int(datos[0])
        prob_llegada_uno = float(datos[1])
        prob_llegada_dos = float(datos[2])
        prob_llegada_tres = float(datos[3])
        prob_llegada_cuatro = float(datos[4])
        fin_fundido_inf = float(datos[5])
        fin_fundido_sup = float(datos[6])
        fin_forjado_inf = float(datos[7])
        fin_forjado_sup = float(datos[8])
        fin_enfriado = float(datos[9])
        fin_terminado_inf = float(datos[10])
        fin_terminado_sup = float(datos[11])
        cantidad_filas = int(datos[12])
        minuto_especifico = int(datos[13])

        print("Datos ingresados para la simulación:", datos)
        print("Simulación iniciada")

# Crear la ventana principal y la instancia de la clase
root = tk.Tk()
app = VentanaMetalurgica(root)

# Iniciar el bucle principal de tkinter
root.mainloop()
