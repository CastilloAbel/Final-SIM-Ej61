from VentanaMetalurgica import VentanaMetalurgica
import tkinter as tk

def main():
    # Crear la ventana principal y la instancia de la clase
    root = tk.Tk()
    app = VentanaMetalurgica(root)
    # Iniciar el bucle principal de tkinter
    root.mainloop()


if __name__ == "__main__":
    main()