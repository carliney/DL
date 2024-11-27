<<<<<<< HEAD:DL/first.py

from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO("comet.pt")

# Run inference on an image
# results = model("the path of your images",save=True)  # list of 1 Results object
#example
results = model("./exp-images/001.jpg",save=True,conf=0.31, save_txt=True,save_crop=True,save_conf=True)  # list of 1 Results object

#c (2)
=======

from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO("comet.pt")

# Run inference on an image
# results = model("the path of your images",save=True)  # list of 1 Results object
#example
results = model("./exp-images/001.jpg",save=True,conf=0.31, save_txt=True,save_crop=True,save_conf=True)  # list of 1 Results object

#c (2)
>>>>>>> 731c15aea0efede28a64bd1ac0b2cbe73ad23125:ultralytics-main/first.py
