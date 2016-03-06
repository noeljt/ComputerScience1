import panoramio as pan
from PIL import Image

def get_pics():
    address = raw_input('Enter an address ==> ')
    urls = pan.getPhotos(address, 4)
    return urls

def wallpaper(urls): #pastes four images together into 512x512 image
    if len(urls) >= 4:
        image1 = pan.openphoto(urls[0])
        im1 = image1.resize( (256,256) )
        image2 = pan.openphoto(urls[1])
        im2 = image2.resize( (256,256) )
        image3 = pan.openphoto(urls[2])
        im3 = image3.resize( (256,256) )
        image4 = pan.openphoto(urls[3])
        im4 = image4.resize( (256,256) )
        im = Image.new('RGB', (512,512), 'white')
        im.paste(im1, (0,0))
        im.paste(im2, (257,0))
        im.paste(im3, (0,257))
        im.paste(im4, (257,257))
        im.save('wallpaper.jpg')
        im.show()
    else:
        print "Not enough images at location"

wallpaper(get_pics())