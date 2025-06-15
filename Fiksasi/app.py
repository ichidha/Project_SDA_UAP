from welcome_page import WelcomePage
from menu_page import MenuPage
from team_page import TeamPage
from profile_page import ProfilePage
from project_page import ProjectPage

import tkinter as tk
from PIL import Image, ImageTk
import csv
import os

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Welcome Page")
        self.geometry("1100x650")
        self.resizable(False, False)

        self.frames = {}
        self.load_images()
        self.load_profil_data()
        self.create_frames()
        self.show_frame("WelcomePage")

    def load_images(self):
        self.bg_image = ImageTk.PhotoImage(Image.open("assets/sunset_bg.png"))
        self.bg2_image = ImageTk.PhotoImage(Image.open("assets/sunset_bg2.png"))
        self.bgAllName_image = ImageTk.PhotoImage(Image.open("assets/sunset_bg3.png"))
        self.bgprofil_image = ImageTk.PhotoImage(Image.open("assets/profil_bg.png"))
        self.bgproject_image = ImageTk.PhotoImage(Image.open("assets/project_bg.png"))
        

        self.btn_start = ImageTk.PhotoImage(Image.open("assets/start_button.png").resize((150, 35)))
        self.btn_exit = ImageTk.PhotoImage(Image.open("assets/exit_button.png").resize((150, 35)))
        self.btn_project = ImageTk.PhotoImage(Image.open("assets/project_button.png").resize((190, 55)))
        self.btn_team = ImageTk.PhotoImage(Image.open("assets/team_button.png").resize((190, 55)))
        self.btn_back = ImageTk.PhotoImage(Image.open("assets/back_button.png").resize((131, 41)))

        self.btn_nrd = ImageTk.PhotoImage(Image.open("assets/Nur Ramadhani.png").resize((230, 60)))
        self.btn_fx = ImageTk.PhotoImage(Image.open("assets/FX Novryandika W..png").resize((230, 60)))
        self.btn_via = ImageTk.PhotoImage(Image.open("assets/Viandra T. Agsatri.png").resize((230, 60)))
        self.btn_muti = ImageTk.PhotoImage(Image.open("assets/Muthia Zhafira.png").resize((230, 60)))

    def load_profil_data(self):
        self.profil_data = {}
        try:
            with open("profil_data.csv", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.profil_data[row["id"]] = row
        except FileNotFoundError:
            print("File profil_data.csv tidak ditemukan.")

    def create_frames(self):
        self.frames["WelcomePage"] = WelcomePage(self)
        self.frames["MenuPage"] = MenuPage(self)
        self.frames["TeamPage"] = TeamPage(self)
        self.frames["ProfilDhn"] = ProfilePage(self, "dhn")
        self.frames["ProfilFx"] = ProfilePage(self, "fx")
        self.frames["ProfilVia"] = ProfilePage(self, "via")
        self.frames["ProfilMuti"] = ProfilePage(self, "muti")
        self.frames["ProjectPage"] = ProjectPage(self)

        for frame in self.frames.values():
            frame.place(x=0, y=0, width=1100, height=650)

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
