import cv2

img = cv2.imread('donald_trump.jpeg')
while True:
    
    cv2.imshow('Puppy', img)

    if cv2.waitKey(1) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()