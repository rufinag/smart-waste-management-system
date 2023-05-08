# Smart Waste Managment System
The goal of this project was to create a low-cost computer vision based system to intelligently classify waste, based on the material composition of the bottle/can detected in real-time. The system was built and executed on the Raspberry Pi 3B, the video stream was captured using a webcam interfaced with the Pi via USB. The computer vision aspect of this project was built using the OpenCV Python library and the Machine Learning component of this project was developed using Tensorflow Lite. Our classification  model helps classifying waste bottles into 4 classes: Aluminium Cans, Glass, PET and HDPEM containers.

## Repository Organization
### Code
#### inference.py
This file contains python code to run compressed/quantized neural network model on inferencing mode. The system pipeline begins with setting up the OpenCV video capture     segment, this is followed by retrieving the machine learning model from the Raspberry Pi file system. During the real-time capture of video, the video is   captured frame-by-frame and resized to make the frame suitable for input into the model. The predictions made by the model are then mapped to the correponding label and printed along with the classification confidence score obtained from the model.
  
#### video_record.py
Python code to capture and write video data in real time. This was used to compile the data set used to train the model used in this project. 

#### EAI_finalproject_model.ipynb
This file contains splitting the data into training, validation, and test sets using a stratfied split. It also contains model development and training as well as reducing the size of the model by converting into a TensorFlow Lite model and using post-training quantization. In this file the base model and all the optimized models are also tested on the test dataset.

#### image_extraction.py
Python script for extracting frames from videos that we took for data collection. We varied the number of frames extracted per video depending on the number of images we wanted.

#### Data Collection.ipynb
This file contains all relevant code that we used for data collection and data pre-processing. In summary, it takes in raw jpeg images of bottles (and cans) resizes them to (224, 224, 3), adds labels corresponding to each image and normalizes the images. The images are then concatenated and stored in data.npy and labels are stored in labels.npy (the numpy files can be found in the data folder of this repository). 

### Data
For our data collection process, the images we collected for our project can be found here : https://drive.google.com/drive/folders/1EA7D0Gq1P7dKqUwgFPZ7LFWhi-s6jcrH?usp=sharing

The gdrive folder above contains the 'data.npy' and 'labels.npy' of 2311 images of 4 classes of waste bottles used in this project. The folders 'newimages' and 'ourimages' contain raw jpeg images.

As mentioned in project report, we initally also used images of waste bottles we found online, the repository of images can be found here: https://www.kaggle.com/datasets/arkadiyhacks/drinking-waste-classification?resource=download



