# importiere QR Modul
import qrcode

# zu verschlüsselnde Daten
data = "https://infho.eu/"
  
# erstelle eine Instanz der QRCode Klasse
qr = qrcode.QRCode(version = 1,
                   box_size = 10,
                   border = 5)
  
# Füge Daten zur Instanz 'qr' hinzu
qr.add_data(data)
  
qr.make(fit = True)
img = qr.make_image(fill_color = 'red',
                    back_color = 'blue')
  
# speichere bild 
img.save('qr_code_infho_2.png')
