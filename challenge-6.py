"""
Python Challenge Level 6.

The page title is 'now there are pairs' and the image is of a zip on a pair
of jeans. Follow clues in 'jeans.html', 'pants.html', 'trousers.html' and
'zipper.html' to 'zip.html' which says 'yes. find the zip'.

'channel.zip' is a zipped folder with the readme: 'welcome to my zipped list.
hint1: start from 90052 hint2: answer is inside the zip'. The files are another
nothing chain.
"""
import re
import zipfile

ZIP_FILENAME = 'resources/channel.zip'
STARTING_NOTHING = 90052


def get_zipfile_comments(zip_file):
    """
    Get a dictionary of comments for each file in the zip as a dictionary
    in the form {}.
    """
    return {i.filename: i.comment.decode('utf-8') for i in zip_file.infolist()}


def find_next_nothing(file_contents):
    """
    Find the next 'nothing' in a string containing the text 'Next nothing is
    <number>'. If this format doesn't exist in the given file contents,
    return None.
    """
    m = re.search('Next nothing is ([0-9]+)', file_contents)
    if m:
        return int(m.group(1))


def get_filename(nothing):
    """
    Determine the filename for a given 'nothing' value.
    """
    return '{nothing}.txt'.format(nothing=nothing)


def follow(zipfile, starting_nothing):
    """
    Follow a series of files pointing to each other from a starting 'nothing'
    value through a chain of 'next nothing is...', where nothing is the next
    filename. Returns a tuple of (list of all filenames, contents of last file).
    """
    filename = get_filename(starting_nothing)
    all_filenames = [filename]
    while True:
        contents = zip_file.read(filename).decode('utf-8')
        next_nothing = find_next_nothing(contents)
        if next_nothing is None:
            # Complete - return
            return all_filenames, contents
        else:
            # Go around for another loop
            filename = get_filename(next_nothing)
            all_filenames.append(filename)


zip_file = zipfile.ZipFile(ZIP_FILENAME)
filenames, last_file_contents = follow(zip_file, STARTING_NOTHING)
print(last_file_contents)
# 'Collect the comments'

comments = get_zipfile_comments(zip_file)
print(''.join([comments[f] for f in filenames]))
# ****************************************************************
# ****************************************************************
# **                                                            **
# **   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
# **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
# **   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
# **   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
# **   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
# **   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
# **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
# **   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
# **                                                            **
# ****************************************************************
#  **************************************************************
# http://www.pythonchallenge.com/pc/def/oxygen.html is the next URL.
