import socket
import yolo_object_detection

UDP_IP = '222.107.177.42' # server IP num
UDP_PORT = 6668 # server port num
                  # UI용 server는 SenTerm 사진용과 port를 다르게 줘서 동시에 실행 가능하도록 만듦

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP, UDP_PORT))
detection = yolo_object_detection.DETECT() # yolo_object_detection의 DETECT class 호출

while True:
    data, addr = serverSock.recvfrom(1024) # data, address(IP, PORT)를 전송 받음
    if data == b'start': # 전송 받은 data가 start인지 확인 (bit단위 전송이므로 b’start’ 라고 씀)
        parkingList = detection.main()#start를 받은 경우 DETECT class의 main 함수 수행(yolo 수행)
        message = ''
        for i in parkingList: # main 함수를 통해 받은 car 유무에 대한 list를
            message += str(i) # 전송을 위해 string으로 형 변환
        serverSock.sendto(message.encode(), addr) # Client 주소로 인코딩하여 전송
