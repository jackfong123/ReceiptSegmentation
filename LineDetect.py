import cv2
import numpy as np

def lineDetect(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    #cv2.imshow('gray', gray)
    _, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # cv2.imshow('th', cv2.resize(th,(0,0), fx=0.5, fy=0.4))

    # dil_kernel = np.ones((5, 5), np.uint8)
    # th = cv2.dilate(th, dil_kernel, iterations=1)
    # cv2.imshow('after_dilate', cv2.resize(th,(0,0), fx=0.5, fy=0.4))

    rows, cols = th.shape
    row = 0
    pre = 0
    while row < rows:
        total_black = cols - np.sum(th[row]) / 255
        if total_black < 80 and row - pre > 20:
            cv2.line(img, (0, row), (cols, row), (0, 255, 0), 2)
            pre = row
            while row < rows and cols-np.sum(th[row])/255 < 80:
                row += 2
        row += 1
    # cv2.imshow('img', cv2.resize(img,(0,0), fx=0.5, fy=0.4))
    # cv2.waitKey(0)
    return img