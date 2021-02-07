# Ai-ParkingSystem
## JetsonNano 와 RasberryPi 2.0 를 이용한 주차 공간 및 QR코드 를 통한 주차 위치 확인 시스템<br/><br/>

### **1. 프로젝트 목표**

aParkings-AI System은 RasberryPi 2.0 이 촬영한 영상을 Jetson Nano 로 전달하고 후 객체 탐지 알고리즘(Yolo v3 알고리즘)을 통해 주차구역내 자동차의 유무를 파악 후 빈 주차 공간을 알려주는 시스템이다. 

이 시스템의 부가적인 서비스로는 QR코드를 통해 주차한 위치를 대략적으로 알 수 있는 애플리케이션도 포함되어 있다. 

이 프로젝트는 사용자의 편리한 주차 및 주차한 위치를 빠르게 찾을 수 있는 서비스를 제공하는 것이 목표이다.<br/><br/>


### **2. 프로젝트 개발 환경**

S/W 개발 환경
* - OS : Window 7
* - IDE : pyCharm, gedit
* - Language : C, Python3

H/W 개발 환경
* - Device : Jeson Nano, Rasberry PI 2.0
* - Commuticate : UDP Socket
* - Language : C, Python3<br/><br/>

### **3. 프로젝트 적용 기술**

#### 3-1. UDP Socket 통신
- PC → Jetson Nano  
SenTerm에서 촬영한 이미지를 SD카드를 통해 PC에 저장 후 PC를 통해 Jetson Nano로 전송

- Jetson Nano → PC  
이미지 처리에 대한 결과(주차구역 내 주차유무에 대한 정보)를 PC로 전송<br/><br/>

#### 3-2.이미지 처리
- OpenCV
이미지의 특정 위치(주차구역)를 자른 이미지 파일 저장
- Yolov3
자른 이미지 파일이 자동차인지 판단하여 자동차 유무 결정
자동차 유무에 대한 리스트 저장<br/><br/>

#### 3-3.User InterFace
- Pygame
주차구역에 대한 정보(자동차 유무)가 표시된 주차 도면을 스크린으로 출력
- Pandas
주차장 정보 테이블을 데이터 프레임으로 출력<br/><br/>

#### 3-4.Qr code
- QR code 생성을 도와주는 파이썬 모듈<br/><br/>















