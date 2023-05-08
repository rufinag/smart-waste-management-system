# Smart Waste Managment System
The goal of this project was to create a low-cost computer vision based system to intelligently classify waste based on the material composition of the bottle/can in the image in real-time. The system was built and executed on the Raspberry Pi 3B, video stream was captured using a webcam interfaced with the Pi via USB. The computer vision aspect of this project is built using the OpenCV Python library and the Machine Learning component of this project was developed using Tensorflow Lite.

## Repository Organization
#### inference.py
Python code to run compressed/quantized neural network model on inferencing mode. The system pipeline begins with setting up the OpenCV video capture     segment, this is followed by retrieving the machine learning model from the Raspberry Pi file system. During the real-time capture of video, teh video is   captured frame-by-frame and resized to make the frame suitable for input into the model. The predictions made by the model are then mapped to the correponding label and printed along with the confidence score obtained from the model.
  
#### video_record.py
Python code to capture and write video data in real time. This was used to compile the data set used to train the model used in this project. 
