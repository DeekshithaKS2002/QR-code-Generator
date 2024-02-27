import qrcode

features = qrcode.QRCode(version=1, box_size=40, border=3)

features.add_data("https://github.com/DeekshithaKS2002/QR-code-Generator")
features.make(fit=True)
image = features.make_image(fill_color="black", back_color="white")
image.save('image.png')
