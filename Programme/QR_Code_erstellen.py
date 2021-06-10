import qrcode

data = "https://infho.eu/"

img = qrcode.make(data)

img.save('qr_code_infho.png')
