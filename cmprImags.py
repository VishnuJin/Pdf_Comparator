#compare two given images with open CV

import cv2

org = cv2.imread("imgOut\prototype1.jpg")
tst = cv2.imread("imgOut\sample1.jpg")

if org.shape == tst.shape:
    print("Images size matches")
    diff = cv2.subtract(org,tst)

    cv2.imshow('compared',diff)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
