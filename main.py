from tkinter import *
import pyshorteners 
import webbrowser

gui = Tk() 

enteredText = ""

class GUI: 
    title = Label(gui, text="URl Shortener")
    URlBox = Entry(gui, bd = 5)
    gui.geometry("800x1250")
    shortenButton = Button(gui, text = "Shorten URL", command = lambda: shortenURL(enteredText))
    giveNewURL = Label(gui, text = "")

g = GUI()

browser = 'safari'
short = ""

def openURL(URL): 
    webbrowser.get(browser).open(URL)

def shortenURL(URL): 
    global short 
    global g 
    global enteredText
    enteredText = g.URlBox.get()
    s = pyshorteners.Shortener()
    short = s.tinyurl.short(URL)
    print("Short is: " + short) 
    g.giveNewURL.labelText = "Success! Your URL has been shortened! You may now use this one: " + short
    g.giveNewURL.pack()
    openURL(URL)

g.title.pack()
g.URlBox.pack()
g.shortenButton.pack()

gui.mainloop() 
