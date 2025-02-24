import customtkinter as ctk
from .videowidget import VideoFrame


class Home(ctk.CTkFrame):
    def __init__(self, master, backend, **kwargs):
        super().__init__(master, **kwargs)
    
        self.backend = backend
        self.sidebar_width = 400
        self.sidebar_visible = True


        self.video_frame = VideoFrame(self, sidebar_width=self.sidebar_width,VideoBackendService=self.backend['video'],fg_color="#010712")
        print(self.backend)
        self.video_frame.pack(side="left", fill="both", expand=True)

        self.sidebar = ctk.CTkFrame(self, width=self.sidebar_width, fg_color="darkgray")
        self.sidebar.pack(side="right", fill="y")

