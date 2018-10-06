# ReceiptSegmentation
The full procedure of receipt segmentation 
1. Rectify the whole image to make the following line detect procedure easier. Here I use HOG to detect lines and its angle, then rotate the image to be horizontal.
2. Eliminate the Horizontal lines use erosion(kernel size is (1,img.shape[1]/b), b is some constance) and use dilation to make the result more obvious. Why I need to do it? Because some receipts have horizontal lines between items while some do not. So I eliminate the lines uniformly.
3. Detect the lines use horizontal projection. Tips: Use global binarizaton will remain fewer noize.
