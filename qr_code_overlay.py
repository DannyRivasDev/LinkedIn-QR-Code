from PIL import Image

# Use these values to position the qr code (horizontal, vertical)
overlay_position = (250, 1000)

background_img = Image.open("background.png")

overlay_img = Image.open("myqrcode.png").convert("RGBA")

background_img.paste(overlay_img, overlay_position, overlay_img)

background_img.save("qr_code_wallpaper.png")

