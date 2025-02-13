
from app import AutoviewLinkApp

app = AutoviewLinkApp()


if __name__ == "__main__":

    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()