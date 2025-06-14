# project_page.py
import tkinter as tk
from tkinter import messagebox
import csv
import os

class ProjectPage(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller
        self.csv_file = 'skor.csv'
        self.ao_score = 0
        self.aka_score = 0

        canvas = tk.Canvas(self, width=1100, height=650)
        canvas.pack(fill="both", expand=True)
        canvas.create_rectangle(0, 0, 1100, 650, fill='gray20')

        self.ao_name = tk.Entry(self)
        self.aka_name = tk.Entry(self)
        canvas.create_window(200, 50, window=self.ao_name)
        canvas.create_window(900, 50, window=self.aka_name)

        self.ao_score_label = tk.Label(self, text="0", font=("Arial", 48), bg="blue", fg="white")
        self.aka_score_label = tk.Label(self, text="0", font=("Arial", 48), bg="red", fg="white")
        canvas.create_window(200, 150, window=self.ao_score_label)
        canvas.create_window(900, 150, window=self.aka_score_label)

        tk.Button(self, text="+1", command=lambda: self.update_score('Ao', 1)).place(x=170, y=230)
        tk.Button(self, text="-1", command=lambda: self.update_score('Ao', -1)).place(x=220, y=230)
        tk.Button(self, text="+1", command=lambda: self.update_score('Aka', 1)).place(x=870, y=230)
        tk.Button(self, text="-1", command=lambda: self.update_score('Aka', -1)).place(x=920, y=230)

        tk.Button(self, text="Simpan", command=self.save_scores).place(x=500, y=300)
        tk.Button(self, text="Reset", command=self.reset_scores).place(x=600, y=300)

        back_btn = tk.Button(self, image=self.controller.btn_back, borderwidth=0,command=lambda: controller.show_frame("MenuPage"), cursor="hand2")
        back_btn.place(x=895, y=575)

    def update_score(self, side, change):
        if side == 'Ao':
            self.ao_score = max(0, self.ao_score + change)
            self.ao_score_label.config(text=str(self.ao_score))
        else:
            self.aka_score = max(0, self.aka_score + change)
            self.aka_score_label.config(text=str(self.aka_score))

    def save_scores(self):
        ao = self.ao_name.get()
        aka = self.aka_name.get()
        if not ao or not aka:
            messagebox.showwarning("Input Kosong", "Nama harus diisi!")
            return

        data = []
        if os.path.exists(self.csv_file):
            with open(self.csv_file, 'r', newline='') as file:
                reader = csv.reader(file)
                data = list(reader)

        updated = False
        for row in data:
            if row[0] == ao and row[1] == 'Ao':
                row[2] = str(self.ao_score)
                updated = True
            elif row[0] == aka and row[1] == 'Aka':
                row[2] = str(self.aka_score)
                updated = True

        if not updated:
            data.append([ao, 'Ao', self.ao_score])
            data.append([aka, 'Aka', self.aka_score])

        with open(self.csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        messagebox.showinfo("Berhasil", "Skor berhasil disimpan.")

    def reset_scores(self):
        self.ao_score = 0
        self.aka_score = 0
        self.ao_score_label.config(text='0')
        self.aka_score_label.config(text='0')
        self.ao_name.delete(0, tk.END)
        self.aka_name.delete(0, tk.END)
        messagebox.showinfo("Reset", "Skor berhasil direset.")
