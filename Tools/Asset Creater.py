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
        self.menu.add_cascade(label="File", menu=self.fmenu)
        
        self.fmenu.add_command(label="New", command=self.newfile)
        self.fmenu.add_command(label="Open File", command=self.openfile)
        self.fmenu.add_command(label="Save", command=self.savefile)
        self.fmenu.add_separator()
        self.fmenu.add_command(label="Exit", command=self.exitapp)
        
        self.bind("<Key">, self.key)
        
        self.text=Text(self)
        self.text.pack()
        
    def newfile(self):
        if not self.saved:
            if messagebox.askokcancel("Confirm", "Do you want to save this file?"):
                self.savefile()
        
        self.text.delete('1.0', END)
    
    def savefile(self):
        file=filedialog.asksaveasfile(mode='w')
        
        if file != None:
            Data=self.text.get('1.0', END+'-1c')
            file.write(Data)
            file.close()
            self.saved=True
    
    def openfile(self):
        
        if not self.saved:
            if messagebox.askokcancel("Confirm", "Do you want to save this file?"):
                self.savefile()
        
        file=filedialog.askopenfile(parent=self, mode='rb', title="Select a file")
        
        if file != None:
            Data=file.read()
            self.newfile()
            self.text.insert('1.0', Data)
            file.close()
    
    def key(self, event):
        if event.char=="":
            self.savefile()
        else:
            self.saved=False
    
    def exitwindow(self):
        if not self.saved:
            if messagebox.askokcancel("Confirm", "Do you want to save this file?"):
                self.savefile()
        
        if messagebox.askokcancel("Exit", "Do you really want to exit?"):
            self.master.destroy()
        
root=Tk()
App=Window(root)
root.mainloop()
