import cv2 

img = cv2.imread("test.jpeg") 
print(type(img)) 

# Shape of the image 
print("Shape of the image", img.shape) 

# [rows, columns] 
crop = img[50:180, 100:300] 

cv2.imshow('original', img) 
cv2.imshow('cropped', crop) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
