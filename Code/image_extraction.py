import os
import cv2

video_path = "/Users/vishnu/Desktop/Embedded AI Project/newvideos/plasticpet.mp4"
video = cv2.VideoCapture(video_path)
output_path = "/Users/vishnu/Desktop/Embedded AI Project/newimages/pet"

success = True
count = 1
image_id = 1

while success:
    success, frame = video.read()
    
    if success == True:
        
        
        # i want every 5th frame from video
        # thats why i used following line of code
        # i dont want all frames from video
        # so we can decide the outpt frames count according to us.
        
        if count%5 == 0:
            
            # specify the output path and file name
            # i used count as a file name
            # you can use any
            
            # name = str(image_id)+".jpg"
            # name = f"AluCan{image_id}.jpg"
            name = os.path.join(output_path, f"pet{str(image_id)}.jpg")
            image_id += 1
            
            # save the image
            cv2.imwrite(name,frame)
        
        count += 1
    else:
        break

print("Total Extracted Frames :",image_id)
