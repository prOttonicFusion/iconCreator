#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Script for creating a set of ICO-files from a single NxN pixel image
# Usage: python iconCreator.py image-file.png
#
# @Date    : 2020-04-05 23:31:12
# @Author  : Otto Lindblom
# @Link    : link

import os
import sys
from PIL import Image
from pathlib import Path

# Output directories
directories = ["base", "linux", "mac"]

# Input file from CLI argument
if (len(sys.argv) != 2):
    print("Expected 1 command line argument, got {}".format(len(sys.argv)-1))
    exit()

infile = sys.argv[1]


def addMargin(image, topMargin, leftMargin, bottomMargin, rightMargin):
    newWidth = image.size[0] + rightMargin + leftMargin
    newHeight = image.size[1] + topMargin + bottomMargin
    newImage = Image.new(image.mode, (newWidth, newHeight), (255, 255, 255, 0))
    newImage.paste(image, (leftMargin, topMargin))
    return newImage


for dir in directories:
    # Create output directory structure if not exists
    pathToDir = Path("icons") / Path(dir)
    if not os.path.exists(pathToDir):
        os.makedirs(pathToDir)

    if dir == 'base':
        # General icons
        imgSizes = [16, 24, 32, 48, 64]
    else:
        # Mac & Linux icons
        imgSizes = [128, 256, 512, 1024]

    for size in imgSizes:
        outfile = pathToDir / Path(str(size) + ".png")
        try:
            with Image.open(infile) as im:
                # Scale & convert image

                if 'mac' in dir:
                    # Add ~5% margin to Mac icons
                    m = int(im.size[0]*0.05)
                    im = addMargin(im, m, m, m, m)

                im.thumbnail((size, size))
                im.save(outfile)
        except IOError:
            print("unable to process ", infile)
            exit()
        print("Created: ", outfile)

# Finally create Windows ICO file
outfile = "icons/Icon.ico"
try:
    # Scale & convert image
    with Image.open(infile) as im:
        im.save(outfile)
except IOError:
    print("unable to process ", infile)
    exit()
print("Created: ", outfile)
print("Done!")
