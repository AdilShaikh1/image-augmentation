import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import cv2
import os
import numpy as np
import math
import random

ang_range = 45
shear_range = 4
trans_range = 10
brightness = 0
i = 0

for i in range(20):
    j = random.randint(1,9)
    val = str(j)
    img = cv2.imread("/Users/atos/Desktop/dirt/dirt"+val+".png")
    rows,cols,c = img.shape

    #rotate
    M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
    imgrot = cv2.warpAffine(img,M,(cols,rows))
    cv2.waitKey(500)
    path = "/Users/atos/Desktop/dataset"
    cv2.imwrite(os.path.join(path ,"dirt rotate"+val+".png"),imgrot)
    cv2.waitKey(500)

    #flip
    imgflip = cv2.flip(img,1)
    path = "/Users/atos/Desktop/dataset"
    cv2.imwrite(os.path.join(path ,"dirt flip"+val+".png"),imgflip)
    cv2.waitKey(500)

    # Translation
    tr_x = trans_range*np.random.uniform()-trans_range/2
    tr_y = trans_range*np.random.uniform()-trans_range/2
    Trans_M = np.float32([[1,0,tr_x],[0,1,tr_y]])
    imgtrans = cv2.warpAffine(img,Trans_M,(cols,rows))
    path = "/Users/atos/Desktop/dataset"
    cv2.imwrite(os.path.join(path ,"dirt translate"+val+".png"),imgtrans)
    cv2.waitKey(500)

    # Shear
    pts1 = np.float32([[5,5],[20,5],[5,20]])
    pt1 = 5+shear_range*np.random.uniform()-shear_range/2
    pt2 = 20+shear_range*np.random.uniform()-shear_range/2
    pts2 = np.float32([[pt1,5],[pt2,pt1],[5,pt2]])
    shear_M = cv2.getAffineTransform(pts1,pts2)
    imgshear = cv2.warpAffine(img,shear_M,(cols,rows))
    path = "/Users/atos/Desktop/dataset"
    cv2.imwrite(os.path.join(path ,"dirt shear"+val+".png"),imgshear)
    cv2.waitKey(500)

    #sharpening
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    imgsharp = cv2.filter2D(img, -1, kernel)
    path = "/Users/atos/Desktop/dataset"
    cv2.imwrite(os.path.join(path ,"dirt sharpened"+val+".png"),imgsharp)
    #cv2.imshow("imagerotate",imgsharp)
    cv2.waitKey(500)

    #blurr
    imgblur = cv2.bilateralFilter(img,9,75,75)
    path = "/Users/atos/Desktop/dataset"
    cv2.imwrite(os.path.join(path ,"dirt blurr"+val+".png"),imgblur)
    cv2.waitKey(500)
    
    #brightness
    matrix = np.ones(img.shape, dtype = "uint8") * 75
    added = cv2.add(img, matrix)
    #cv2.imshow("Added", added)
    subtracted = cv2.subtract(img, matrix)
    #cv2.imshow("Subtracted", subtracted)
    cv2.waitKey(500)
    path = "/Users/atos/Desktop/dataset"
    cv2.imwrite(os.path.join(path ,"dirt add"+val+".png"),added)
    cv2.waitKey(500)
    path = "/Users/atos/Desktop/dataset"
    cv2.imwrite(os.path.join(path ,"dirt subtract"+val+".png"),subtracted)
    cv2.waitKey(500)
    
