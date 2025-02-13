import customtkinter as ctk

from modules.video import VideoInterface

from PIL import Image, ImageTk

import threading

"""
    This Section used to Configuring Gui Video Playing overall functions

"""

class VideoFrame(ctk.CTkFrame):
    def __init__(self,master, **kwargs):
        super().__init__(master, **kwargs)
        

