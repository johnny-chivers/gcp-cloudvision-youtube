import io 
import os 

from google.cloud import vision 
from google.cloud.vision import types

# set the os GCP APP varibale
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'demo-cloud-vision-a403bea1be00.json'

#client for image annotate vision 
client = vision.ImageAnnotatorClient()

# image to send
file_name = os.path.abspath('/Users/johnathanchivers/Documents/visual-code/gcp-vision-python-demo/test-image.png')

#reading in the image file to memory
with io.open(file_name,'rb') as image_file:
    content = image_file.read()

# setting the image 
image = types.Image(content=content)

# making the request to vision 
response = client.label_detection(image=image)

labels = response.label_annotations

for label in labels:
    print(label)