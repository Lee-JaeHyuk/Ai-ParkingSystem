import socket
import imgCrop # 같은 directory 내에 있는 imgCrop.py를 import

UDP_IP = '222.107.177.42' # server IP num
UDP_PORT = 6667 # server port num

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP, UDP_PORT))
crop = imgCrop.CROP() # imgCrop.py의 CROP class

def s():
   while True:
      data_transferred = 0
      title, addr = serverSock.recvfrom(1024) # client에게 data 및 주소(IP, PORT)를 받음
      print ("Messsage: ", title) # 처음 오는 데이터는 file(image) name
      if not title:
         print("Error") # title이 없는 경우(전송을 받지 못한 경우) error
      else :
         data, addr = serverSock.recvfrom(1024) # 여기부터는 image에 대한 정보를 받음
         with open('./img/'+ title.decode(), 'wb') as f: # title로 file을 생성하여 open
            try:
               while data:
                  f.write(data) # file에 읽어온 data를 기록
                  data_transferred += len(data)
                  data, addr = serverSock.recvfrom(1024)
                  if data == b'end': # client에서 ‘end’를 전송하면 이미지 하나를 다 보냈다는 의미
                     print('end')
                     crop.main() # CROP class의 main 함수를 실행하여 image crop
                     s() # 함수를 처음부터 다시 실행하여 다음 image를 받아옴
               print("while end")
            except Exception as e:
               print(e)

s() # server에 대한 함수 실행
