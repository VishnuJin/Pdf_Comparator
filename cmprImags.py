#compare two given images with open CV

import cv2

org = cv2.imread("imgOut\prototype1.jpg")
#tst = cv2.imread("imgOut\sample1.jpg")
dup = cv2.imread("imgOut\prototype - duplicate1.jpg")

if org.shape == dup.shape:
    print("Images size matches")
    print(org.shape)
    print(dup.shape)
    diff = cv2.subtract(org,dup)
    r,g,b = cv2.split(diff)
    if (cv2.countNonZero(r)==0) & (cv2.countNonZero(g)==0) & (cv2.countNonZero(b)==0):
        print("The images are comletely equal")
    cv2.imshow('compared',diff)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
