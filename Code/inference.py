'''
Inferencing Code
--------------------------------------------------------
Python code to run quantized neural network in inference
mode to classify recyclable waste in real-time.
'''
# import the opencv library
import cv2
import tflite_runtime
import tflite_runtime.interpreter as tt
import numpy as np

# Setting up video capture
vid = cv2.VideoCapture(-1, cv2.CAP_V4L)
if (vid.isOpened()==False):
    print("error reading file")
    
# Fetching model
tflite_model_path = '/home/pi/Documents/embedded ai/tf_lite_quant_model.tflite'
interpreter1 = tt.Interpreter(model_path=tflite_model_path)


# Get input and output details of the model
input_details = interpreter1.get_input_details()
output_details = interpreter1.get_output_details()

interpreter1.resize_tensor_input(input_details[0]['index'], (1,224,224,3))
interpreter1.resize_tensor_input(output_details[0]['index'], (1,5))
interpreter1.allocate_tensors()
input_details = interpreter1.get_input_details()
output_details = interpreter1.get_output_details()

labels = ['Aluminium Can', 'Glass', 'HDPEM(milk container)', 'PET'] 

i = 0
while(True):
    
    # Capture the video frame by frame
    ret, frame = vid.read()
    
    if(ret==True):
        # Display the resulting frame
        cv2.imshow('frame', frame)
        frame = cv2.resize(frame, (224, 224))
        
        # Inferencing using quantized model 
        img = np.array(frame).astype(np.float32)
        data = np.array([img])
        interpreter1.set_tensor(input_details[0]['index'], data)
        interpreter1.invoke()
        tflite_preds = interpreter1.get_tensor(output_details[0]['index'])
        preds = int(np.argmax(tflite_preds, axis=1))
        
        # Printing model predictions at every 10th iteration
        if (i%10==0):
            
            if (tflite_preds[0][preds] < 0.3):
                print('PREDICTION: Non-recyclable')
            else:
                print('PREDICTION: ', labels[preds], ' classification confidence: ', tflite_preds[0][preds])
        
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    else:
        break
        
    i += 1

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()