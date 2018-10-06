from os import walk
import cv2
from Rectify import *
from LineEliminator import *
from LineDetect import *

def main():
    directory = './origin/'
    f = []
    for (dirpath, dirname, filename) in walk(directory):
        f.extend(filename)
        break
    for filename in f:
        # if filename != 'TBAL1808290000500105032.jpg':
        #     continue
        img = cv2.imread(directory + filename)
        dst = Rectify(img)
        img_noLine = lineEliminate(dst)
        #cv2.imshow('no_line', img_noLine)
        img_withLine = lineDetect(img_noLine)
        # cv2.imshow('has_line', cv2.resize(img_withLine,(0,0), fx=0.5, fy=0.4))
        # cv2.waitKey(0)
        cv2.imwrite('./results/' + filename, img_withLine)

if __name__ == '__main__':
    main()