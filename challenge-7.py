"""
Python Challenge Level 7.

The page title is 'smarty' and there is an image of a stream with what looks
like a greyscale barcode running across it ('oxygen.png'). Converting the
luminosity of each square into an ASCII value gives the answer.
"""
from PIL import Image

IMAGE_FILENAME = 'resources/oxygen.png'


def sample_barcode(image, x_targets, y):
    """
    Sample the barcode greyscale value in the image at a series of
    x-coordinates, with a constant y-coordinate.
    """
    pixels = image.convert('L').load()
    return [pixels[x, y] for x in x_targets]


def ascii_list_to_string(ascii_vals):
    """
    Convert a list of numbers to a string composed of their ASCII characters.
    """
    return ''.join([chr(c) for c in ascii_vals])


# The pixels of interest span pixels 44 - 52 vertically and 1 - 608 horizontally
# They are 7 pixels wide apart from the first which is 5 and the last which is 8
image = Image.open(IMAGE_FILENAME)
targets_x = range(1, 608, 7)
y = 47
values = sample_barcode(image, targets_x, y)

print(ascii_list_to_string(values))
# 'smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]'

print(ascii_list_to_string([105, 110, 116, 101, 103, 114, 105, 116, 121]))
# 'integrity'
# http://www.pythonchallenge.com/pc/def/integrity.html is the next URL.
