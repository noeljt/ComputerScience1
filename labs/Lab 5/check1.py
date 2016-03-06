"""
Makes a 512x512 wallpaper out of four images.

Author: Joe Noel (noelj)
"""

from PIL import Image

def wallpaper(): #select 4 images and pastes them together into 512x512 image
    image1 = Image.open(image_files[int(raw_input('Select a Picture ID (0-14) ==> '))])
    im1 = image1.resize( (256,256) )
    image2 = Image.open(image_files[int(raw_input('Select a Picture ID (0-14) ==> '))])
    im2 = image2.resize( (256,256) )
    image3 = Image.open(image_files[int(raw_input('Select a Picture ID (0-14) ==> '))])
    im3 = image3.resize( (256,256) )
    image4 = Image.open(image_files[int(raw_input('Select a Picture ID (0-14) ==> '))])
    im4 = image4.resize( (256,256) )
    im = Image.new('RGB', (512,512), 'white')
    im.paste(im1, (0,0))
    im.paste(im2, (257,0))
    im.paste(im3, (0,257))
    im.paste(im4, (257,257))
    im.save('wallpaper.jpg')
    im.show()

#Main Code

image_files = [ 'ca.jpg','im.jpg', 'hk.jpg','bw.jpg', 'hw.jpg', \
                'fl.jpg', 'tr.jpg', 'tr2.jpg', 'cf.jpg', '1.jpg',\
                '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg']

wallpaper()