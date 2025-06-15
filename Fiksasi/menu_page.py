import tkinter as tk

class MenuPage(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller)
        self.controller = controller

        canvas = tk.Canvas(self, width=1100, height=650)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.controller.bg2_image, anchor="nw")

        for x in [275, 825]:
            for y in [230, 340]:
                canvas.create_text(x, y, text="_____", font=("Forte", 68, "bold"), fill="white")
            for y in [245 ,325]:
                canvas.create_text(x, y, text="____", font=("Forte", 68, "bold"), fill="white")
        
        project_btn = tk.Button(self, image=self.controller.btn_project, borderwidth=0,command=lambda: controller.show_frame("ProjectPage"), cursor="hand2")
        canvas.create_window(275, 325, window=project_btn)

        team_btn = tk.Button(self, image=self.controller.btn_team, borderwidth=0,command=lambda: controller.show_frame("TeamPage"), cursor="hand2")
        canvas.create_window(825, 325, window=team_btn)

        back_btn = tk.Button(self, image=self.controller.btn_back, borderwidth=0,command=lambda: controller.show_frame("WelcomePage"), cursor="hand2")
        canvas.create_window(895, 575, window=back_btn)
