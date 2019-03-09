import cv2

#capture video
our_video = cv2.VideoCapture(0)



while True:
    #check if loaded correctly
    check, frame = our_video.read()
    print(check,"\n",frame)
    cv2.imshow("Capturing",frame)

    key = cv2.waitKey(1)
    print("Key",key)
    if(key == ord('q')):
        break

our_video.release()
cv2.destroyAllWindows
