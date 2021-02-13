from tkinter import *
import pyshorteners 
import webbrowser
import socket

gui = Tk() 

enteredText = ""

class Mode: 
    LOCAL = 0
    GLOBAL = 1

MODE = Mode()

class Account: 
    m = Mode()
    urls = [] 

class Global(Account): 
    m = Mode().GLOBAL
    def __init__(self): 
        self.username = ""
        self.password = ""

class Local(Account):
    m = Mode().LOCAL 
    def __init__(self): 
        hostName = socket.gethostname()
        self.IP = socket.gethostbyname(hostName)

account = []

class GUI: 
    gui.geometry("800x1250")
    title = Label(gui, text="URl Shortener")
    accounts = Label(gui, text = "Make an account to save your URLs on any device!")
    local = Label(gui, text = "Or, save these URLs on your local browser!")
    goLocal = Button(gui, text = "Save locally", command = lambda: localAccount())
    haveAccount = Label(gui, text = "Have an account? Sign in")
    makeAccount = Button(gui, text = "Make Account", command = lambda: makeNewAccount())
    username = Label(gui, text = "Enter username: ")
    usernameBox = Entry(gui, bd = 10)
    password = Label(gui, text = "Enter password: ")
    passwordBox = Entry(gui, bd = 10)
    enter = Button(gui, text = "Enter", command = lambda: proceed())
    URlBox = Entry(gui, bd = 5)
    shortenButton = Button(gui, text = "Shorten URL", command = lambda: shortenURL(enteredText))
    giveNewURL = Label(gui, text = "")

g = GUI()

class GlobalGUI(GUI):
    def Call(self): 
        g.username.pack()
        g.password.pack()
        g.enter.pack()


class Make(GlobalGUI): 
    def __init__(self):  
        g.makeAccount.pack()
        GlobalGUI.Call()


class Have(GlobalGUI): 
    def __init__(self):  
        g.haveAccount.pack()
        GlobalGUI.Call()
       

class LocalGUI(GUI): 
    def __init__(self):  
        g.enter.pack()
        g.URlBox.pack()
        g.shortenButton.pack()
        g.giveNewURL.pack()


browser = 'safari'
short = ""

def makeNewAccount(): 
    global Mode
    MODE = Mode.GLOCAL
    globalGui = GlobalGUI()

def signIn(): 
    global Mode
    MODE = Mode.GLOCAL
    globalGui = GlobalGUI()
    

def localAccount(): 
    global Mode
    MODE = Mode.LOCAL
    localGUI = LocalGUI()


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
    for s in Account().urls:
        if s[0] == Local().IP and s[1] == short:
            print("Already exists: " + s[1])
            isThere = True
    if not isThere: 
        newValue = (Local().IP, short) 
        Account().urls.append(newValue)
        print("Short is: " + short) 
        g.giveNewURL.labelText = "Success! Your URL has been shortened! You may now use this one: " + short
        g.giveNewURL.pack()
        openURL(URL)

g.title.pack()
g.accounts.pack()
g.local.pack()
g.goLocal.pack()
g.haveAccount.pack()
g.makeAccount.pack()

gui.mainloop() 
