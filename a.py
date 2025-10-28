import requests, json, base64, cv2

import requests

import json

import base64

import cv2

import os



# Replace with your container public IP and API key

CONTAINER_URL = "http://172.212.37.14:5000/vision/v3.2/analyze"

API_KEY = "029t5TCZ6NipROHLAUOCoAeOlckeWJufxI9JKAFk53UAN5TG17XkJQQJ99BJACYeBjFXJ3w3AAAFACOGGtYt"


CONTAINER_URL = process.env.CONTAINER_URL
API_KEY = process.env.API_KEY



# Try to capture one frame from the default webcam

print("Attempting to capture image from webcam...")

cam = cv2.VideoCapture(0)  # specify camera index (0 = default camera)

ret, frame = cam.read()

cam.release()



if not ret or frame is None:

    print("⚠️ Could not capture image from webcam. Trying fallback image...")

    fallback_path = "test.jpg"  # make sure this file exists

    if os.path.exists(fallback_path):

        frame = cv2.imread(fallback_path)

    else:

        raise RuntimeError("Could not capture image and no fallback image found.")



# Encode image to Base64

_, buf = cv2.imencode(".jpg", frame)

img_base64 = base64.b64encode(buf).decode("utf-8")



# Prepare API request

headers = {

    "Ocp-Apim-Subscription-Key": API_KEY,

    "Content-Type": "application/json"

}

data = {

    "url": "data:image/jpeg;base64," + img_base64,

    "features": ["objects"]

}



print("Sending request to vision container...")

resp = requests.post(CONTAINER_URL, headers=headers, json=data)





# Print response

print("Status:", resp.status_code)

try:

    print(json.dumps(resp.json(), indent=2))

except Exception:

    print("Response text:", resp.text)







# Backup Plan





#Scope Department of Health.

#1 . Analyse Videos

#2 . Semantics or Take informatoin of object or elements in the Frame Picu

#3 . It will go AI agents to feed the information to DB

#4. AI Agents will create Power BI Dasboard.



