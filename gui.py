import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance, ImageFilter
import customtkinter
import cv2
import matplotlib.pyplot as plt
import numpy as np



class GUI:
    
    def __init__(self, root):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.skala_za_crop_down = None
        self.skala_za_crop_up = None
        self.skala_za_crop_left = None
        self.skala_za_crop_right = None
        self.skala_za_ostrinu = None
        self.skala_za_kontrast = None
        self.skala_za_osvetljenje=None
        self.skala_za_blur=None
        self.skala_za_boju=None
        self.img12=None
        self.slika_path=None
        self.root = root
        self.root.title("Advanced Photoshop")
        self.root.geometry("1200x800")
        self.root.resizable(1, 1)
        self.root.config(bg="#2d2d30")
        self.slika_path = None
        if self.slika_path is not None:
             self.prikazi_sliku(self.slika_path)
        left_frame = tk.Frame(self.root, bg="#2d2d30")
        global right_frame
        right_frame = tk.Frame(self.root, bg="#252526",padx=8)  
        left_frame.pack(side="left", padx=20, pady=20)
        right_frame.pack(side="right", fill="y", padx=20, pady=20)
        self.label = tk.Label(left_frame)
        self.label.pack(anchor="nw")
        
        
    
        
        global promeni_ostrinu_button
        global promeni_osvetljenje_button
        global promeni_boju_button
        global promeni_kontrast_button
        global bluruj_sliku_button
        # global crop_image_button
        #button = customtkinter.CTkButton(app, text="CTkButton", command=self.dodaj_sliku)

        dodaj_sliku_button = tk.Button(left_frame, text="Dodaj sliku",height = 2,width = 16, command=self.dodaj_sliku, bg="#2d2d30", foreground="white", bd= "4")
        dodaj_sliku_button.pack(fill="y", padx=10, pady=10, anchor="nw")
        
        promeni_ostrinu_button = tk.Button(right_frame, text="Promeni ostrinu",height = 1,width = 16, command=self.menjanje_ostrine, bg="#2d2d30", foreground="white", bd= "4")
        promeni_boju_button = tk.Button(right_frame, text="Promeni boju",height = 1,width = 16, command=self.menjanje_boje, bg="#2d2d30", foreground="white", bd = "4")
        
        cuvaj_na_cloud_button=tk.Button(right_frame,text="Cuvaj na cloud",height = 1,width = 16, command=self.cuvaj_na_cloud)
        promeni_kontrast_button = tk.Button(right_frame, text="Promeni kontrast",height = 1,width = 16, command=self.menjanje_kontrasta,bg="#2d2d30", foreground="white", bd= "4")
        promeni_osvetljenje_button = tk.Button(right_frame, text="Promeni osvetljenje",height = 1,width = 16, command=self.menjanje_osvetljenja,bg="#2d2d30", foreground="white",  bd= "4")
        okreni_za_devedeset_button = tk.Button(right_frame, text="Okreni sliku za 90°",height = 1,width = 16, command=self.rotate_slike, bg="#2d2d30", foreground="white",  bd= "4")
        bluruj_sliku_button = tk.Button(right_frame, text="Bluruj sliku", height = 1, width = 16, command= self.bluruj_sliku,  bg="#2d2d30", foreground="white",  bd= "4")
        # crop_image_button = tk.Button(right_frame, text = "Iseci sliku", height = 1, width = 16, command= self.menjanje_dimenzija,  bg="#2d2d30", foreground="white",  bd= "4")
        #konture_button = tk.Button(right_frame, text="Konture", height = 1, width = 16, command=izvuci_konture)
        
        sacuvaj_promene_button=tk.Button(right_frame, text="Sacuvaj promene",height = 1,width = 16, command=self.cuvanje_slike, bg= "#3e3e42", foreground="white", bd = "4")
        save_picture_dialog_button = tk.Button(right_frame, text="Sacuvaj sliku nakon editovanja", command=self.save_picture_dialog, bg= "#3e3e42", foreground="white", bd = "4")
        
        
        promeni_osvetljenje_button.pack(pady=10)
        okreni_za_devedeset_button.pack(pady=10)
        promeni_kontrast_button.pack(pady=10)
        promeni_boju_button.pack(pady=10)
        bluruj_sliku_button.pack(pady=10)
        #konture_button.pack()
        # crop_image_button.pack(pady=10)
        promeni_ostrinu_button.pack(pady=10)
        
        sacuvaj_promene_button.pack(pady=10)
        save_picture_dialog_button.pack(pady=10)
        cuvaj_na_cloud_button.pack(pady=10)
        


    def prikazi_sliku(self, pathSlike):
        max_sirina = 710
        max_visina = 710
        
        
        self.img = Image.open(pathSlike)
        self.img13=self.img
        sirina, visina = self.img.size 
        aspect_ratio = visina / sirina
        if sirina > visina: #ako slika vodoravna
            if sirina > max_sirina or visina > max_visina:
                aspect_ratio = sirina / visina

            if sirina > max_sirina:
                nova_sirina = max_sirina
                nova_visina = int(max_sirina / aspect_ratio)
            else:
                nova_visina = max_visina
                nova_sirina = int(max_visina * aspect_ratio)
        elif sirina < visina: 
            if visina > max_sirina or sirina > max_visina:
                aspect_ratio = visina / sirina

            if visina > max_sirina:
                nova_visina = max_sirina
                nova_sirina = int(max_visina / aspect_ratio)
            else:
                nova_sirina = max_sirina
                nova_visina = int(max_sirina * aspect_ratio)
        
        self.img1 = self.img.resize((nova_sirina, nova_visina))
        
        img_tk = ImageTk.PhotoImage(self.img1)
        self.label.config(image=img_tk)

        self.label.img = img_tk
    

    # def canny(self):
    #     # img = self.img1.convert('L')
    #     # img2 = self.img.convert('L')
    #     # img_blur = cv2.GaussianBlur(img, (3,3), 0)
    #     # img_blur2=cv2.GaussianBlur(img2, (3,3), 0)
    #     # cv2.Canny(img_blur,20,30)
    #     # cv2.Canny(img_blur2,20,30)
    #     # self.img1=img_blur
    #     # self.img=img_blur2
    #     img_cv1 = cv2.cvtColor(np.array(self.img1), cv2.COLOR_RGB2BGR)
    #     img_cv2 = cv2.cvtColor(np.array(self.img), cv2.COLOR_RGB2BGR)

    #     # Convert images to grayscale
    #     img_gray1 = cv2.cvtColor(img_cv1, cv2.COLOR_BGR2GRAY)
    #     img_gray2 = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2GRAY)

    #     # Apply Gaussian blur
    #     img_blur1 = cv2.GaussianBlur(img_gray1, (3, 3), 0)
    #     img_blur2 = cv2.GaussianBlur(img_gray2, (3, 3), 0)

    #     # Apply Canny edge detection
    #     self.img1 = cv2.Canny(img_blur1, 20, 30)
    #     self.img = cv2.Canny(img_blur2, 20, 30)
    # def menjanje_dimenzija(self):
    #     if self.slika_path:
    #         if self.skala_za_crop_down is None or self.skala_za_crop_up is None or self.skala_za_crop_left is None or self.skala_za_crop_right:
    #             self.skala_za_crop_up = Scale(crop_image_button,label="Gornji deo", from_=0, to=210, orient=HORIZONTAL, command=self.promeni_dimenziju,   bg="#2d2d30", fg="white", bd= "4")
    #             self.skala_za_crop_down = Scale(crop_image_button,label="Donji deo", from_=0, to=210, orient=HORIZONTAL, command=self.promeni_dimenziju,   bg="#2d2d30", fg="white", bd= "4")
    #             self.skala_za_crop_left = Scale(crop_image_button,label="Levi deo", from_=0, to=210, orient=HORIZONTAL, command=self.promeni_dimenziju,   bg="#2d2d30", fg="white", bd= "4")
    #             self.skala_za_crop_right = Scale(crop_image_button,label="Desni deo", from_=0, to=210, orient=HORIZONTAL, command=self.promeni_dimenziju,   bg="#2d2d30", fg="white", bd= "4")
    #             self.skala_za_crop_up.pack()
    #             self.skala_za_crop_down.pack()
    #             self.skala_za_crop_left.pack()
    #             self.skala_za_crop_right.pack()

    #             img_tk = ImageTk.PhotoImage(self.img1)
    #             self.label.config(image=img_tk)
    #             self.label.self.img1 = img_tk
    #             self.label.image = img_tk
    
    # def promeni_dimenziju(self, vrednost):
    #     if self.slika_path:
    #         pass
            
            
            
            

    def menjanje_ostrine(self):
        if self.slika_path:
            if self.skala_za_ostrinu is None:
                self.skala_za_ostrinu = Scale(promeni_ostrinu_button,label="Ostrina", from_=0, to=100, orient=HORIZONTAL, command=self.promeni_ostrinu,   bg="#2d2d30", fg="white", bd= "4")
                self.skala_za_ostrinu.pack()
                img_tk = ImageTk.PhotoImage(self.img1)
                self.label.config(image=img_tk)
                self.label.self.img1 = img_tk
                self.label.image = img_tk
    def promeni_ostrinu(self, vrednost):
        if self.slika_path:
            ostrina = float(vrednost) / 50.0  
            enhancer = ImageEnhance.Sharpness(self.img1)
            enhancer2=ImageEnhance.Sharpness(self.img)
            self.img12 = enhancer.enhance(ostrina)
            self.img13=enhancer2.enhance(ostrina)
            img_tk = ImageTk.PhotoImage(self.img12)
            self.label.config(image=img_tk)
            self.label.img1 = img_tk        
    def menjanje_boje(self):
        if self.slika_path:
            if self.skala_za_boju is None:
                self.skala_za_boju = Scale(promeni_boju_button,label="Saturacija", from_=0, to=100, orient=HORIZONTAL, command=self.promeni_boju,   bg="#2d2d30", fg="white", bd= "4")
                self.skala_za_boju.pack()
                img_tk = ImageTk.PhotoImage(self.img1)
                self.label.config(image=img_tk)
                self.label.img1 = img_tk
                self.label.image = img_tk
    def menjanje_kontrasta(self):
        global skala_za_kontrast
        if self.slika_path:
            if self.skala_za_kontrast is None:
                self.skala_za_kontrast = Scale(promeni_kontrast_button,label="Kontrast", from_=30, to=180, orient=HORIZONTAL, command=self.promeni_kontrast,   bg="#2d2d30", fg="white", bd= "4")
                self.skala_za_kontrast.pack()
                img_tk = ImageTk.PhotoImage(self.img1)
                self.label.config(image=img_tk)
                self.label.self.img1 = img_tk
                self.label.image = img_tk
    def promeni_boju(self, vrednost):
        if self.slika_path:
            boja = float(vrednost) / 50.0  
            enhancer = ImageEnhance.Color(self.img1)
            enhancer2=ImageEnhance.Color(self.img)
            self.img12 = enhancer.enhance(boja)
            self.img13 = enhancer2.enhance(boja)
            img_tk = ImageTk.PhotoImage(self.img12)
            self.label.config(image=img_tk)
            self.label.img1 = img_tk            
    def promeni_kontrast(self, vrednost):
        if self.slika_path:
            

            kontrast = float(vrednost) / 50.0  
            enhancer = ImageEnhance.Contrast(self.img1)
            enhancer2=ImageEnhance.Contrast(self.img)
            self.img12 = enhancer.enhance(kontrast)
            self.img13=enhancer2.enhance(kontrast)
            img_tk = ImageTk.PhotoImage(self.img12)
            self.label.config(image=img_tk)
            self.label.img1 = img_tk
    
    def menjanje_osvetljenja(self):
        if self.slika_path:
            if self.skala_za_osvetljenje is None:
                self.skala_za_osvetljenje = Scale(promeni_osvetljenje_button,label="Osvetljenje", from_=10, to=280, orient=HORIZONTAL, command=self.promeni_osvetljenje,   bg="#2d2d30", fg="white", bd= "4")
                self.skala_za_osvetljenje.pack()
                img_tk = ImageTk.PhotoImage(self.img1)
                self.label.config(image=img_tk)
                self.label.self.img1 = img_tk
                self.label.image = img_tk 
    def promeni_osvetljenje(self, vrednost):
        if self.slika_path:
            osvetljenje=float(vrednost)/50
            enhancer=ImageEnhance.Brightness(self.img1)
            enhancer2=ImageEnhance.Brightness(self.img)
            self.img12=enhancer.enhance(osvetljenje)
            self.img13=enhancer2.enhance(osvetljenje)
            img_tk=ImageTk.PhotoImage(self.img12)
            self.label.config(image=img_tk)
            self.label.img1 = img_tk
            
    def rotate_slike(self):
        if self.slika_path:
            angle = 90
            out = self.img1.rotate(angle, expand=True)
            out2=self.img13.rotate(angle, expand=True)
            self.img12=out
            self.img13=out2
            img_tk = ImageTk.PhotoImage(out)
            img_tk2=ImageTk.PhotoImage(out2)
            self.label.config(image=img_tk)
            self.label.img1 = img_tk
            
            self.img1=self.img12
            
    
    def bluruj_sliku(self):
        if self.slika_path:
            if self.skala_za_blur is None:
                self.skala_za_blur = Scale(bluruj_sliku_button,label="Blur", from_=0, to=210, orient=HORIZONTAL, command=self.promeni_blur,  bg="#2d2d30", fg="white", bd= "4")
                self.skala_za_blur.pack()
                img_tk = ImageTk.PhotoImage(self.img1)
                self.label.config(image=img_tk)
                self.label.self.img1 = img_tk
                self.label.image = img_tk
    # def izvuci_konture(self):
    #     if self.slika_path:
    #         if self.skala_za_konture is None:
    #             self.skala_za_konture = Scale(izvuci_konture_button,label="Konture", from_=0, to=210, orient=HORIZONTAL, command=self.promeni_konture)
    #             self.skala_za_konture.pack()
    #             img_tk = ImageTk.PhotoImage(self.img1)
    #             self.label.config(image=img_tk)
    #             self.label.self.img1 = img_tk
    #             self.label.image = img_tk
    def promeni_blur(self, vrednost):
        if self.slika_path:
            blur=float(vrednost)/50.0
            blurovana_slika = self.img1.filter(ImageFilter.GaussianBlur(blur))
            blurovana_slika2=self.img.filter(ImageFilter.GaussianBlur(blur))
            self.img12=blurovana_slika
            self.img13=blurovana_slika2
            img_tk=ImageTk.PhotoImage(self.img12)
            self.label.config(image=img_tk)
            self.label.img1 = img_tk  
    def dodaj_sliku(self):
        
        self.slika_path = filedialog.askopenfilename(filetypes=[("Slike", "*.jpg")])
        if self.slika_path:
            self.prikazi_sliku(self.slika_path)
    def cuvanje_slike(self):
        # images_preview.append(self.img12)
        # images.append(self.img)
        self.img1=self.img12
        self.img=self.img13
        #self.img=
    
    
    # def crop_image(self):
    #     if self.slika_path:
    #          if self.skala_za_crop is None:
    #             self.skala_za_crop_up = Scale(crop_image_button,label="Blur", from_=0, to=210, orient=HORIZONTAL, command=self.crop_image)
    #             self.skala_za_crop_down = Scale(crop_image_button,label="Blur", from_=0, to=210, orient=HORIZONTAL, command=self.crop_image)
    #             self.skala_za_crop_left = Scale(crop_image_button,label="Blur", from_=0, to=210, orient=HORIZONTAL, command=self.crop_image)
    #             self.skala_za_crop_right = Scale(crop_image_button,label="Blur", from_=0, to=210, orient=HORIZONTAL, command=self.crop_image)
    #             self.skala_za_crop.pack()
    #             img_tk = ImageTk.PhotoImage(self.img1)
    #             self.label.config(image=img_tk)
    #             self.label.self.img1 = img_tk
    #             self.label.image = img_tk
    
    # def crop_image

    # def save_picture_dialog(self):
    #     root = tk.Tk()
    #     root.withdraw()  # Hide the main window

    #     file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        
    #     if file_path:
    #         try:
    #             image.save(file_path)
    #             print("Image saved successfully!")
    #         except Exception as e:
    #             print(f"Error saving the image: {e}")
    
    #     root.destroy()
    def save_picture_dialog(self):
        if self.slika_path:
            file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")])
        
            if file_path:
                try:
                    self.img.save(file_path)
                    print("Image saved successfully!")
                except Exception as e:
                    print(f"Error saving the image: {e}")

    def cuvaj_na_cloud(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()


