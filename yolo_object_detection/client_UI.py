import pandas as pd
import datetime
import time
import pygame
from pygame import *
from pygame.locals import *
import numpy
import socket


UDP_IP = '222.107.177.42' # server IP num
UDP_PORT = 6668 # server port num
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 주차 도면 위의 circle 생성 좌표
parkingList = [(1180,303), (1180,269), (1180,244), (1180,218), (1180,183), (1180,156), (1180,129), (944,46), (919,46), (894,46), (870, 46), (836,46), (810,46), (747,46), (720,46), (695,46), (660,46), (633,46), (573,46), (548,46), 517,46), (486,46), (458,46), (396,46), (370,46), (344,46), (288,46), (257,46), (222,46), (203,46), (175,46),(149,46), (76,46), (34,126), (34,148), (34,172), (34,198), (34,222), (34,248),(34,273), (34,297), (34,323), (34,347), (34,372), (34,397), (93,440), (114,440), (149,440), (176,440),(199,440), 223,440), (258,440), (280,440), (309,440), (345,440), (370,440), (397,440), (434,440), (457,440),(520,440), (545,440), (575,440), (605,440), (633,440), (661,440), (694,440), (719,440), (747,440), (780,440),(807,440), (835,440), (875,440), (901,440), (928,440), (953,440), (1000,440), (1026,440), (1051,440), (1085,440),(1107,440), (1127,440), (1061,166), (1036,166), (1011,166), (985,166), (962,166), (937,166), (914,166), (887,166),(835,166), (809,166), (785,166), (761,166), (736,166), (710,166), (686,166), (700, 240), (700, 270),(689,323),(712,323), (741,323), (766,323), (797,323), (822,323), (849,323), (878,323), (898,323), (956,323), (984,323),(1009,323), (1062,323), (582,166), (558,166), (533,166), (505,166), (483,166), (434,166), (412,166), (390,166),(364,166), (339,166), (315,166), (290,166), (265,166), (238,166), (214,166), (188,166), (164,166), (139,166),(145,223), 145,241), (145,264), (138,323), (164,323), (186,323), (210,323), (242,323), (264,323), (314,323),(338,323), (358,323), (382,323), (408,323), (429,323), (458,323), (479,323), (507,323), (529,323), (555,323),(580,323), 565,240), (565,270)]

screen = pygame.display.set_mode((1332,477), pygame.DOUBLEBUF) # screen에 대한 설정

class PROCESSING:
    def main(self):
        pygame.init()
        img = pygame.image.load("./parkingLotImg/MoonParkingLot.png") # 배경 이미지 생성
        img = pygame.transform.scale(img, (1332, 477)) # 배경 이미지 크기 변경 (screen에 맞게)
        screen.blit(img, (0, 0)) # screen에 배경 이미지 삽입
        for i in range(len(parkingList)): # parking list 길이만큼 circle 삽입
            pygame.draw.circle(screen, (0, 255, 0), parkingList[i], 5)
        pygame.display.flip() # 지금까지 변한 모든 설정을 screen 위에 반영
        carTable = [] # 주차면, 입차 시간, 출차 시간에 대한 리스트
        carArray = numpy.array(carTable) # 특정 열을 받아 오기 위해 numpy.array 사용

        running = True # while문의 수행 상태 변화를 위해 running 변수 사용

        while running:
            for event in pygame.event.get(): # 종료에 관한 입력 event를 받아 옴
                if event.type == pygame.QUIT: running = False # 마우스로 창 닫기를 클릭하면 종료
                if event.type == pygame.KEYDOWN: # 키보드를 누르는 경우
                    if (event.key == pygame.K_ESCAPE): running = False # 누른 키보드가 esc면 종료
                pygame.display.flip() # 지금까지 변한 모든 설정을 screen 위에 반영
                clientSock.sendto("start".encode(), (UDP_IP, UDP_PORT)) # car 유무에 대한 list를 받기 위해 server로 ‘start’를 인코딩하여 전송
                data, addr = clientSock.recvfrom(1024) # server가 전송한 data를 받음
                yolo_detection = data.decode() # yolo 수행 결과로 보낸 data 디코딩
                yolo_detection = [int(i) for i in yolo_detection] # list구조 및 int형으로 변경
                check = [0] * len(yolo_detection) # in, not in check
                print("주차 가능:", len(parkingList) - sum(yolo_detection), "/", len(parkingList)) # 현재 주차 가능한 수에 대해 출력 (sum(yolo_detection)은 리스트의 숫자 합을 의미)

                for i in range(len(yolo_detection)):
                    carArray = numpy.array(carTable)
                    if yolo_detection[i]: # yolo_detection[i] == 1 인 경우 (car인 경우)
                        if len(carTable) == 0:
                            check[i] = 1 # check가 1이면 내용 기록이 필요함을 의미
                        else:
                            for j in range(len(carTable)):
                                carArray = numpy.array(carTable)
                                if str(i) not in carArray[:, 0]: # 기록된 주차면이 아닌 경우
                                    check[i] = 1 # 새로 들어온 차이므로 기록 필요
                                elif carArray[:, 0][j] == str(i) and carArray[:, 2][j] == str(0):
                                    # 해당 주차면의 출차 기록이 없는 경우
                                    check[i] = 0 # 기존에 있던 차이므로 기록 필요 X
                                elif carArray[:, 0][j] == str(i) and carArray[:, 2][j] != str(0):
                                    # 해당 주차면의 출차 기록이 있는 경우
                                    check[i] = 1 # 새로 들어온 차이므로 기록 필요
                    else: # yolo_detection[i] == 0인 경우 (car가 아닌 경우)
                        for j in range(len(carTable)):
                            if carTable[j][0] == i and carTable[j][2] == 0: # 입차 기록이 있는 경우
                                now = datetime.datetime.now()
                                carTable[j][2] = now.strftime('%Y-%m-%d %H:%M:%S') # 출차 시간 기록
                        pygame.draw.circle(screen, (0, 255, 0), parkingList[i], 5) # Create green
                        # cv2.circle(img, parkingList[i], 5, (0, 255, 0), -1)  # Create green circle
                for i in range(len(check)): # check list 확인을 위한 반복문
                    if check[i]: # check[i] == 1이면
                        now = datetime.datetime.now()
                        carTable.append([i, now.strftime('%Y-%m-%d %H:%M:%S'), 0])
                        #주차면, 입차 시간 기록
                        pygame.draw.circle(screen, (255, 0, 0), parkingList[i], 5) # Create rea
                df = pd.DataFrame(carTable, columns=['주차면', '입차', '출차']) #DataFrame Update
                print(df) # 테이블 형식으로 내용 출력
        pygame.quit() # running == False인 경우 while문을 종료하면서 프로그램 종료

if __name__ == '__main__':
    processing = PROCESSING()
    processing.main()
