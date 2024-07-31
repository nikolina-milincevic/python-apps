import qrcode

# pip install pillow --> in a terminal

image = qrcode.make("https://127.0.0.1:8000")
image.save("app18-restaurant-menu/qr.png")
