#Converts Image to Simulated Lithophane, Returns base64 encoded string of image

from __future__ import division
from PIL import Image, ImageFilter

import time, sys, base64, re

import StringIO

from io import BytesIO

from decimal import Decimal


for line in sys.stdin:
    image_base64 = line



im = Image.open(BytesIO(base64.b64decode(image_base64)))


start_time = time.time()

#Uncommet to read filename from system arguments
#filename = sys.argv[-1]

#im = Image.open(filename)

width = im.size[0]
height = im.size[1]

if width > 400:
	new_width = 400
	new_height = int((400 / width) * height)
else:
	new_width = 400
	new_height = int((400 / width) * height)

	#Calculate pricing based on .1935 dollars/cm2

price = ((new_width / 2.6247) * (new_height / 2.6247) * 0.001937504)
price = Decimal(price)
price = round(price,2)
price = str(price)



#print width
#print height
#print new_width
#print new_height

im = im.resize((new_width,new_height))





layer_1 = Image.open("python/image_keys/layer_1.jpg").resize(im.size)
layer_2 = Image.open("python/image_keys/layer_2.jpg").resize(im.size)
layer_3 = Image.open("python/image_keys/layer_3.jpg").resize(im.size)
layer_4 = Image.open("python/image_keys/layer_4.jpg").resize(im.size)
layer_5 = Image.open("python/image_keys/layer_5.jpg").resize(im.size)
layer_6 = Image.open("python/image_keys/layer_6.jpg").resize(im.size)
layer_7 = Image.open("python/image_keys/layer_7.jpg").resize(im.size)
layer_8 = Image.open("python/image_keys/layer_8.jpg").resize(im.size)
layer_9 = Image.open("python/image_keys/layer_9.jpg").resize(im.size)
layer_10 = Image.open("python/image_keys/layer_10.jpg").resize(im.size)
layer_11 = Image.open("python/image_keys/layer_11.jpg").resize(im.size)
layer_12 = Image.open("python/image_keys/layer_12.jpg").resize(im.size)



im_list = list(im.getdata())

layer_1_list = list(layer_1.getdata())
layer_2_list = list(layer_2.getdata())
layer_3_list = list(layer_3.getdata())
layer_4_list = list(layer_4.getdata())
layer_5_list = list(layer_5.getdata())
layer_6_list = list(layer_6.getdata())
layer_7_list = list(layer_7.getdata())
layer_8_list = list(layer_8.getdata())
layer_9_list = list(layer_9.getdata())
layer_10_list = list(layer_10.getdata())
layer_11_list = list(layer_11.getdata())
layer_12_list = list(layer_12.getdata())

im_gray = []

levels = 12
stepsize = 256 // levels

light_dict = {0: layer_12_list, 1: layer_12_list, 2: layer_12_list, 3: layer_11_list, 4: layer_10_list, 5: layer_9_list, 6: layer_8_list, 7: layer_7_list , 8: layer_6_list  , 9: layer_5_list , 10: layer_4_list  , 11: layer_3_list  , 12: layer_2_list, 13: layer_1_list}

icount = -1;

for i in im_list:
	icount +=1
	j = ((i[0] * .21) + (i[1] * .72) + (i[2]* .07))
	r = (j // stepsize) 
	l = (j / stepsize) 
	if (l - r) > 0.5:
		q = r
		im_gray.append(light_dict[int(q)][icount])
	else:
		q = (r + 1)
		im_gray.append(light_dict[int(q)][icount])


im2 = Image.new(im.mode, im.size)
im2.putdata(im_gray)


counter = 0
while counter != 1:
	im2 = im2.filter(ImageFilter.GaussianBlur)
	counter +=1

#filesave = filename[0:-4] + "_lithophane" ".jpg"
#im2.save(filesave)


#convert image to base64


output = StringIO.StringIO() 
im2.save(output, format='JPEG')
im_data = output.getvalue()



#b64_output_image = base64.b64encode(im_data)

b64_output_image = base64.b64encode(im_data)
b64_output_image = str(b64_output_image)





print(b64_output_image)

sys.stdout.flush()

print(price)

sys.stdout.flush()


