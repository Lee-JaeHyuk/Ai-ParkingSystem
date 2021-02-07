import socket
import os
import time

UDP_IP = '222.107.177.42' # server IP num
UDP_PORT = 6667 # server port num

path = './img' # SenTerm에서 촬영한 사진이 저장된 directory 경로
img_list = os.listdir(path) # path에 저장된 file list를 저장 (list형으로)
img_list.sort() # 받아온 이미지를 정렬

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for file_name in img_list: # 이미지 리스트가 저장된 img_list의 이름을 file_name이라는 변수로 받음
    clientSock.sendto(file_name.encode(), (UDP_IP, UDP_PORT))
    # server로 file(image) name 전송, client의 IP, PORT를 실어서 전송함.
    data_transferred = 0
    with open('./img/' + file_name, 'rb') as f: # file(image) open
        print(file_name) # file name 확인용
        try:
            data = f.read(1024) # file(image)에 적힌 내용 read하여 data 변수로 저장
            while data: # read한 data가 없을 때까지 data read 반복
                data_transferred += clientSock.sendto(data, (UDP_IP, UDP_PORT))
                data = f.read(1024)
                time.sleep(0.0001) # data가 중간에 손실되는 것을 막기 위해 약간의 delay를 넣음
        except Exception as e:
            print(e)
    clientSock.sendto('end'.encode(), (UDP_IP, UDP_PORT))
    # client는 server로 image를 다 보내면 ‘end’를 전송하여 image 하나를 다 보냄을 알려줌
    print('end') # image 하나 전송 완료 확인용
