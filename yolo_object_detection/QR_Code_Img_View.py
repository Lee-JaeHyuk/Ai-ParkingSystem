import cv2 as cv
import os
import qrcode

#parkingimg = cv.imread("./parkingLotImg/MoonParkingLot.png", cv.IMREAD_COLOR)
#cv.imshow("show", parkingimg)

a = input()

red = (0, 0, 255)

path_img = './QRimg'  # Set image directory path
img_file_list = os.listdir(path_img)  # Read file list in path
img_file_list.sort()
image = ("./QRimg/"+a+".png") # _1.JPG 순서대로 잘라서 파일을 저장
img = cv.imread(image, cv.IMREAD_COLOR) #
cv.imshow("show", img)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imshow("show", img)
cv.waitKey(0)
cv.destroyAllWindows()








