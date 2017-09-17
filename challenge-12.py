"""
Python Challenge Level 12.

The page title is 'dealing evil' and the image is of someone dealing a pack
of cards into five piles. The image filename is 'evil1.jpg' - 'evil2.jpg' is an
image containing the words 'not jpg - _.gfx'. 'evil2.gfx' downloads a binary
file of no known file type.

Note that following the jpegs to 'evil4.jpg' does not contain an image but the
text, 'Bert is evil! go back!'.
"""
from enum import Enum

from PIL import Image

NUM_PILES = 5
FILENAME = 'resources/evil2.gfx'
OUT_FILENAME_TEMPLATE = '12-image-out-{num}{ext}'


class ImageFileTypes(Enum):
    """
    File identification information for a small number of image file formats.
    """
    JPEG = 0
    PNG = 1
    GIF = 2

    def extension(self):
        """
        Determine this file format's typical file extension.
        """
        return {
            self.JPEG: '.jpg',
            self.PNG: '.png',
            self.GIF: '.gif'
        }[self]

    def byte_signature(self):
        """
        The byte signature with which files of this format begin.
        """
        return {
            self.JPEG: b'\xFF\xD8\xFF\xE0',
            self.PNG: b'\x89PNG\x0D\x0A\x1A\x0A',
            self.GIF: b'GIF87a'
        }[self]


def deal(bytes_in, count):
    """
    Split a bytearray into a list of smaller bytearrays by 'dealing' the bytes
    into `count` different piles.
    """
    return [bytes_in[i::count] for i in range(count)]


def find_filetype(bytedata):
    """
    Find the filetype which matches the bytedata signature
    """
    for filetype in ImageFileTypes:
        if bytedata.startswith(filetype.byte_signature()):
            return filetype

with open(FILENAME, 'rb') as f:
    data = bytearray(f.read())

# 'Deal' the bytes into five even-sized piles (like the page title / image
# imply), then write them out to the appropriate image format.
for i, data_pile in enumerate(deal(data, NUM_PILES)):
    filetype = find_filetype(data_pile)
    output_filename = OUT_FILENAME_TEMPLATE.format(
        num=i, ext=filetype.extension())
    with open(output_filename, 'wb') as f:
        f.write(data_pile)
# Sequence of images spells 'disproportionality' with 'ity' crossed out.
# http://www.pythonchallenge.com/pc/return/disproportional.html is the next URL.
