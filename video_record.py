'''
Video Capture Code
------------------------
Python code to capture data using webcam interfaced with Raspberry Pi.
'''

# import the opencv library
import cv2


# define a video capture object
vid = cv2.VideoCapture(-1, cv2.CAP_V4L)
if (vid.isOpened()==False):
    print("error reading file")
    
frame_width = int(vid.get(3))
frame_height = int(vid.get(4))

size = (frame_width, frame_height)

# Writing the video to file location on the raspberry pi
result = cv2.VideoWriter('/home/pi/Documents/embedded ai/record/glass3.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size)

while(True):
    
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    
    if(ret==True):
        result.write(frame)

        # Display the resulting frame
        cv2.imshow('frame', frame)
    
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    else:
        break


# After the loop release the cap object
vid.release()
result.release()
# Destroy all the windows
cv2.destroyAllWindows()
print("save successful")










