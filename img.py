import torch
import torchvision.transforms as T
from PIL import Image

# Load the pre-trained YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Load and preprocess the image
image_path = r'C:\Users\AJ\Downloads\pexels-alexandra-novitskaya-2951921'
image = Image.open(image_path)
transform = T.Compose([T.ToTensor()])
image = transform(image)

# Perform inference
results = model([image])



