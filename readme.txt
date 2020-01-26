Intact Challenge using Computer Vision : 
    In this challenge, I try to solve the problem of autmoatic car model detection in an image.
    This information can be used to get the car model type of moving vehicles.
    Also, here along with knowing the car type I also localize the car in the scene which can be further used in various
    information extraction like license plate, damage location.
    The computer vision models are trained on 8k images of 196 classes of cars.
    Here I used transfer learning to train Mask-RCNN ResNet-50 model trained on COCO dataset as my initial starting point.
    
STATISTICS:
Dataset : Cars Dataset
Number of Classes : 196
Training framework used : detectron2 (Recently open sourced by Facebook)
Training Images : 8144
Testing Images : 8041

MAP(Mean Average Precision over all the classes) achieved by the best model on :

Training Data : 
Validation Data : 


MODEL IS LIVE: 

The model is live and running on a GPU server.
User can test the model by running test_app.py using python.
The user has to feed the path of the car image they want to test and the app will fetch the information from server.