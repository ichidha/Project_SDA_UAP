import tkinter as tk
from PIL import Image, ImageTk

class ProfilePage(tk.Frame):
    def __init__(self, controller, profile_id):
        super().__init__(controller)
        self.controller = controller

        canvas = tk.Canvas(self, width=1100, height=650)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.controller.bgprofil_image, anchor="nw")

        data = self.controller.profil_data.get(profile_id)
        if data:
            try:
                image = Image.open(data["foto"]).resize((200, 250), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                canvas.create_image(350, 300, image=photo)
                canvas.image = photo
            except Exception as e:
                print(f"Foto tidak ditemukan: {e}")
            detail = (
                f"Nama: {data['nama']}\n"
                f"Nickname: {data['nickname']}\n"
                f"Tempat tgl Lahir: {data['tempat_lahir']}, {data['lahir']}\n"
                f"Golongan darah: {data['gol_darah']}\n"
                f"NPM: {data['npm']}\n"
                f"Alamat: {data['alamat']}\n"
                f"Email: {data['email']}\n"
                f"Motto hidup: {data['motto']}\n"
                f"Hobi: {data['hobi']}")
            canvas.create_text(500, 150, text=data["nama"], font=("Forte", 36, "bold"), fill="orange", anchor="nw")
            canvas.create_text(500, 200, text=detail, font=("Arial", 12), fill="white", anchor="nw")

        back_btn = tk.Button(self, image=self.controller.btn_back, borderwidth=0,command=lambda: controller.show_frame("TeamPage"), cursor="hand2")
        canvas.create_window(895, 575, window=back_btn)

