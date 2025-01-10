






















from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
import cohere
from tkinter import messagebox
import os
import sys
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
# Initialisation de l'API Cohere avec votre clé API
cohere_client = cohere.Client('')

# Variable globale pour stocker la description générée
generated_description = ""

def generate_description():
    global generated_description
    product_name = entry_2.get()
    keywords = entry_3.get()
    product_details = entry_4.get("1.0", "end-1c")
    
    if not product_name or not keywords or not product_details:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
        return
    
    # Créer le prompt pour Cohere
    prompt = f"Product Name: {product_name}\nKeywords: {keywords}\nDetails: {product_details}\n\nGive me a description of this product in 1000 words maximum.to share it in shopify , give me some h1 heading and some keywords "
    
    # Envoyer une requête à Cohere pour générer une description du produit
    response = cohere_client.generate(
        model='command-light',
        prompt=prompt,
        max_tokens=1000,
        temperature=0.7
    )
    
    # Stocker la description générée dans la variable globale
    generated_description = response.generations[0].text.strip()
    
    # Afficher la description générée dans la zone de texte dédiée
    entry_1.delete(1.0, tk.END)  # Supprimer le texte existant
    entry_1.insert(tk.END, generated_description)  # Insérer la nouvelle description

def copy_description():
    global generated_description
    if generated_description:
        # Copier la description dans le presse-papiers
        window.clipboard_clear()
        window.clipboard_append(generated_description)
        window.update()  # Mettre à jour le presse-papiers
        messagebox.showinfo("Copié", "La description a été copiée dans le presse-papiers.")
    else:
        messagebox.showwarning("Aucune description", "Aucune description à copier. Veuillez générer une description d'abord.")

OUTPUT_PATH = Path(__file__).parent 
#ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Ayoub\Videos\build\assets\frame0")
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("700x600")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
background_image = PhotoImage(file=relative_to_assets("bg.png"))
canvas.create_image(0, 0, image=background_image, anchor="nw")
canvas.create_rectangle(
    264.0,
    475.0,
    437.0,
    508.0,
    fill="#000940",
    outline=""
)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    522.0,
    274.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=395.0,
    y=102.0,
    width=254.0,
    height=342.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=38.0,
    y=36.0,
    width=108.0,
    height=24.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=222.0,
    y=36.0,
    width=108.0,
    height=24.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=553.0,
    y=36.0,
    width=108.0,
    height=24.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=390.0,
    y=36.0,
    width=121.0,
    height=24.0
)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    173.5,
    121.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=50.0,
    y=102.0,
    width=247.0,
    height=36.0
)

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    173.5,
    208.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=50.0,
    y=189.0,
    width=247.0,
    height=36.0
)

entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    173.5,
    349.5,
    image=entry_image_4
)
entry_4 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=50.0,
    y=269.0,
    width=247.0,
    height=159.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=generate_description,
    relief="flat"
)
button_5.place(
    x=264.0,
    y=475.0,
    width=173.0,
    height=33.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=copy_description,
    relief="flat"
)
button_6.place(
    x=383.0,
    y=416.0,
    width=278.0,
    height=30.0
)

window.resizable(False, False)
window.mainloop()











# from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
# import tkinter as tk
# import cohere
# from tkinter import messagebox
# import os
# import sys

# # Fonction pour obtenir le chemin des ressources
# def resource_path(relative_path):
#     try:
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")
#     return os.path.join(base_path, relative_path)

# # Initialisation de l'API Cohere
# cohere_client = cohere.Client('E2G8ATrN8Yb8Di9CBXRYX7TLKz9ZoI4DM01DnmGl')

# # Fonction pour générer une description
# def generate_description():
#     global generated_description
#     product_name = entry_2.get()
#     keywords = entry_3.get()
#     product_details = entry_4.get("1.0", "end-1c")
    
#     if not product_name or not keywords or not product_details:
#         messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
#         return
    
#     # Créer le prompt pour Cohere
#     prompt = f"Product Name: {product_name}\nKeywords: {keywords}\nDetails: {product_details}\n\nGive me a description of this product in 100 words maximum."
    
#     # Envoyer une requête à Cohere
#     response = cohere_client.generate(
#         model='command-light',
#         prompt=prompt,
#         max_tokens=100,
#         temperature=0.7
#     )
    
#     # Stocker la description générée
#     generated_description = response.generations[0].text.strip()
    
#     # Afficher la description générée
#     entry_1.delete(1.0, tk.END)
#     entry_1.insert(tk.END, generated_description)

# # Fonction pour copier la description
# def copy_description():
#     global generated_description
#     if generated_description:
#         window.clipboard_clear()
#         window.clipboard_append(generated_description)
#         window.update()
#         messagebox.showinfo("Copié", "La description a été copiée dans le presse-papiers.")
#     else:
#         messagebox.showwarning("Aucune description", "Aucune description à copier. Veuillez générer une description d'abord.")

# # Fonction pour afficher le frame correspondant
# def show_frame(frame):
#     frame.tkraise()

# # Initialisation de la fenêtre principale
# window = Tk()
# window.geometry("700x600")
# window.configure(bg = "#FFFFFF")

# # Création du conteneur principal pour les frames
# container = tk.Frame(window)
# container.pack(side="top", fill="both", expand=True)

# # Création des frames de contenu
# frames = {}
# for F in ("Description", "Title", "Meta Description", "Strategy Tools"):
#     frame = tk.Frame(container)
#     frames[F] = frame

#     # Layout de chaque frame
#     frame.grid(row=0, column=0, sticky="nsew")

# # Exemple de contenu pour le frame "Description"
# label_description = tk.Label(frames["Description"], text="Contenu de Description", font=('Arial', 14))
# label_description.pack(pady=20)

# # Afficher le frame "Description" par défaut
# show_frame(frames["Description"])

# # Création des boutons du menu
# menu_frame = tk.Frame(window)
# menu_frame.pack(side="top", fill="x")

# button_1 = Button(menu_frame, text="Description", command=lambda: show_frame(frames["Description"]))
# button_1.pack(side="left", padx=10)

# button_2 = Button(menu_frame, text="Title", command=lambda: show_frame(frames["Title"]))
# button_2.pack(side="left", padx=10)

# button_3 = Button(menu_frame, text="Meta Description", command=lambda: show_frame(frames["Meta Description"]))
# button_3.pack(side="left", padx=10)

# button_4 = Button(menu_frame, text="Strategy Tools", command=lambda: show_frame(frames["Strategy Tools"]))
# button_4.pack(side="left", padx=10)

# window.mainloop()
