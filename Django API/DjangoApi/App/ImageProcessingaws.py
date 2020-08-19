import boto3
import requests



def ObjectDetection(imagePath, Service):
    
    session = boto3.Session(profile_name="default")
    Service = session.clint("rekognition")
    image = open(imagePath,"rb").read()
    response = Service.detect_labels(Image = {"Bytes": image})
    print(response)

image = "D:\College section\Language practice\Python Practice\Django API\DjangoApi\MyUpload\2.jpg"
ObjectDetection(image,"Object Detection")    