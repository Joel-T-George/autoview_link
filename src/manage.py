import customtkinter as ctk
from .modules.video import VideoInterface
from .view.home import Home
class ManageApplication():
    """

            Setting up overall Gui Interfaces

            Network Scanner button


            - Master Tab 
                - Connection
                - Video Viewer and Controller
                - Setting
                - Recording
                - UAV Setup
                - MultiCamera Viewer
                - Optional

            Expection Handling..
            
            concurrent communication with Camera Video , AI or Object Model , Tracker , Controll Communication

            feedback and status bar
    """
   
    def __init__(self, root):
        self.root = root
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.Services = {
            "video":VideoInterface()
        }
        # Menu Section Created  Here
        self.create_menu_bar()
        self.create_tab_view()
        self.create_status_bar()

        

       
    
    def create_menu_bar(self):      
        self.menu_bar = ctk.CTkFrame(self.root, height=30, corner_radius=0)
        self.menu_bar.grid(row=0, column=0, sticky="we")
        self.menu_label = ctk.CTkLabel(self.menu_bar, text="Menu Bar", font=("Arial", 14, "bold"))
        self.menu_label.pack(pady=3)
    
    def create_tab_view(self):
        self.tabview_frame = ctk.CTkFrame(self.root)
        self.tabview_frame.grid(row=1, column=0, sticky="nswe", padx=5, pady=5)
        self.tabview_frame.grid_columnconfigure(1, weight=1)
        self.tabview_frame.grid_rowconfigure(0, weight=1)

  

        self.tabview = ctk.CTkTabview(self.tabview_frame)
        self.tabview.grid(row=0, column=1, sticky="nswe")
        self.tabview._segmented_button.grid(sticky="w")

        self.tab1 = self.tabview.add("Home")
        self.tab2 = self.tabview.add("Connection")
        self.tab3 = self.tabview.add("Record")

        self.sidebar_tab = Home(self.tab1, backend = self.Services)
        self.sidebar_tab.pack(fill="both", expand=True)

        ctk.CTkLabel(self.tab2, text="Settings Tab", font=("Arial", 18)).pack(pady=20)
        ctk.CTkLabel(self.tab3, text="About Tab", font=("Arial", 18)).pack(pady=20)

        self.tabview._segmented_button.grid(row=0, column=0, sticky="nw", padx=0, pady=1)
        for tab in self.tabview._segmented_button._buttons_dict.values():
            tab.configure(width=50, height=25, font=("Arial", 16)) 
    
    def create_status_bar(self):
        self.status_bar = ctk.CTkFrame(self.root, height=30)
        self.status_bar.grid(row=2, column=0, sticky="we")
        self.status_label = ctk.CTkLabel(self.status_bar, text="Status: Ready", font=("Arial", 12))
        self.status_label.pack(side="left", padx=10)

    

