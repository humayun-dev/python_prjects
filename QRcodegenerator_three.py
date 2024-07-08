# install qrcode module via pip install qrcode and import as shown below
# Two important functions are used such as make() and save().

'''
# Part - I QR Code with default design 

import qrcode as qr

image = qr.make("https://www.uetmardan.edu.pk/uetm/")
image.save("uetmardan.png")

'''

# Part II - QR Code with modified design
import qrcode
from PIL import Image   # for modified QR Code

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=4)
qr.add_data("https://www.uetmardan.edu.pk/uetm/")
qr.make(fit=True)
img = qr.make_image(fill_color="red",back_color="white") # image color and its background color 
img.save("modifieduetmardan.png")   # save image with the name.extension

'''
    version = 1 is the smallest which is 21 * 21 matrix
    error_correction is the level of the correction to be corrected such as high(30%),low(7%),Medium(15%)
    box size is the number of the pixels of each box of the QR Code
    border is the thickness of the boxes border
'''

