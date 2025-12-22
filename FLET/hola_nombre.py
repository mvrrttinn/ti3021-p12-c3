# Este ejemolo va a abarcar 
# El uso de Inputs, labels y botones
# Para familiarizarse que cosas basicas
# De funcionalidad dpdoemos lograr con flet 

# Paso.1 Importar flet
import flet as ft

# Paso 2. Crear la clase de la App
class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.tittle = "Hola nombre"
        
        self.input_nombre = ft.TextField( hint_text = "Ingresa tu nombre: " )
        self.button_saludar = ft.Button( text = "Saludar", on_click=self.handle_saludo)
        self.text_saludo = ft.Text( value = "")

        self.build()

    def build(self):
        self.page.add(
         self.input_nombre,
         self.button_saludar,
         self.text_saludo   
        )
        self.page.update()

    def handle_saludo(self, e):
        nombre = (self.input_nombre.value or "").strip()
        if nombre:
            self.text_saludo.value = f"Hola, {nombre}"
        else:
            self.text_saludo.value = "Ingrese un Nombre"
        self.page.update()        

if __name__ == "__main__":
    ft.app(target=App)
