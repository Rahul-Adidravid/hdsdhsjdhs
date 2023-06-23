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

# Extract bounding box information
boxes = results.xyxy[0]  # Get the bounding boxes
scores = results.names[0]  # Get the class names
confidence = results.xyxys[0][:, 4]  # Get the confidence scores

# Iterate over the bounding boxes and display the results
for box, score, conf in zip(boxes, scores, confidence):
    x1, y1, x2, y2 = box.tolist()
    label = f'{score} {conf:.2f}'
    print(f'Label: {label}, Coordinates: ({x1:.1f}, {y1:.1f})-({x2:.1f}, {y2:.1f})')
