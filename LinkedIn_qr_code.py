import qrcode

# Enter link to genrate qr code
link = input("Enter your LinkedIn Profile URL: ")
img = qrcode.make(link)

img.save("myqrcode.png")