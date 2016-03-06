"""
Makes a 512x512 wallpaper out of two images.

Author: Joe Noel (noelj)
"""
import check2_helper
from PIL import Image

def wallpaper(): #select 4 images and pastes them together into 512x512 image
    image1 = Image.open(image_files[int(raw_input('Select a Picture ID (0-14) ==> '))])
    im1s = check2_helper.sq_crop(image1)
    im1 = im1s.resize( (256,256) )
    image2 = Image.open(image_files[int(raw_input('Select a Picture ID (0-14) ==> '))])
    im2s = check2_helper.sq_crop(image2)
    im2 = im2s.resize( (256,256) )
    image3 = Image.open(image_files[int(raw_input('Select a Picture ID (0-14) ==> '))])
    im3s = check2_helper.sq_crop(image3)
    im3 = im3s.resize( (256,256) )
    image4 = Image.open(image_files[int(raw_input('Select a Picture ID (0-14) ==> '))])
    im4s = check2_helper.sq_crop(image4)
    im4 = im4s.resize( (256,256) )
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