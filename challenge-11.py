"""
Python Challenge Level 11.

The page title is 'odd even' and the image ('cave.jpg') appears to have half of
the pixels filled in a shade of dark grey in a checkboard pattern. Extract only
the dark pixels to reveal the image.
"""
from PIL import Image

IMAGE_FILENAME = 'resources/cave.jpg'


def is_dark(x, y):
    """
    Determine if a given pixel coordinate is a 'dark' pixel or not.
    """
    # Odds are (0,0), (0,2), (1,1), (1,3)
    # Evens are (0,1), (0,3), (1,0), (1,2)
    return (x + y) % 2 == 0


def make_output_image(data, w, h):
    """
    Create an output image given the dark pixel values and the width, height
    of the original image.
    """
    # Half width as we resampled every other pixel
    out = Image.new('RGB', (w // 2, h))
    out.putdata(dark_px)
    # Resize to maintain aspect ratio with 50% fewer pixels
    return out.resize((w, h))

image = Image.open(IMAGE_FILENAME)
dark_px = []
# Work from left to right across the image:
for y in range(image.height):
    for x in range(image.width):
        if is_dark(x, y):
            dark_px.append(image.getpixel((x,y)))
out = make_output_image(dark_px, *image.size)
out.show()
# Image shows the word 'evil'
# http://www.pythonchallenge.com/pc/return/evil.html is the next URL.
