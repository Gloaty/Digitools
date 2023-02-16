import tkinter
from tkinter.ttk import *

class digiTools():
    def __init__(self):
        def openHelpMenu():
            helpMenu = tkinter.Toplevel(self.root)
            helpMenu.title("Help Menu")
            helpMenu.geometry("500x250")

            helpLabel = tkinter.Label(text = "Welcome to Digitools! Thank you for downloading this application!")

            closeHelpMenu = tkinter.Button(text="Close", bd="5", command = self.root.destroy)
        self.root = tkinter.Tk()
        self.root.title("Digitools")
        self.root.geometry("1250x750")

        titleFont = ("Fixedsys", 20, "bold")
        masterFont = ("Fixedsys", 10)

        title = tkinter.Label(text = "Digitools")
        title.grid(row=0, column=1, padx=6, pady=4)
        title.configure(font = titleFont, bg="white")

        subtitle = tkinter.Label(text = "Digital Tools")
        subtitle.grid(row=0, column=2, padx=10, pady=8)
        subtitle.configure(font = masterFont, fg="grey", bg="white")

        help = tkinter.Button(text="Help Menu", bd = "5", command = openHelpMenu())
        help.grid(row=3, column=1, padx=20, pady=16)
        help.configure(font = masterFont, borderwidth=1)

app = digiTools()
app.root.mainloop()
