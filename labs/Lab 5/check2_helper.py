from PIL import Image

def sq_crop(image):
    im = image
    size = im.size
    w = size[0]
    h = size[1]
    if w > h:
        return im.crop((0,0, h,h))
    elif h > w:
        return im.crop((0,0, w,w))
    elif w == h:
        return im