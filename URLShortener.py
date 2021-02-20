from tkinter import *
import pyshorteners
import socket

accounts = []

main = Tk()
main.geometry("1250x800")
accountPage = None
newAccountPage = None
enteredURL = ""
short = ""

urlEntered = ""
titleFont = ("Times New Roman", 100)


def makeBlankSpace(gui, height):
    blankBox = Label(gui)
    blankBox.pack(ipady=height)


def showURL(URL):
    global short
    global main
    global urlEntered
    global appearHere
    appearHere.destroy()
    urlEntered = str(URL)
    s = pyshorteners.Shortener()
    newURL = s.tinyurl.short(urlEntered)
    newText = StringVar()
    try:
        newText.set("Your shortened URL is: " + newURL)
        shortURL = Entry(main, bd=0, state="readonly", width=40, textvariable=newText, font = ("Arial", 40))
        shortURL.pack()
    except:
        error = Label("Error! This URL is invalid. Try entering a valid URL like 'https:www.google.com' ")
        error.pack()


title = Label(main, text = "URL Shortener", font = titleFont)
subtitle = Label(main, text = "Just paste it in!", font = ("Arial", 40))
enterBox = Entry(main, width = 70)
pressEnter = Label(main, text = "Press the button below to get your shortened URL!", font = ("Arial", 30))
enterButton = Button(main, text = "Get", width = 20, height = 2, font = ("Arial", 20), command = lambda: showURL(enterBox.get()))
appearHere = Label(main, text = "Your shortened URL will appear here", font = ("Arial", 40))


def init():
    title.pack()
    makeBlankSpace(main, 8)
    subtitle.pack()
    makeBlankSpace(main, 3)
    enterBox.pack(ipady = 15)
    makeBlankSpace(main, 3)
    pressEnter.pack()
    makeBlankSpace(main, 3)
    enterButton.pack()
    makeBlankSpace(main, 3)
    appearHere.pack()

init()
main.mainloop()
