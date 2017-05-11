from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class Window(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master=master
        self.text=None
        self.setup()
        
    def setup(self):
        self.master.title("Asset Creater")
        
        self.menu=Menu(self)
        self.fmenu=Menu(self.menu)
        self.master.config(menu=self.menu)
        self.menu.add_cascade(label="File", menu=fmenu)
        
        self.fmenu.add_command(label="New", command=newfile)
        self.fmenu.add_command(label="Open File", command=openfile)
        self.fmenu.add_command(label="Save", command=savefile)
        self.fmenu.add_separator()
        self.fmenu.add_command(label="Exit", command=exitapp)
        
    def newfile(self):
        if not self.text==None:
            self.text.pack_forget()
        
        self.text=Text(self)
        self.text.pack()
        
    def savefile(self):
        file=filedialog.asksaveasfile(mode='w')
        
        if file != None:
            Data=self.text.get('1.0', END+'-1c')
            file.write(Data)
            file.close()
    
    def openfile(self):
        file=filedialog.askopenfile(parent=self, mode='rb', title="Select a file")
        
        if file != None:
            Data=file.read()
            self.newfile()
            self.text.insert('1.0', Data)
            file.close()
    
    def exitwindow(self):
        if messagebox.askokcancel("Exit", "Do you really want to exit?"):
            self.master.destroy()
        
root=Tk()
App=Window(root)
root.mainloop()
