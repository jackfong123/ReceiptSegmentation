import cv2
import numpy as np

def lineEliminate(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    #cv2.imshow('gray', gray)
    th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                               cv2.THRESH_BINARY, 29, 2)
    #cv2.imshow('th', cv2.resize(th,(0,0), fx=0.5, fy=0.4))
    ero_kernel1 = np.ones((1, 6), np.uint8)
    erosion = cv2.erode(th, ero_kernel1, iterations=1)
    #cv2.imshow('ero1', cv2.resize(erosion,(0,0), fx=0.5, fy=0.4))
    ero_kernel2 = np.ones((1, int(th.shape[1]/10)), np.uint8)
    erosion = cv2.erode(~erosion, ero_kernel2, iterations=1)
    dil_kernel = np.ones((1, 6), np.uint8)
    dilation = cv2.dilate(erosion, dil_kernel, iterations=1)
    #cv2.imshow('dilaimg', cv2.resize(dilation,(0,0), fx=0.5, fy=0.4))

    rows, cols = dilation.shape
    st_idx = 0
    ed_idx = 0
    flag = False
    lines = []
    for row in range(rows):
        whitePts = np.sum(dilation[row]) / 255
        if row - ed_idx < 8:
            continue
        if whitePts > cols/10 and flag is False:
            st_idx = row
            flag = True
        elif whitePts < cols/10 and flag is True:
            ed_idx = row
            lines.append((st_idx + ed_idx) // 2)
            flag = False
    for l in lines:
        img[l-5:l+5] = np.ones((1, cols, 3)) * 255
        #cv2.line(img, (0, l), (cols, l), (0, 255, 0), 2)
    # cv2.imshow('img', cv2.resize(img, (0, 0), fx=0.5, fy=0.4))
    # cv2.waitKey(0)
    return img
