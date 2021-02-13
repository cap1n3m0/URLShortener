from tkinter import *
import pyshorteners 
import webbrowser
import socket

gui = Tk() 

enteredText = ""

class Mode: 
    LOCAL = 0
    GLOBAL = 1

m = Mode()

class Account: 
    urls = [] 

class Global(Account): 
    def __init__(self): 
        self.username = ""
        self.password = ""
    
accounts = []

class Local(Account): 
    def __init__(self): 
        hostName = socket.gethostname()
        self.IP = socket.gethostbyname(hostName)


class GUI: 
    title = Label(gui, text="URl Shortener")
    accounts = Label(gui, text = "Make an account to save your URLs on any device!")
    local = Label(gui, text = "Or, save these URLs on your local browser!")
    goLocal = Button(gui, text = "Save locally", command = goLocally)
    haveAccount = Label(gui, text = "Have an account? Sign in")
    makeAccount = Button(gui, text = "Make Account", command = lambda: makeNewAccount())
    username = Label(gui, text = "Enter username: ")
    usernameBox = Entry(gui, bd = 10)
    password = Label(gui, text = "Enter password: ")
    passwordBox = Entry(gui, bd = 10)
    enter = Button(gui, text = "Enter", command = lambda: proceed())
    URlBox = Entry(gui, bd = 5)
    gui.geometry("800x1250")
    shortenButton = Button(gui, text = "Shorten URL", command = lambda: shortenURL(enteredText))
    giveNewURL = Label(gui, text = "")

g = GUI()

browser = 'safari'
short = ""

def makeNewAccount(): 
    m = Mode.GLOCAL

def signIn(): 
    m = Mode.GLOBAL

def goLocally(): 
    m = Mode.LOCAL

def proceed(): 
    pass

def openURL(URL): 
    webbrowser.get(browser).open(URL)

def shortenURL(URL): 
    global short 
    global g 
    global enteredText
    isThere = False
    enteredText = g.URlBox.get()
    s = pyshorteners.Shortener()
    short = s.tinyurl.short(URL)
    for s in URLS:
        if s[0] == IP and s[1] == short:
            print("Already exists: " + s[1])
            isThere = True

    if not isThere: 
        newValue = (IP, short) 
        URLS.append(newValue)
        print("Short is: " + short) 
        g.giveNewURL.labelText = "Success! Your URL has been shortened! You may now use this one: " + short
        g.giveNewURL.pack()
        openURL(URL)

g.title.pack()
g.accounts.pack()
g.local.pack()
g.URlBox.pack()
g.shortenButton.pack()

gui.mainloop() 
