import os
from PIL import Image, ExifTags
mainFolder=os.path.dirname(__file__)
pathfile= os.path.join(mainFolder, 'ABOUT/307.jpg')
pathfile= os.path.normpath(pathfile)
img = Image.open(pathfile)
tags = ExifTags.TAGS
x = 'кодирует в строку байтов'
b=x.encode('utf-8')
exif= img.getexif()
#val_utf=[]
for key, val in exif.items():

        if tags.get(key, key)== 'XPComment':
                output = str(val, 'UTF-16')[:-1]
                print(output)

        #val_utf.append(val)

        #print(tags.get(key, key), ':', val_utf)

#exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
#a=val_utf[1]
#output = str(a, 'UTF-16')

#print(a, type(a), output)
