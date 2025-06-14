# def draw_shadow_text(canvas, x, y, text):
#     offsets = [(-2, -2), (2, -2), (-2, 2), (2, 2)]
#     for dx, dy in offsets:
#         canvas.create_text(x + dx, y + dy, text=text, font=("Forte", 56, "bold"), fill="white")
#     canvas.create_text(x, y, text=text, font=("Forte", 56, "bold"), fill="orange")
def draw_shadow_text(canvas, x, y, text):
    for dx, dy, color in [(0, 4, "white"), (1, 3, "black"), (3, 0, "orange")]:
        canvas.create_text(x + dx, y + dy, text=text, font=("Forte", 68, "bold"), fill=color)