import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class SistemaCine:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Sistema de Cine")

        self.peliculas = {
            "Parasite": 10,
            "La La Land": 12,
            "The Dark Knight": 15
        }

        self.etiqueta_titulo = tk.Label(ventana, text="Bienvenido al Cinemas", font=("Arial", 18))
        self.etiqueta_titulo.pack(pady=10)

        # Cargar y mostrar imagen
        self.imagen = Image.open("cine.jpg")  # Ruta de la imagen
        self.imagen = self.imagen.resize((200, 200), Image.BICUBIC)  # Redimensionar la imagen
        self.imagen = ImageTk.PhotoImage(self.imagen)
        self.etiqueta_imagen = tk.Label(ventana, image=self.imagen)
        self.etiqueta_imagen.pack()

        self.etiqueta_pelicula = tk.Label(ventana, text="Seleccione una película:")
        self.etiqueta_pelicula.pack()

        self.lista_peliculas = tk.Listbox(ventana, height=5, selectmode="SINGLE")
        for pelicula in self.peliculas:
            self.lista_peliculas.insert(tk.END, pelicula)
        self.lista_peliculas.pack()

        self.etiqueta_cantidad = tk.Label(ventana, text="Cantidad de boletos:")
        self.etiqueta_cantidad.pack()

        self.entry_cantidad = tk.Entry(ventana)
        self.entry_cantidad.pack()

        self.boton_comprar = tk.Button(ventana, text="Comprar", command=self.comprar_boletos)
        self.boton_comprar.pack(pady=5)

        self.ventana.mainloop()

    def comprar_boletos(self):
        try:
            seleccion = self.lista_peliculas.curselection()
            pelicula_seleccionada = self.lista_peliculas.get(seleccion[0])
            cantidad_boletos = int(self.entry_cantidad.get())
            if cantidad_boletos <= 0:
                messagebox.showerror("Error", "La cantidad de boletos debe ser mayor que cero.")
            else:
                precio_pelicula = self.peliculas[pelicula_seleccionada]
                precio_total = precio_pelicula * cantidad_boletos
                messagebox.showinfo("Detalle de Compra", f"Película: {pelicula_seleccionada}\nCantidad de boletos: {cantidad_boletos}\nPrecio Total: ${precio_total}")
        except IndexError:
            messagebox.showerror("Error", "Por favor seleccione una película.")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese una cantidad válida de boletos.")

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = SistemaCine(ventana_principal)
