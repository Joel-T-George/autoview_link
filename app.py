import customtkinter as ctk

from src.manage import ManageApplication
import os
import sys


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class AutoviewLinkApp(ctk.CTk):
    def __init__(self):
        super().__init__()
     
        self.width = self.winfo_screenwidth()
        self.height= self.winfo_screenheight()

        self.title("Autoview_Link")
        self.geometry(f"{self.width}x{self.height}")

       


        self.AppManager = ManageApplication(self)

        
         
    

    def on_closing(self):
        
        self.destroy()
       