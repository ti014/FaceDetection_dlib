import cv2
import dlib
import numpy as np
import os

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(r'model.dat')

usb_camera_index = 0
cap = cv2.VideoCapture(usb_camera_index)

image_count = 1

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        landmarks = predictor(gray, face)
        landmarks = np.array([[p.x, p.y] for p in landmarks.parts()])
        
        # Tạo đường dẫn cho file ảnh
        filename = f"detected_face_{image_count}.jpg"
        
        if os.path.exists(filename):
            # Ghi đè lên tệp đó nếu đã tồn tại
            cv2.imwrite(filename, frame[face.top():face.bottom(), face.left():face.right()])
            print(f"Đã ghi đè lên {filename}")
        else:
            # Lưu ảnh khi phát hiện khuôn mặt
            face_img = frame[face.top():face.bottom(), face.left():face.right()]
            cv2.imwrite(filename, face_img)
            print(f"Đã lưu ảnh {filename}")
            
        image_count += 1

        for (x, y) in landmarks:
            cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
    cv2.imshow("TEST", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if image_count > 10: 
        break

cap.release()
cv2.destroyAllWindows()
