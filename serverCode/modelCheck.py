import os
command = "wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=" 
command += '1jSO2lVG_K8CrDfzA9AzzVtjSTu1gIBqe' + "' -O model/model.pth"
if not(os.path.exists('model/model.pth')):
    os.system(command)