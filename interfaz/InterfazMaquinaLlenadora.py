import customtkinter as ctk
from PIL import Image, ImageTk

datos = []

def mostrar_pantalla(frame):
    frame.tkraise()

def boton_presionado(tipo_bebida):
    datos.append(tipo_bebida)
    print(f"Selección: {tipo_bebida}")
    mostrar_pantalla(tercera_pantalla)

def cantidad(cantidad_seleccionada):
    datos.append(cantidad_seleccionada)
    print(f"Cantidad: {cantidad_seleccionada}")
    mostrar_pantalla(quinta_pantalla)

def servir():
    print("Acción: SERVIR")
    datos.append("SERVIR")
    print(f"Datos guardados: {datos}")

def reiniciar():  
    datos.clear()
    mostrar_pantalla(segunda_pantalla)
    print("Se reinició su elección")

app = ctk.CTk()
app.geometry("1366x768")
app.title("Maquina autollenado de botellas")
app.configure(fg_color="#FFFFFF")

main_frame = ctk.CTkFrame(app, fg_color="#FFFFFF", bg_color="#FFFFFF")
main_frame.pack(fill="both", expand=True)

pantalla_principal = ctk.CTkFrame(main_frame, fg_color="#FFFFFF", bg_color="#FFFFFF")
segunda_pantalla = ctk.CTkFrame(main_frame, fg_color="#1A2C47", bg_color="#1A2C47")
tercera_pantalla = ctk.CTkFrame(main_frame, fg_color="#1A2C47", bg_color="#1A2C47")
quinta_pantalla = ctk.CTkFrame(main_frame, fg_color="#1A2C47", bg_color="#1A2C47")

for frame in (pantalla_principal, segunda_pantalla, tercera_pantalla, quinta_pantalla):
    frame.place(x=0, y=0, relwidth=1, relheight=1)

