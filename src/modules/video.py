import cv2
from PIL import Image
import numpy
import threading

import os
  # Shows the current working directory

class VideoInterface():
    def __init__(self):
        self.Frame = None

#         self.video_source = (
#     "rtspsrc location=rtsp://admin:Dhaksha123@192.168.6.116:554/live/ch00_0 latency=0 ! "
#     "rtph265depay ! h265parse ! avdec_h265 ! videoconvert ! appsink"
# )             
        # self.video_source = "filesrc location=/home/dhaksha/autoview_link/test/testImage.png ! decodebin ! imagefreeze ! videoconvert ! appsink"
        self.video_source = "filesrc location=/home/dhaksha/Downloads/1204911-hd_1920_1080_30fps.mp4 ! decodebin ! videoconvert ! appsink"
        
        self.cap = cv2.VideoCapture(self.video_source, cv2.CAP_GSTREAMER)
        self.running = False
        self.curFrameArray= []

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.startCapture, daemon=True)
        self.thread.start()
        print("Started..")
    
    def get_frame(self):
        return self.curFrameArray
    
    def startCapture(self):
        while self.running and self.cap.isOpened():
            ret , frame =self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.curFrameArray = Image.fromarray(frame)
            else:
                print("no Video Frame")
                print(os.getcwd())
                noFrame = Image.open("assests/no-signal.png")
                noFrameArray = numpy.array(noFrame)
                self.curFrameArray =Image.fromarray(noFrameArray)

            
    def stop(self):
        self.running = False
        self.cap.release()

    def getFrameShape(self):
        pass

    def isRunning(self):
        return self.running


    def dyanamic_resize_image(self, frame, max_width, max_height):
        """Resize image while maintaining the aspect ratio."""
        # Get original dimensions
        # Calculate the aspect ratio of the video
        aspect_ratio = self.ImageWidth / self.ImageHeight
        
        # Calculate the new width and height based on the window size while maintaining aspect ratio
        if max_width / max_height > aspect_ratio:
            # Width is too large for the given height; adjust width
            new_height = max_height
            new_width = int(aspect_ratio * new_height)
        else:
            # Height is too large for the given width; adjust height
            new_width = max_width
            new_height = int(new_width / aspect_ratio)


        padding_x = (max_width-new_width)//2
        padding_y = (max_height-new_height)//2

        # Ensure new_width and new_height are greater than zero
        if new_width > 0 and new_height > 0:
            # Resize the frame using the calculated new dimensions
            resized_frame = cv2.resize(frame, (new_width, new_height), interpolation=cv2.INTER_AREA)
            padded_frame = cv2.copyMakeBorder(resized_frame, padding_y, padding_y, padding_x, padding_x, cv2.BORDER_CONSTANT, value=[0, 0, 0])
            return padded_frame, padding_x,padding_y
        else:
            return frame  , padding_x,padding_y# If the dimensions invalid, return the original frame
