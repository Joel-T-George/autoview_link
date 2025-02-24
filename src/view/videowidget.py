from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..modules.video import VideoInterface





import customtkinter as ctk
from PIL import Image, ImageTk
import threading



"""
    This Section used to Configuring Gui Video Playing overall functions

"""

class VideoFrame(ctk.CTkFrame):
    def __init__(self,master,sidebar_width, VideoBackendService: "VideoInterface",**kwargs):
        super().__init__(master, **kwargs)
        self.video_service = VideoBackendService
        self.sidebar_width = sidebar_width
        self.video_service.start()



        self.update_frame()
    

        self.videoFrame_label = ctk.CTkLabel(self, text="", cursor="cross")
        self.videoFrame_label.pack(fill="both",expand=True)

  

    def update_frame(self):
        if self.video_service.isRunning():
        
            frame = self.video_service.get_frame()
            if frame:
                frame = ctk.CTkImage(light_image=frame, dark_image=frame,size=(self.videoFrame_label.winfo_width(), self.videoFrame_label.winfo_height()) )
                self.videoFrame_label.after(10, lambda: self.videoFrame_label.configure(image=frame))

        self.after(30, self.update_frame) 
            
        

