#!/usr/bin/env python
# coding: utf-8

# ## Python Code for Leopard detection project

# In[ ]:


import cv2
from ultralytics import YOLO

# custom YOLOv8 model
model = YOLO('NTLeopard1.pt')  # Replace with your model path

# video capture
cap = cv2.VideoCapture(0)  # Video file path

# detection parameters threshold
conf_threshold = 0.7  #confidence level

while cap.isOpened():
    success, frame = cap.read()
    
    if not success:
        break

   
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Performs detection
    results = model.predict(rgb_frame, conf=conf_threshold, verbose=False)
    
    # Results
    for result in results:
        boxes = result.boxes.xyxy.cpu().numpy()
        confidences = result.boxes.conf.cpu().numpy()
        class_ids = result.boxes.cls.cpu().numpy().astype(int)
        
        
        for box, conf, cls_id in zip(boxes, confidences, class_ids):
            x1, y1, x2, y2 = map(int, box)
            
           
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            
            label = "Leopard Detected"  # Static text without confidence
            
            
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)

    # Displays the resulting frame
    cv2.imshow('Leopard Detection - YOLOv8', frame)

   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()


# In[ ]:


'''

/Users/sushantvidhate/Downloads/12972688_2160_4096_30fps.mp4     
/Users/sushantvidhate/Downloads/istockphoto-1469090082-640_adpp_is.mp4
/Users/sushantvidhate/Downloads/istockphoto-1470778447-640_adpp_is.mp4 

rtsp://admin:L2CB5EFB@192.168.31.21:554/cam/realmonitor?channel=1&subtype=0

'''

