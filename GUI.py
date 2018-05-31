#图形界面是个坑，到时候再看看

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alerButton =Button(self, text  ="hello", command = self.hello)
        self.alerButton.pack()

        self.helloLable = Label(self, text = "Helle")
        self.helloLable.pack()
        self.quitButton = Button(self, text = "quit", command = self.quit)
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or "world"
        messagebox.showinfo("Message", "hello, %s" %name)

app = Application()
app.master.title("hello")
app.mainloop()
