import qrcode

# URL of your public website
url = "https://vitthal22.github.io/Personal-ID/"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save("your_website_qr.png")

print("QR code generated and saved as your_website_qr.png")
