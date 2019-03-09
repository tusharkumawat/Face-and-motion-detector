import cv2

#Load Cascade
face_cascade = cv2.CascadeClassifier('venv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')

#Load image
our_image_color = cv2.imread("friends.jpg")
our_image_gray = cv2.cvtColor(our_image_color,cv2.COLOR_BGR2GRAY)

#detect face
faces = face_cascade.detectMultiScale(our_image_gray, scaleFactor = 1.05, minNeighbors = 5)

#Print out type and values of object faces
print(type(faces))
print(faces)

if len(faces) == 0:
    print("No faces")
else:
    for x,y,w,h in faces:
        our_image_rect = cv2.rectangle(our_image_color,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow("Face recognition", our_image_rect)
    cv2.waitKey(0)
    cv2.destroyAllWindows
