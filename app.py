#VIDEO STREAMING APP
# you need to watch the video to understand the code again and then write this code and learn about each of its component used 
# https://youtu.be/vF9QRJwJXJk?si=drGDdC5WWcb5eyi1

from flask import Flask, render_template, redirect, url_for, request, Response

import cv2 # opencv library for camera, video and other multimedia usages

app = Flask(__name__)
camera = cv2.VideoCapture(0) # 0- for webcam

        

@app.route('/')
def home():
    return render_template('index.html')

def generate_frames():
    #read the camera frame
    
    while True : 
        success ,frame = camera.read()

        if not success:
            break
        else:
            ret ,buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
        
        yield(b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            



@app.route('/video')
def video():
    return Response( generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame' ) #whenever Response calls a function a 'mimetype' is given


    

if __name__ == '__main__':
    app.run(debug=True)