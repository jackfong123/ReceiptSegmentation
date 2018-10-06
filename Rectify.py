import cv2
import numpy as np
import math

def get_lines(lines_in):
    if cv2.__version__ < '3.0':
        return lines_in[0]
    return [l[0] for l in lines_in]

def Rectify(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    #cv2.imshow('edge', cv2.resize(edges, (0,0), fx=0.5, fy=0.5))

    lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=200,
                            minLineLength=200, maxLineGap=10)

    valid = []
    rows = img.shape[0]
    cols = img.shape[1]
    for x1, y1, x2, y2 in get_lines(lines):
        if x2 == x1 or x1 > cols/2:
            continue
        slope = (y2-y1)*1.0/(x2-x1)
        if abs(slope) > 0.2:
            continue
        #cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        valid.append(slope)
    #print(len(valid))
    avg = sum(valid) / len(valid)
    avg = math.atan(avg) * 180 / np.pi
    #print('%.3f' % (avg))
    M = cv2.getRotationMatrix2D((cols/2, rows/2), avg, 1)
    dst = cv2.warpAffine(img, M, (cols, rows),
                         borderValue=(255, 255, 255))
    return dst

