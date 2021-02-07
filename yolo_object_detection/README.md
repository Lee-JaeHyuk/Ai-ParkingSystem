

# Code Review

### 1. client.py
- Rasberry Pi 2.0 에서 촬영한 사진을 저장한 PC(client)에서 Jeston Nano(server)로 이미지 전송
- 이전에 server.py가 실행이 되어야 통신이 가능하다. 

### 2. server.py
- Jeston Nano는 client(PC)로 부터 전송을 받은 이미지를 처리한다.

### 3. img_Crop.py + img_processing
- client로 부터 받은 이미지를 처리 한다.

### 4. yolo_object_detection.py
- Yolo v3를 활용하여 처리 된 이미지에서 차량 이미지의 유무를 추출한다.

### 5. server_UI.py
- UI Client(PC)가 Server(Jetson Nano)로 ‘start’를 전송하면 Server에서 Yolo 수행 후 결과를 UI Client에게 전송한다.

### 6. client_UI.py
- Server(Jetson Nano)에서 Yolo 수행 결과값을 받은 UI Client(PC)는 pygame과 pandas를 이용해 UI를 생성한다.
