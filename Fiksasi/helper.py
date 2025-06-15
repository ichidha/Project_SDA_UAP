#buat shadow teks
def draw_shadow_text(canvas, x, y, text):
    for dx, dy, color in [(0, 4, "white"), (1, 3, "black"), (3, 0, "orange")]:
        canvas.create_text(x + dx, y + dy, text=text, font=("Forte", 68, "bold"), fill=color)
