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
        canvas.create_image(0, 0, image=self.controller.bgproject_image, anchor="nw")

        #input nama
        self.ao_name = tk.Entry(self)
        self.aka_name = tk.Entry(self)
        canvas.create_window(300, 80, window=self.ao_name)
        canvas.create_window(870, 80, window=self.aka_name)

        #input divisi
        self.division_entry = tk.Entry(self)
        canvas.create_window(550, 30, window=self.division_entry)

        #memilih gaya/jurus
        gaya_list = ["Shotokan", "Shito-Ryu", "Goju-Ryu", "Wado-Ryu"]
        self.ao_style_var = tk.StringVar(value="Pilih Gaya")
        ao_dropdown = tk.OptionMenu(self, self.ao_style_var, *gaya_list)
        canvas.create_window(290, 120, window=ao_dropdown)
        self.aka_style_var = tk.StringVar(value="Pilih Gaya")
        aka_dropdown = tk.OptionMenu(self, self.aka_style_var, *gaya_list)
        canvas.create_window(860, 120, window=aka_dropdown)

        #tampilan score biru(ao) dan merah(aka)
        self.ao_score_label = tk.Label(self, text="0", font=("Arial", 100), bg="blue", fg="white")
        self.aka_score_label = tk.Label(self, text="0", font=("Arial", 100), bg="red", fg="white")
        canvas.create_window(135, 300, window=self.ao_score_label)
        canvas.create_window(685, 300, window=self.aka_score_label)

        #tombol update score pada sisi biru(ao)
        tk.Button(self, text="+1", command=lambda: self.update_score('Ao', 1)).place(x=100, y=385)
        tk.Button(self, text="-1", command=lambda: self.update_score('Ao', -1)).place(x=150, y=385)
        #tombol update score pada sisi merah(aka)
        tk.Button(self, text="+1", command=lambda: self.update_score('Aka', 1)).place(x=650, y=385)
        tk.Button(self, text="-1", command=lambda: self.update_score('Aka', -1)).place(x=700, y=385)

        #tombol simpan score ke csv
        tk.Button(self, text="Simpan", command=self.save_scores).place(x=525, y=600)
        #tombol mereset (nama, score, waktu)
        tk.Button(self, text="Reset", command=self.reset_scores).place(x=1000, y=600)

        #tombol back
        back_btn = tk.Button(self, image=self.controller.btn_back, borderwidth=0,command=lambda: controller.show_frame("MenuPage"), cursor="hand2")
        back_btn.place(x=950, y=25)

        self.timer_running = False
        self.ao_time = 0
        self.aka_time = 0

        #mengatur font dan posisi timer
        self.ao_timer_label = tk.Label(self, text="00:00", font=("Arial", 40), bg="blue", fg="white")
        self.aka_timer_label = tk.Label(self, text="00:00", font=("Arial", 40), bg="red", fg="white")
        self.ao_timer_label.place(x=270, y=440)
        self.aka_timer_label.place(x=840, y=440)

        #tombol start timer
        self.timer_button = tk.Button(self, text="Start", command=self.toggle_timer)
        canvas.create_window(550, 530, window=self.timer_button)

        #tombol shikkaku dan kikken pada sisi biru(ao)
        tk.Button(self, text="Shikkaku ", bg="blue", fg="white", command=self.shikkaku_ao).place(x=300, y=600)
        tk.Button(self, text="Kikken ", bg="blue", fg="white", command=self.kikken_ao).place(x=400, y=600)
        #tombol shikkaku dan kikken pada sisi merah(aka)
        tk.Button(self, text="Shikkaku ", bg="red", fg="white", command=self.shikkaku_aka).place(x=650, y=600)
        tk.Button(self, text="Kikken ", bg="red", fg="white", command=self.kikken_aka).place(x=750, y=600)

        #tombol hide/show stopwatch 
        self.timer_visible = True
        self.toggle_timer_visibility_button = tk.Button(self, text="Hide Stopwatch", command=self.toggle_timer_visibility)
        canvas.create_window(100, 615, window=self.toggle_timer_visibility_button)

    #fungsi mengupdate score
    def update_score(self, side, change):
        if side == 'Ao':
            self.ao_score = max(0, self.ao_score + change)
            self.ao_score_label.config(text=str(self.ao_score))
        else:
            self.aka_score = max(0, self.aka_score + change)
            self.aka_score_label.config(text=str(self.aka_score))

    #fungsi menyimpan score di csv
    def save_scores(self):
        ao = self.ao_name.get()
        aka = self.aka_name.get()
        division = self.division_entry.get()

        if not ao or not aka or not division:
            messagebox.showwarning("Input Kosong", "Nama dan Divisi harus diisi!")
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
            data.append([ao, 'Ao', self.ao_score, self.ao_style_var.get(), division])
            data.append([aka, 'Aka', self.aka_score, self.aka_style_var.get(), division])

        with open(self.csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        messagebox.showinfo("Berhasil", "Skor berhasil disimpan.")

    #fungsi mereset score & nama & timer
    def reset_scores(self):
        self.ao_score = 0
        self.aka_score = 0
        self.ao_score_label.config(text='0')
        self.aka_score_label.config(text='0')
        self.ao_name.delete(0, tk.END)
        self.aka_name.delete(0, tk.END)
        self.division_entry.delete(0, tk.END)
        self.timer_running = False
        self.ao_time = 0
        self.aka_time = 0
        self.ao_timer_label.config(text="00:00")
        self.aka_timer_label.config(text="00:00")
        self.timer_button.config(text="Start")
        messagebox.showinfo("Reset", "berhasil direset.")

    #fungsi membuat tombol mulai timer
    def toggle_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.timer_button.config(text="Stop")
            self.update_timers()
        else:
            self.timer_running = False
            self.timer_button.config(text="Start")
            self.ao_time = 0
            self.aka_time = 0
            self.ao_timer_label.config(text="00:00")
            self.aka_timer_label.config(text="00:00")

    #fungsi membuat update timer
    def update_timers(self):
        if self.timer_running:
            self.ao_time += 1
            self.aka_time += 1
            ao_minutes, ao_seconds = divmod(self.ao_time, 60)
            aka_minutes, aka_seconds = divmod(self.aka_time, 60)
            self.ao_timer_label.config(text=f"{ao_minutes:02d}:{ao_seconds:02d}")
            self.aka_timer_label.config(text=f"{aka_minutes:02d}:{aka_seconds:02d}")
            self.after(1000, self.update_timers)

    #fungsi untuk shikkaku pada biru(ao)
    def shikkaku_ao(self):
        confirm = messagebox.askyesno("Konfirmasi", "Apakah Ao (biru) didiskualifikasi (Shikkaku)?")
        if confirm:
            self.aka_score = 8
            self.ao_score = 0
            self.aka_score_label.config(text='8')
            self.ao_score_label.config(text='0')

    #fungsi untuk kikken pada biru(ao)
    def kikken_ao(self):
        confirm = messagebox.askyesno("Konfirmasi", "Apakah Ao (biru) mengundurkan diri (Kikken)?")
        if confirm:
            self.aka_score = 8
            self.ao_score = 0
            self.aka_score_label.config(text='8')
            self.ao_score_label.config(text='0')

    #fungsi untuk shikkaku pada merah(aka)
    def shikkaku_aka(self):
        confirm = messagebox.askyesno("Konfirmasi", "Apakah Aka (merah) didiskualifikasi (Shikkaku)?")
        if confirm:
            self.ao_score = 8
            self.aka_score = 0
            self.ao_score_label.config(text='8')
            self.aka_score_label.config(text='0')

    #fungsi untuk kikken pada merah(aka)
    def kikken_aka(self):
        confirm = messagebox.askyesno("Konfirmasi", "Apakah Aka (merah) mengundurkan diri (Kikken)?")
        if confirm:
            self.ao_score = 8
            self.aka_score = 0
            self.ao_score_label.config(text='8')
            self.aka_score_label.config(text='0')

    #fungsi untuk menghide timer
    def toggle_timer_visibility(self):
        if self.timer_visible:
            self.ao_timer_label.place_forget()
            self.aka_timer_label.place_forget()
            self.toggle_timer_visibility_button.config(text="Show Stopwatch")
        else:
            self.ao_timer_label.place(x=270, y=440)
            self.aka_timer_label.place(x=840, y=440)
            self.toggle_timer_visibility_button.config(text="Hide Stopwatch")
        self.timer_visible = not self.timer_visible
