import cv2
from tracker import *

# Create tracker object
tracker = EuclideanDistTracker()

cap = cv2.VideoCapture('videos/4K Road traffic.mp4')
cap = cv2.VideoCapture('videos/Road traffic video for object.mp4')
# cap = cv2.VideoCapture('videos/troca de passes.mp4')

# Object Detection
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

while True:
    ret, frame = cap.read()
    
    height, width, _ = frame.shape
    print(height, width)
    # Extract Region of interest
    roi = frame[100:700, 200:600]
    
    
    mask = object_detector.apply(frame)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    
    # teste 
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []
    for cnt in contours:
        # Calculate Area and remove small elements
        area = cv2.contourArea(cnt)
        if area > 500:
            # cv2.drawContours(frame, [cnt], -1, (0,255,0), 2)
            x,y,w,h = cv2.boundingRect(cnt)
            # cv2.rectangle(roi, (x,y), (x+w, y+h), (0, 255,0), 3)
            cv2.rectangle(frame, (x , y), (x + w, y + h), (0, 255, 0), 3)
            # print([x,y,w,h])
            detections.append([x, y, w, h])
    
    # Object Tracking
    
    boxes_ids = tracker.update(detections)
    # print(boxes_ids)
    for box_id in boxes_ids:
        x, y, w, h, id = box_id
        cv2.putText(frame, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    
    cv2.imshow("roi", roi)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    
    key = cv2.waitKey(60)
    
    if key == 27:
        break
        
cap.release()
cv2.destroyAllWindows()