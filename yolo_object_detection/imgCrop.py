import cv2 as cv
import os

class CROP:
    def main(self):
        # Color
        red = (0, 0, 255)

        # Read image file list in directory
        path_img = './img'  # Set image directory path
        img_file_list = os.listdir(path_img)  # Read file list in path
        img_file_list.sort()

        # Read vector file list in directory
        '''
        path_vector = './vector'
        vector_file_list = os.listdir(path_vector)
        vector_file_list.sort()
        '''
        # Store light status (0:Green, 1:Red)
        light_list = [0] * 3

        # ------test code-----------------------------------------

        # Open vector_file_list
        cnt = 0

        vector_list = []
        f = open("vector/vec.txt", "r")  # read mode
        while 1:
            line = f.readline()
            if not line:
                break
            else:
                vector_list = line.split()
                vector_list = [int(i) for i in vector_list]

        def extractor(img, cnt):
            cropped_img = img[vector_list[cnt + 1]:vector_list[cnt + 3], vector_list[cnt]:vector_list[cnt + 2]]
            return cropped_img

        for j in range(0, len(img_file_list)):
            count = 0
            while 1:
                count+=1
                if cnt > len(vector_list)-1:
                    break
                if vector_list[cnt] == -1:
                    cnt += 1
                    break
                image = "./img/{}".format(img_file_list[j])  # _1.JPG
                img = cv.imread(image, cv.IMREAD_COLOR)
                # print(vector_list[cnt], vector_list[cnt+1],vector_list[cnt+2], vector_list[cnt+3])
                cv.rectangle(img, (vector_list[cnt], vector_list[cnt + 1]),
                             (vector_list[cnt + 2], vector_list[cnt + 3]), red, 3)
                img = extractor(img, cnt)
                file_name = img_file_list[j].split('.')
                print(file_name)
                file_name_path = './crop_img/' + str(file_name[0]) + '_' + str(count) + '.' + str(file_name[-1])
                cv.imwrite(file_name_path, img)
                cnt = cnt + 4


if __name__ == '__main__':
    crop = CROP()
    crop.main()