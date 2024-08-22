#importing the libraries
from proper_project_mantainance.object_detection.src.models.utilss import load_model
import torch 
import yaml 
import cv2  
import platform 
import pathlib 

if platform.system() == "Windows":
    pathlib.PosixPath = pathlib.WindowsPath
else:
    pathlib.WindowsPath = pathlib.PosixPath


def main():
    #load configuration 
    with open("config.yaml","r") as file: 
        config = yaml.safe_load(file) 
        
    #load yolov5 model 
    model =  load_model(config['model_path'])
    
    # Initialize the video capture 
    cap = cv2.VideoCapture(config['video_source'])
    
    while True:
        ret,frame = cap.read() #getting the frame and result 
        
        if not ret:
            cap = cv2.VideoCapture(config['video_source']) 
            continue 
        
        image = [frame] #converting the frame to list 
        results = model(image) #sending the image to model and getting the result 
        
        # labels,cord = result.xyxyn[0][:,-1],result.xyxyn[0][:,:-1] #getting the labels and coordinates 
        
        # n = len(labels) 
        # Draw results on the frame
        results.render()
        
        #Display on the frame 
        cv2.imshow("Object detection",results.ims[0]) 
        
        #Exit 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break 
    cap.release() 
    cv2.destroyAllWindows() 


if __name__ == "__main__":
    main()