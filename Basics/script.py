import cv2

#Loading Image
#Where, 0 = Grayscale and 1 = RGB
our_image = cv2.imread("cars.jpeg",0)

#Resizing our image
resized_image = cv2.resize(our_image, (400,400))


cv2.imshow("Cars image",resized_image)
cv2.imwrite("Generated_cars.jpeg", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
