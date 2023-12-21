import qrcode
from PIL import Image

# Enter link to genrate qr code
# link = input("Enter your LinkedIn Profile URL: ")
link = "Hello World!"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=1,
    border=1,
)
qr.add_data(link)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white")

background_img = Image.open("Background.png")

qr_position = (
    (background_img.width // 4),
    (background_img.height // 2)
)

qr_img = qr_img.resize(background_img.size, Image.Resampling.LANCZOS)

merged_img = Image.new("RGBA", background_img.size, (0, 0, 0, 0))
merged_img.paste(background_img.convert("RGBA"), (0, 0))
merged_img.paste(qr_img.convert("RGBA"), qr_position, qr_img.convert("RGBA"))

merged_img.save("myqrcode.png")
