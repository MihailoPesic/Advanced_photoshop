from gui import GUI
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance

# def promeni_kontrast(slika, vrednost):
    # ImageEnhance.Contrast(slika).enchance(vrednost)

# def promeni_osvetljenje(slika, vrednost):
#     ImageEnhance.Brightness(slika).enhance(vrednost)

# def promeni_boju(slika, vrednost):
#     ImageEnhance.Color(slika).enhance(vrednost)

# def promeni_ostrinu(slika, vrednost):
#     ImageEnhance.Sharpness(slika).enhance(vrednost)

def main():
    root = tk.Tk()

    app = GUI(root)

    root.mainloop()

if __name__ == "__main__":
    main()

    



