import qrcode

# Enter link to genrate QR code
link = input("Enter link to generate QR code: ")
# link = "https://www.linkedin.com/"

# Edit the size of the qr code box and border
qr = qrcode.QRCode(
    version = 1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size = 19,
    border = 1,
)

qr.add_data(link)
qr_img = qr.make_image(fill_color="black", back_color="white")

qr_img.save("qrcode.png")
