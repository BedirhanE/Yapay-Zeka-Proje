import cv2
import pyttsx3  # Sesli geri bildirim için pyttsx3 kütüphanesi kullanılıyor.

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

# Sesli geri bildirim için motor oluştur
engine = pyttsx3.init()

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Yüz tespit edildiğinde sesli geri bildirim.
        engine.say("Bir yüz tespit edildi!")
        engine.runAndWait()

    cv2.imshow('Yüz Tanıma', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
