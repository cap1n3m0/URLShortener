from tkinter import *
import pyshorteners 
import webbrowser
import socket

gui = Tk() 

enteredText = ""
browser = 'safari'
short = ""

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

accounts = []

class GUI: 
    gui.geometry("800x1250")
    title = Label(gui, text="URL Shortener", width = 200)
    title.config(font = ("Courier", 60))
    accounts = Label(gui, text = "Make an account to save your URLs on any device!", font = ("Courier", 20))
    local = Label(gui, text = "Or, save these URLs on your local browser!", font = ("Courier", 20))
    goLocal = Button(gui, text = "Save locally", width  = 20, font = ("Courier", 20), command = lambda: localAccount())
    haveAccount = Label(gui, text = "Have an account?", font = ("Courier", 20))
    makeAccount = Label(gui, text = "New?", font = ("Courier", 20))
    makeAccountButton = Button(gui, text = "Make Account", font = ("Courier", 20), command = lambda: makeNewAccount())
    haveAccountButton = Button(gui, text = "Sign in", font = ("Courier", 20), command = lambda: makeNewAccount())
    username = Label(gui, text = "Enter username: ")
    usernameBox = Entry(gui, bd = 10)
    password = Label(gui, text = "Enter password: ")
    passwordBox = Entry(gui, bd = 10)
    enter = Button(gui, text = "Enter", command = lambda: proceed())    
    accountExists = Label(text = "Error! Account exists! Please sign in, reset your password, or make another account")
    emailBoxReset = Label(text = "Enter the email this account was registered with: ")
    resetEmail = Entry(gui, bd = 5)
    URlBox = Entry(gui, bd = 5)
    shortenButton = Button(gui, text = "Shorten URL", command = lambda: shortenURL(enteredText))
    giveNewURL = Label(gui, text = "")  
    # sendEmail = Label(text = "Send password reset email", command = resetMail)
    # emailButton = Button(gui, text = "Send mail to this account", command = lambda: resetMail())
    def makeBlank(self, h): 
        sizedBox = Label(gui, text = "", height = h)
        sizedBox.pack()

class Intro(GUI): 
    def __init__(self): 
        self.title.pack()
        self.makeBlank(3)
        self.accounts.pack()
        self.local.pack()
        self.makeBlank(3)
        self.goLocal.pack()
        self.makeBlank(3)
        self.haveAccount.pack()
        self.haveAccountButton.pack()
        self.makeBlank(3)
        self.makeAccount.pack()
        self.makeAccountButton.pack()

class Local(GUI): 
    def __init__(self): 
        self.enter.pack()
        self.URlBox.pack()
        self.shortenButton.pack()
        self.giveNewURL.pack()
        clearScreen(gui)

class Global(GUI):
    def __init__(self): 
        self.username.pack()
        self.usernameBox.pack(); 
        self.password.pack()
        self.passwordBox.pack(); 
        self.enter.pack()
        clearScreen(gui)


class Make(Global): 
    def __init__(self):  
        self.makeAccount.pack()
        self.Call(self)


class Have(Global): 
    def __init__(self):  
        self.haveAccount.pack()
        self.Call(self)


class Flag(GUI): 
    def __init__(self): 
        self.enter.pack()
        self.URlBox.pack()
        self.shortenButton.pack()
        self.giveNewURL.pack()
   

class NotFlag(GUI): 
    def __init__(self): 
        self.accountExists.pack()


class Success(GUI): 
    def __init__(self): 
        self.giveNewURL.labelText = "Success! Your URL has been shortened! You may now use this one: " + short
        self.giveNewURL.pack()


def resetMail(): 
    gui.sendEmail.pack()
    gui.emailBoxReset.pack()
    gui.resetEmail.pack()
    gui.emailButton.pack()

class Window(): 
    def __init__(self): 
        self.window = Tk()
        self.window.geometry("800x1250")
        self.title = Label(gui, text="URL Shortener", width = 200)
        self.title.config(font = ("Courier", 60))
        self.title.pack()
        self.accounts = Label(gui, text = "Make an account to save your URLs on any device!", font = ("Courier", 20))
        self.accounts.pack()
        self.local = Label(gui, text = "Or, save these URLs on your local browser!", font = ("Courier", 20))
        self.local.pack()
        self.goLocal = Button(gui, text = "Save locally", width  = 20, font = ("Courier", 20), command = lambda: localAccount())
        self.goLocal.pack()
        self.haveAccount = Label(gui, text = "Have an account?", font = ("Courier", 20))
        self.haveAccount.pack()
        self.makeAccount = Label(gui, text = "New?", font = ("Courier", 20))
        self.makeAccount.pack()
        self.makeAccountButton = Button(gui, text = "Make Account", font = ("Courier", 20), command = lambda: makeNewAccount())
        self.makeAccountButton.pack()
        self.haveAccountButton = Button(gui, text = "Sign in", font = ("Courier", 20), command = lambda: makeNewAccount())
        self.haveAccountButton.pack()
        self.username = Label(gui, text = "Enter username: ")
        self.username.pack()
        self.usernameBox = Entry(gui, bd = 10)
        self.usernameBox.pack()
        self.password = Label(gui, text = "Enter password: ")
        self.password.pack()
        self.passwordBox = Entry(gui, bd = 10)
        self.passwordBox.pack()
        self.enter = Button(gui, text = "Enter", command = lambda: proceed())    
        self.enter.pack()
        self.accountExists = Label(text = "Error! Account exists! Please sign in, reset your password, or make another account")
        self.accountExists.pack()
        self.sendEmail = Label(text = "Send password reset email", command = resetMail)
        self.sendEmail.pack()
        self.emailBoxReset = Label(text = "Enter the email this account was registered with: ")
        self.emailBoxReset.pack()
        self.resetEmail = Entry(gui, bd = 5)
        self.resetEmail.pack()
        self.emailButton = Button(gui, text = "Send mail to this account", command = lambda: resetMail())
        self.emailButton.pack()
        self.URlBox = Entry(gui, bd = 5)
        self.URlBox.pack()
        self.shortenButton = Button(gui, text = "Shorten URL", command = lambda: shortenURL(enteredText))
        self.shortenButton.pack()
        self.giveNewURL = Label(gui, text = "")  
        self.giveNewURL.pack()

    def makeBlank(self, window, h): 
        sizedBox = Label(window, text = "", height = h)
        sizedBox.pack()


def clearScreen(oldWindow): 
    window = Window()


def IntroGUI(): 
    intro = Intro()

def makeNewAccount(): 
    global Mode
    MODE = Mode.GLOBAL
    m = Make() 

def signIn(): 
    global Mode
    MODE = Mode.GLOBAL
    h = Have()
    

def localAccount(): 
    global Mode
    MODE = Mode.LOCAL
    localGUI = Local()


def proceed(acc): 
    flag = False
    for account in accounts: 
        if account == acc: 
            flag = False
    if flag: 
        accounts.add(acc) 
        flag = Flag()
    else: 
        notFlag = NotFlag()


def openURL(URL): 
    webbrowser.get(browser).open(URL)

def shortenURL(URL): 
    global short 
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
        success = Success()
        openURL(URL)

IntroGUI()

gui.mainloop() 
