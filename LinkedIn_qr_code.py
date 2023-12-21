import qrcode
from PIL import Image

# Enter link to genrate qr code
# link = input("Enter your LinkedIn Profile URL: ")
link = "Hello World!"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(link)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white")

background_img = Image.open("Background.png")

qr_img = qr_img.resize(background_img.size, Image.ANTIALIAS)

merged_img = Image.alpha_composite(background_img.convert("RGBA"), qr_img.convert("RGBA"))

merged_img.save("myqrcode.png")
