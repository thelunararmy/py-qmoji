'''
Created on Jun 24, 2019

@author: thelunararmy
'''
# External deps
import qrcode
import numpy as np
import emoji 

# Internal deps
import io
import warnings

if __name__ == '__main__':
    # Begin
    print "Starting"
    
    # Generate QR code with no border
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1,
        border=0,
        )
    
    # Our string to emojifi
    # Max 25 character to generate less than 21x21 to display on Whatapp 
    text = "Example Emoji QR Code"
    if len(text) > 25: 
        warnings.warn("Input text must be less than 26 characters to display properly on Whatsapp.")    
    qr.add_data(text)
    qr.make(True)
    
    # Create black white image
    img = qr.make_image(fill_color="black",back_color="white")
    
    # Convert to Numpy Array
    pix = np.array(img)
    
    # Convert to UTF8 emojis
    out = []
    for x in pix:
        t = []
        for y in x:
            t.append((emoji.emojize(":black_large_square:") if not y else emoji.emojize(":white_large_square:")))
        out.append(t)
    
    # Write emojis to file because my IDE cant display emojis
    with io.open('output.txt','w',encoding='utf-8-sig') as f:
        for x in out:
            for y in x: 
                f.write(y)
            f.write(u"\u000A")
    
    # Done with life, go make tea
    print "Complete"