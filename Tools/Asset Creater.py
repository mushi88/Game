from tkinter import *

class Window(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master=master
        self.setup()
        
    def setup(self):
        self.master.title("Asset Creater")
        
        self.text=Text(self)
        
root=Tk()
App=Window(root)
root.mainloop()
