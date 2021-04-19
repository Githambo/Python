import tkinter as tk
from PIL import Image,ImageTk
import random


root=tk.Tk()
root.geometry('500x500')
root.title('DICE GAME')

BlankLine=tk.Label(root,text="")
BlankLine.pack()

HeadingLabel=tk.Label(root,text="Welcome to Dice Game",fg="light green",bg="grey",font="Helvica 16 bold")
HeadingLabel.pack()

dice=['die1.png','die2.png','die3.png','die4.png','die5.png','die6.png',]
DiceImage1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
DiceImage2=ImageTk.PhotoImage(Image.open(random.choice(dice)))


ImageLabel1=tk.Label(root,image=DiceImage1)
ImageLabel1.image=DiceImage1
ImageLabel1.pack(expand=True)

ImageLabel2=tk.Label(root,image=DiceImage2)
ImageLabel2.image=DiceImage2
ImageLabel2.pack(expand=True)

def computer_roll_dice():
	DiceImage1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
	DiceImage2=ImageTk.PhotoImage(Image.open(random.choice(dice)))
	ImageLabel1.configure(image=DiceImage1)
	ImageLabel1.image=DiceImage1
	ImageLabel2.configure(image=DiceImage2)
	ImageLabel2.image=DiceImage2
	
def user_roll_dice():
	DiceImage1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
	DiceImage2=ImageTk.PhotoImage(Image.open(random.choice(dice)))
	ImageLabel1.configure(image=DiceImage1)
	ImageLabel1.image=DiceImage1
	ImageLabel2.configure(image=DiceImage2)
	ImageLabel2.image=DiceImage2

if computer_roll_dice:
	button=button=tk.Button(root,text="COMPUTER TURN",bg="red",command=computer_roll_dice)
	button.pack()
else:
	button=tk.Button(root,text="YOUR TURN ",bg="red",command=user_roll_dice)
	button.pack()














root.mainloop()