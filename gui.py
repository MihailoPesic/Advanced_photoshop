import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from main import promeni_kontast

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Photoshop")
        self.root.geometry("1200x800")
        self.root.resizable(1, 1)
        self.root.config(bg="grey")
        
        self.label = tk.Label(self.root)
        self.label.pack()

        dodaj_sliku_button = tk.Button(self.root, text="Dodaj sliku", command=self.dodaj_sliku)
        dodaj_sliku_button.pack()
        
    def prikazi_sliku(self, pathSlike):
        img = Image.open(pathSlike)
        img_tk = ImageTk.PhotoImage(img)
        self.label.config(image=img_tk)
        self.label.img = img_tk
    
    def dodaj_sliku(self):
        slika_path = filedialog.askopenfilename(filetypes=[("Slike", "*.jpg")])
        if slika_path:
            self.prikazi_sliku(slika_path)

    def menjanje_kontrasta(self):
        
        promeni_kontast(self.slika_path, self.vrednost)