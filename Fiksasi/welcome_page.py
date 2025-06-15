# welcome_page.py
import tkinter as tk
from helper import draw_shadow_text

class WelcomePage(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller

        canvas = tk.Canvas(self, width=1100, height=650)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.controller.bg_image, anchor="nw")

        #shadow teks
        draw_shadow_text(canvas, 547, 100, "WELCOME")
        draw_shadow_text(canvas, 547, 175, "TO OUR")
        draw_shadow_text(canvas, 547, 250, "PROJECT")

        #tombol start
        start_btn = tk.Button(self, image=self.controller.btn_start, borderwidth=0,command=lambda: controller.show_frame("MenuPage"), cursor="hand2")
        canvas.create_window(550, 420, window=start_btn)

        #tombol exit
        exit_btn = tk.Button(self, image=self.controller.btn_exit, borderwidth=0,command=lambda: quit(), cursor="hand2")
        canvas.create_window(550, 500, window=exit_btn)
