from tkinter import *
from tkinter import filedialog
from tkinter import font
from time import sleep
import ML_test_backend as Mlb
import numpy as np

BUTTON_WIDTH = 20 # number of letters
BUTTON_HEIGHT = 2 # number of lines
BUTTON_HEIGHTLIGHTCOLOR = "RED"
TEXT_WIDTH = 40 # number of letters
TEXT_HEIGHT = 4 # number of lines
WRAPLENGTH = 200 # number of pixels??
FONT = ""


def browseSourceLine():		
	sourceFolder.set("<no path>")
	text_browseSrc = Label(text="Source",anchor="w",master=root,width=TEXT_WIDTH,height=TEXT_HEIGHT,wraplength=WRAPLENGTH,font=FONT).grid(row=0,column=0)
	browseSourceBtn = Button(text="browse",master=root,height=BUTTON_HEIGHT, width=BUTTON_WIDTH,highlightcolor=BUTTON_HEIGHTLIGHTCOLOR,command=browseSrcAction).grid(row=0,column=1)
	folder_text = Label(textvariable=sourceFolder,master=root,width=TEXT_WIDTH,height=TEXT_HEIGHT,wraplength=WRAPLENGTH,font=FONT).grid(row=0,column=2)
	
def browseSrcAction():
	t = filedialog.askdirectory()
	sourceFolder.set(t)

def browseDestinationLine():
	destinationFolder.set("<no path>")
	text_browseDst = Label(text="Destination",anchor="w",master=root,width=TEXT_WIDTH,height=TEXT_HEIGHT,wraplength=WRAPLENGTH,font=FONT).grid(row=1,column=0)
	browseSourceBtn = Button(text="browse",master=root,height=BUTTON_HEIGHT, width=BUTTON_WIDTH,highlightcolor=BUTTON_HEIGHTLIGHTCOLOR,command=browseDstAction).grid(row=1,column=1)
	folder_text = Label(textvariable=destinationFolder,master=root,width=TEXT_WIDTH,height=TEXT_HEIGHT,wraplength=WRAPLENGTH,font=FONT).grid(row=1,column=2)

def browseDstAction():
	t = filedialog.askdirectory()
	destinationFolder.set(t)

def run():
	print("Running the Application")
	backend()
	

def quit():
	root.destroy()

def progress():
	if (progressBar.get() == "0 %"):
		sleep(2)
		progressBar.set("50 %")
	else:
		sleep(2)
		progressBar.set("100 %")

def backend():
	data, target = Mlb.load()
	print(data.shape)
	print(target.shape)
	return 0

#------------------------MAIN-------------------------------------#
root = Tk()
root.geometry("800x600")
FONT = font.Font(family='Consolas', size=12, weight='bold')

sourceFolder = StringVar()
browseSourceLine() #choose source folder - widgets

destinationFolder = StringVar()
browseDestinationLine() #choose destination folder - widgets

progressBar = StringVar()
progressBar.set("0 %")
progessBarLabel = Label(textvariable=progressBar,anchor="w",master=root,height=TEXT_HEIGHT,font=FONT).grid(row=3,column=1)

runBtn = Button(text="Run",master=root,height=BUTTON_HEIGHT, width=BUTTON_WIDTH,highlightcolor=BUTTON_HEIGHTLIGHTCOLOR,command=run).grid(row=5,column=0)
quitBtn = Button(text="Quit",master=root,height=BUTTON_HEIGHT, width=BUTTON_WIDTH,highlightcolor=BUTTON_HEIGHTLIGHTCOLOR, command=quit).grid(row=5,column=2)

root.mainloop()