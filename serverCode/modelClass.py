from dt2Functions import *

class model:
    configPath = None
    weightsPath = None
    classes = None
    model = None
    thresh = 0.25
    nms = 0.5
    
    def load(self):
        self.model = load_net(self.configPath,self.weightsPath,self.nms)
    def detect(self,image):
        return detect(self.model,self.classes,self.thresh,image)
        