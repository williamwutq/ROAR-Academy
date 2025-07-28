from matplotlib import image
from matplotlib import pyplot
import os
import requests
from io import BytesIO

# Read an image file
path = os.path.abspath(__file__) if '__file__' in globals() else '.'
# Go up three directories
path = os.path.dirname(os.path.dirname(os.path.dirname(path)))
filename = path + '/' + 'Part Two/notebooks/lenna.bmp'
lenna = image.imread(filename)
img_data = lenna.copy()

# Get the USA flag image file from https://www.countryflags.com/
filename = path + '/' + 'usa.jpg'
usa = image.imread(filename)

# Shink the USA flag by half
usa = usa[::2, ::2]

# Put the USA flag in the top left corner of the Lenna image
for width in range(img_data.shape[1]):
    for height in range(img_data.shape[0]):
        if width < usa.shape[1] and height < usa.shape[0]:
            img_data[height, width] = usa[height, width]

# Save the modified image
output_filename = path + '/' + 'lenna_with_usa.bmp'
image.imsave(output_filename, img_data)

# use pyplot to plot the image
pyplot.imshow(img_data)
pyplot.show()