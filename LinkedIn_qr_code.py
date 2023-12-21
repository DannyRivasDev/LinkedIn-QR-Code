import qrcode

# Enter link to genrate qr code
# link = input("Enter your LinkedIn Profile URL: ")
link = "Hello World!"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=25,
    border=1,
)

qr.add_data(link)
qr_img = qr.make_image(fill_color="black", back_color="white")

qr_img.save("qrcode.png")
