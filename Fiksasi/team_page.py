import tkinter as tk

class TeamPage(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller

        canvas = tk.Canvas(self, width=1100, height=650)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.controller.bgAllName_image, anchor="nw")

        back_btn = tk.Button(self, image=self.controller.btn_back, borderwidth=0,command=lambda: controller.show_frame("MenuPage"), cursor="hand2")
        canvas.create_window(895, 575, window=back_btn)

        canvas.create_window(270, 200, window=tk.Button(self, image=self.controller.btn_nrd, borderwidth=0,
                                                        command=lambda: controller.show_frame("ProfilDhn"), cursor="hand2"))
        canvas.create_window(270, 300, window=tk.Button(self, image=self.controller.btn_muti, borderwidth=0,
                                                        command=lambda: controller.show_frame("ProfilMuti"), cursor="hand2"))
        canvas.create_window(850, 200, window=tk.Button(self, image=self.controller.btn_via, borderwidth=0,
                                                        command=lambda: controller.show_frame("ProfilVia"), cursor="hand2"))
        canvas.create_window(850, 300, window=tk.Button(self, image=self.controller.btn_fx, borderwidth=0,
                                                        command=lambda: controller.show_frame("ProfilFx"), cursor="hand2"))