image = Image.open("logo.png")
image = image.resize((350, 350), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(image)

label_principal = ctk.CTkLabel(pantalla_principal, image=photo, text="")
label_principal.image = photo
label_principal.pack(pady=20)

font_config = ("Roboto Condensed", 35, "bold")
boton_principal = ctk.CTkButton(pantalla_principal, text="INICIAR", font=font_config, fg_color="#A8D500", text_color="#000000", corner_radius=40, width=400, height=90, command=lambda: mostrar_pantalla(segunda_pantalla))
boton_principal.pack(pady=100)

imagenes_segunda = [
    {"ruta": "logowlema.png", "tamaño": (350, 180), "color_fondo": "#1A2C47"},
    {"ruta": "bebida.png", "tamaño": (600, 150), "color_fondo": "#1A2C47"},
    {"ruta": "lata.png", "tamaño": (400, 500), "color_fondo": "#1A2C47"},
]

x = 20
y = 20
altura_max_en_fila = 0
for img_data in imagenes_segunda:
    imagen = Image.open(img_data["ruta"])
    imagen = imagen.resize(img_data["tamaño"], Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(imagen)
    
    label = ctk.CTkLabel(segunda_pantalla, image=photo, text="", bg_color=img_data["color_fondo"])
    label.image = photo
    if img_data["ruta"] == "logowlema.png":
        label.place(x=x, y=y-20)
    elif img_data["ruta"] == "lata.png":
        label.place(x=x - 20, y=y -20)
    elif img_data["ruta"] == "bebida.png":
        label.place(x=x +90, y=y+45 )
    else:
        label.place(x=x, y=y)

    x += img_data["tamaño"][0] + 20
    altura_max_en_fila = max(altura_max_en_fila, img_data["tamaño"][1])
    
    if x + img_data["tamaño"][0] > 1200:
        x = 20
        y += altura_max_en_fila + 20
        altura_max_en_fila = 0
        
font_config = ("Roboto Condensed", 35, "bold")
boton1 = ctk.CTkButton(segunda_pantalla, text="GASEOSA", font=font_config, fg_color="#FFFFFF", text_color="#000000", corner_radius=40, width=500, height=100, command=lambda: boton_presionado("GASEOSA"))
boton1.place(x=550, y=280)
boton2 = ctk.CTkButton(segunda_pantalla, text="JUGOS", font=font_config, fg_color="#FFFFFF", text_color="#000000", corner_radius=40, width=500, height=100, command=lambda: boton_presionado("JUGOS"))
boton2.place(x=550, y=420)
boton3 = ctk.CTkButton(segunda_pantalla, text="AGUA", font=font_config, fg_color="#FFFFFF", text_color="#000000", corner_radius=40, width=500, height=100, command=lambda: boton_presionado("AGUA"))
boton3.place(x=550, y=560)

imagenes_tercera = [
    {"ruta": "logowlema.png", "tamaño": (350, 180), "color_fondo": "#1A2C47"},
    {"ruta": "Seleccionatamaño.png", "tamaño": (1200, 65), "color_fondo": "#1A2C47"},
    {"ruta": "250ml.png", "tamaño": (250, 350), "color_fondo": "#1A2C47"},
    {"ruta": "500ml.png", "tamaño": (250, 350), "color_fondo": "#1A2C47"},
    {"ruta": "750ml.png", "tamaño": (250, 350), "color_fondo": "#1A2C47"},
]

x = 20
y = 20
altura_max_en_fila = 0
for img_data in imagenes_tercera:
    imagen = Image.open(img_data["ruta"])
    imagen = imagen.resize(img_data["tamaño"], Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(imagen)
    
    label = ctk.CTkLabel(tercera_pantalla, image=photo, text="", bg_color=img_data["color_fondo"])
    label.image = photo
    if img_data["ruta"] == "logowlema.png":
        label.place(x=x, y=y-20)
    elif img_data["ruta"] == "Seleccionatamaño.png":
        label.place(x=x -300, y=y +160)
    elif img_data["ruta"] == "250ml.png":
        label.place(x=x +140, y=y+90 )
        label.bind("<Button-1>", lambda event, nombre="250ml": cantidad(nombre))
    elif img_data["ruta"] == "500ml.png":
        label.place(x=x +260, y=y+90 )
        label.bind("<Button-1>", lambda event, nombre="500ml": cantidad(nombre))
    elif img_data["ruta"] == "750ml.png":
        label.place(x=x +380, y=y+90 )
        label.bind("<Button-1>", lambda event, nombre="750ml": cantidad(nombre))
    else:
        label.place(x=x, y=y)

    x += img_data["tamaño"][0] + 20
    altura_max_en_fila = max(altura_max_en_fila, img_data["tamaño"][1])
    
    if x + img_data["tamaño"][0] > 1200:
        x = 20
        y += altura_max_en_fila + 20
        altura_max_en_fila = 0

imagenes_quinta = [
    {"ruta": "logowlema.png", "tamaño": (300, 150), "color_fondo": "#1A2C47"}
]

x = 20
y = 20
altura_max_en_fila = 0
imagenes = [
    {"ruta": "logowlema.png", "tamaño": (350, 180), "color_fondo": "#1A2C47"}
]
x = 20
y = 20
altura_max_en_fila = 0 
for img_data in imagenes:
    imagen = Image.open(img_data["ruta"])
    imagen = imagen.resize(img_data["tamaño"], Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(imagen)
    
    label = ctk.CTkLabel(quinta_pantalla, image=photo, text="", bg_color=img_data["color_fondo"])
    label.image = photo
    if img_data["ruta"] == "logowlema.png":
        label.place(x=x, y=y-20)
    else:
        label.place(x=x, y=y)

    x += img_data["tamaño"][0] + 20  
    altura_max_en_fila = max(altura_max_en_fila, img_data["tamaño"][1])  
    
    if x + img_data["tamaño"][0] > 1200:
        x = 20
        y += altura_max_en_fila + 20  
        altura_max_en_fila = 0
font_config = ("Roboto Condensed", 60, "bold")
boton1 = ctk.CTkButton(quinta_pantalla, text="SERVIR", font=font_config, fg_color="#FFFFFF", text_color="#000000", corner_radius=80, width=750, height=135, command=servir)
boton1.place(x=310, y=200)
boton2 = ctk.CTkButton(quinta_pantalla, text="REINICIAR", font=font_config, fg_color="#FFFFFF", text_color="#000000", corner_radius=80, width=750, height=135, command=reiniciar)
boton2.place(x=310, y=450)

mostrar_pantalla(pantalla_principal)
app.mainloop()
