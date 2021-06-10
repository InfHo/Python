# importiere QR Modul
import qrcode

# zu verschlüsselnde Daten
data = "https://infho.eu/"

# verschlüssele Daten mit der make-Funktion
img = qrcode.make(data)

# speichere bild 
img.save('qr_code_infho.png')
