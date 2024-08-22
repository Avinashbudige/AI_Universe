import torch 

def load_model(model_path):
    '''
    This function takes model path and initializes the yolov5
    '''
    model = torch.hub.load("ultralytics/yolov5","custom",path=model_path) #loading the model 
    return model