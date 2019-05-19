from PIL import Image, ImageDraw

W, H = (300,200)
msg = "Hello"

im = Image.open('bac.png')
draw = ImageDraw.Draw(im)
w, h = draw.textsize(msg)

# Смещение оси X(ширине).
axial_shift = 0

w_calculate = ((W-w) / 2)-axial_shift

draw.text((w_calculate,(H-h)/2), msg, fill="black")
im.save("Hello.png", "PNG")