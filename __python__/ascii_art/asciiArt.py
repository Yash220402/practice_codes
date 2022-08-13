import sys, random, argparse
import numpy as np
import math
from PIL import Image

# DEFINING GRAYSCALE LEVELS
# 70 levels of gray 
gscale1 = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^`'. """
# 10 levels of gray
gscale2 = '@%#*+=-:. '


def getAverage(image):
    """Given PIL image, return average value of grayscale value"""
    im = np.array(image)
    w, h = im.shape
    
    return np.average(im.reshape(w*h))


def convertImageToAscii(fileName, cols, scale, morelevels):
    """
    Given image and dimension (rows,cols), returns an m*n list of images
    """
    global gscale1, gscale2
    
    image = Image.open(fileName).convert("L")  # L - luminance (measure of brightness of an img)
    
    # store the image dimensions
    W, H = image.size[0], image.size[1]
    print("Input img dims: %d x %d" % (W, H))
    
    # compute tile width
    w = W/cols
    # compute tile height
    h = w/scale
    # compute the no. of rows to use in final grid
    rows = int(H/h)
    
    print("cols: %d, rows: %d" % (cols, rows))
    print("tile dims: %d x %d" % (w,h))
    
    # check if the image size is too small
    if cols > W or rows > H:
        print("Image is too small for specified cols!")
        exit(0)
        
    # an ASCII image is a list of character strings
    aimg = []
    # generate the list of tile dimensions
    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j+1)*h)
        
        # correct the last tile
        if j == rows-1:
            y2 = H
        
        # append an empty string
        aimg.append("")
        for i in range(cols):
            # crop the image to fit the tile
            x1 = int(i*w)
            x2 = int((i+1)*w)
            # correct the last tile
            if i == cols-1:
                x2 = W
            # crop the image to extract the tile into another image object
            img = image.crop((x1,y1,x2,y2))
            
            # get the average luminance
            avg = int(getAverage(img))
            # lookup the ASCII char fot grayscale value (avg)
            if morelevels:
                gsval = gscale1[int((avg*69)/255)]
            else:
                gsval = gscale2[int((avg*9)/255)]
            
            # append the ASCII character to the string
            aimg[j] += gsval
        
    return aimg

def main():
    # create parser
    descStr = "This program converts an image into ASCII art"
    parser = argparse.ArgumentParser(description=descStr)
    
    # add expected arguments
    parser.add_argument('--file', dest='imgFile', required=True)
    parser.add_argument('--scale', dest='scale', required=False)
    parser.add_argument('--out', dest='outFile', required=False)
    parser.add_argument('--cols', dest='cols', required=False)
    parser.add_argument('--morelevels', dest='morelevels', action='store_true')
    
    # parse arguments
    args = parser.parse_args()
    
    imgFile = args.imgFile
    # set output file
    outFile = 'out.txt'
    if args.outFile:
        outFile = args.outFile
    
    # set scale default 0.43, which suits a Courier font
    scale = 0.50
    if args.scale:
        scale = float(args.scale)
    
    # set cols
    cols = 80
    if args.cols:
        cols = int(args.cols)
    
    print("generating ASCII art...")
    # convert image to ASCII text
    aimg = convertImageToAscii(imgFile, cols, scale, args.morelevels)
    
    # open a new text file
    f = open(outFile, 'w')
    # write each string in the list to the new file
    for row in aimg:
        f.write(row + '\n')

    f.close()
    print("ASCII art written to %s" % outFile)

# def main():
#     image = 'guts.jpg'
#     # test
#     print("generating ASCII art...")
#     # convert image to ASCII text
#     aimg = convertImageToAscii(fileName=image, cols=150, scale=0.5, morelevels=True)
#     outFile = "guts.txt"
#     # open a new text file
#     f = open(outFile, 'w')
#     # write each string in the list to the new file
#     for row in aimg:
#         f.write(row + '\n')
#     # clean up
#     f.close()
#     print("ASCII art written to %s" % outFile)
    
if __name__ == "__main__":
    main()