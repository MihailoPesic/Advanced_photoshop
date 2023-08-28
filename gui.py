# import tkinter as tk
# from tkinter import *
# from tkinter import filedialog
# from PIL import Image, ImageTk
# from PIL import Image, ImageTk, ImageEnhance

# def promeni_kontrast(slika, vrednost):
#     ImageEnhance.Contrast(slika).enchance(vrednost)

# class GUI:

#     def __init__(self, root):
#         self.root = root
#         self.root.title("Advanced Photoshop")
#         self.root.geometry("1200x800")
#         self.root.resizable(1, 1)
#         self.root.config(bg="grey")
#         self.slika_path = None
#         self.label = tk.Label(self.root)
#         self.label.pack()
        
#         dodaj_sliku_button = tk.Button(self.root, text="Dodaj sliku", command=self.dodaj_sliku)
#         dodaj_sliku_button.pack()
#         if self.slika_path is not None:
#             self.prikazi_sliku(self.slika_path)
#         promeni_kontrast_button = tk.Button(self.root, text="Promeni kontrast", command=self.menjanje_kontrasta)
#         promeni_kontrast_button.pack()
#         dodaj_sliku_button.pack()
        
#     def prikazi_sliku(self, pathSlike):
#         img = Image.open(pathSlike)
#         img_tk = ImageTk.PhotoImage(img)
#         self.label.config(image=img_tk)
#         self.label.img = img_tk
    
#     def prikazi_sliku(self, slika_path):
#         max_sirina = 500
#         max_visina = 500
        
        
#         img = Image.open(slika_path)
#         sirina, visina = img.size 
#         if sirina > visina: #ako slika vodoravna
#             if sirina > max_sirina or visina > max_visina:
#                 aspect_ratio = sirina / visina

#             if sirina > max_sirina:
#                 nova_sirina = max_sirina
#                 nova_visina = int(max_sirina / aspect_ratio)
#             else:
#                 nova_visina = max_visina
#                 nova_sirina = int(max_visina * aspect_ratio)
        
#         else: #ako slika nije vodoravna
#             if visina > max_sirina or sirina > max_visina:
#                 aspect_ratio = visina / sirina

#             if visina > max_sirina:
#                 nova_visina = max_sirina
#                 nova_sirina = int(max_visina / aspect_ratio)
#             else:
#                 nova_sirina = max_sirina
#                 nova_visina = int(max_sirina * aspect_ratio)
#         )
#         img = img.resize((nova_sirina, nova_visina))
        
#         img_tk = ImageTk.PhotoImage(img)
#         self.label.config(image=img_tk)
#         self.label.img = img_tk
    
#     def dodaj_sliku(self):
        
#         self.slika_path= filedialog.askopenfilename(filetypes=[("Slike", "*.jpg")])
#         if self.slika_path:
#             self.prikazi_sliku(self.slika_path)

#     def menjanje_kontrasta(self):
#         skala= Scale(self.root, from_=0, to=100, orient=HORIZONTAL, command=self.promeni_kontast)
#         promeni_kontrast(self.slika_path, skala)
#         self.slika.show()

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance

class GUI:

    def __init__(self, root):
        self.img12=None
        self.slika_path=None
        self.root = root
        self.root.title("Advanced Photoshop")
        self.root.geometry("1200x800")
        self.root.resizable(1, 1)
        self.root.config(bg="grey")
        self.slika_path = None
        if self.slika_path is not None:
             self.prikazi_sliku(self.slika_path)
        # Kreiranje label za prikaz slike na levoj strani
        self.label = tk.Label(self.root)
        self.label.pack(side="left")

        # Kreiranje gumba za dodavanje slike
        dodaj_sliku_button = tk.Button(self.root, text="Dodaj sliku", command=self.dodaj_sliku)
        dodaj_sliku_button.pack()

        # Kreiranje gumba za promenu kontrasta
        
        promeni_kontrast_button = tk.Button(self.root, text="Promeni kontrast", command=self.menjanje_kontrasta)
        promeni_kontrast_button.pack()

    def prikazi_sliku(self, pathSlike):
        max_sirina = 500
        max_visina = 500
        
        
        self.img = Image.open(pathSlike)
        sirina, visina = self.img.size 
        if sirina > visina: #ako slika vodoravna
            if sirina > max_sirina or visina > max_visina:
                aspect_ratio = sirina / visina

            if sirina > max_sirina:
                nova_sirina = max_sirina
                nova_visina = int(max_sirina / aspect_ratio)
            else:
                nova_visina = max_visina
                nova_sirina = int(max_visina * aspect_ratio)
        
        else: #ako slika nije vodoravna
            if visina > max_sirina or sirina > max_visina:
                aspect_ratio = visina / sirina

            if visina > max_sirina:
                nova_visina = max_sirina
                nova_sirina = int(max_visina / aspect_ratio)
            else:
                nova_sirina = max_sirina
                nova_visina = int(max_sirina * aspect_ratio)
        
        self.img1 = self.img.resize((nova_sirina, nova_visina))
        # img = Image.open(pathSlike)
        img_tk = ImageTk.PhotoImage(self.img1)
        self.label.config(image=img_tk)
        self.label.img1 = img_tk

    def menjanje_kontrasta(self):
        if self.slika_path:
            skala = Scale(self.root, from_=0, to=100, orient=HORIZONTAL, command=self.promeni_kontrast)
            skala.pack()
            # img = Image.open(self.slika_path)
            img_tk = ImageTk.PhotoImage(self.img1)
            self.label.config(image=img_tk)
            self.label.self.img1 = img_tk
            self.label.image = img_tk  # Dodajte ovu liniju kako biste sprečili gubljenje reference na sliku

    def promeni_kontrast(self, vrednost):
        if self.slika_path:
            # img = Image.open(self.slika_path)

            kontrast = float(vrednost) / 50.0  # Prilagodite ovaj faktor prema vašim potrebama
            enhancer = ImageEnhance.Contrast(self.img1)
            # self.img = enhancer.enhance(kontrast)
            self.img12 = enhancer.enhance(kontrast)
            img_tk = ImageTk.PhotoImage(self.img12)
            self.label.config(image=img_tk)
            self.label.img1 = img_tk

    def dodaj_sliku(self):
        self.slika_path = filedialog.askopenfilename(filetypes=[("Slike", "*.jpg")])
        if self.slika_path:
            self.prikazi_sliku(self.slika_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
