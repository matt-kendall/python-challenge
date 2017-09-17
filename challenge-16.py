"""
Python Challenge Level 16.

The page title is 'let me get this straight'. There is an image (mozart.gif)
which looks like noise but every row has 5 consecutive pink
"""
from PIL import Image
import numpy as np

IMAGE_FILENAME = 'resources/mozart.gif'
MARKER = np.array(5 * [195])  # GIF Palette mode - this is the palette index


def find_marker(array, marker):
    """
    Find the index of a specified marker sequence in a 1D array.
    """
    for x in range(0, len(array) - len(marker)):
        sub_array = array[x: x + len(marker)]
        if np.array_equal(sub_array, marker):
            return x


image = Image.open(IMAGE_FILENAME)
data = np.array(image)

for y in range(0, image.height):
    # Search row for marker and shift the row so the marker is at the start.
    marker_index = find_marker(data[y,:], MARKER)
    data[y,:] = np.roll(data[y,:], -marker_index + 1)

Image.fromarray(data, image.mode).show()
# The image shows the word 'romance'.
# http://www.pythonchallenge.com/pc/return/romance.html is the next URL.
