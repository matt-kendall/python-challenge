"""
Python Challenge Level 14.

The page title is 'walk around' and the image is some kind of spiral pastry.
There is a 10,000 x 1pixel image resembling a barcode ('wire.png') underneath.
The clue in the page source 'remember: 100*100 = (100+99+99+98) + (...' tells
us to 'wrap' the barcode-like image into a 100*100 image.
"""
from PIL import Image
import numpy as np

IMAGE_FILENAME = 'resources/wire.png'
WRAPPED_IMAGE_SIZE = (100, 100)

def get_spiral_coords(w, h):
    """
    Determine the sequence of coordinates found by spiraling in on an image of
    given size clockwise from the top-left corner to the centre.
    """
    x, y = 0, 0
    depth = 0
    coords = []
    while len(coords) < w * h:
        # Check for the special case where we are 1 pixel wide:
        one_pixel_wide = w - 2 * depth == 1
        one_pixel_tall = h - 2 * depth == 1

        # Top
        for _x in range(depth, w - depth):
            x = _x
            coords.append((x, y))
        # If one pixel tall, we are finished:
        if one_pixel_tall:
            break

        # Right
        for _y in range(depth + 1, h - depth):
            y = _y
            coords.append((x, y))
        # If one pixel wide, we are finished
        if one_pixel_wide:
            break

        # Bottom
        for _x in reversed(range(depth, w - depth - 1)):
            x = _x
            coords.append((x, y))

        # Left
        for _y in reversed(range(depth + 1, h - depth - 1)):
            y = _y
            coords.append((x, y))
        depth += 1
    return coords


image = Image.open(IMAGE_FILENAME)
wrapped_image = Image.new('RGB', WRAPPED_IMAGE_SIZE)

for idx, coord in enumerate(get_spiral_coords(*WRAPPED_IMAGE_SIZE)):
    wrapped_image.putpixel(coord, image.getpixel((idx, 0)))

wrapped_image.show()
# The image is of a cat.
# http://www.pythonchallenge.com/pc/return/cat.html leads to
# http://www.pythonchallenge.com/pc/return/uzi.html which is the next URL.
