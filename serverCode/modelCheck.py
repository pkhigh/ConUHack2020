import os
command = "wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=" 
command += '1LyCAYafpLLebfzRaOwY1LA_zzH9aNQij' + "' -O model/model.pth"
if not(os.path.exists('model/model.pth')):
    os.system(command)