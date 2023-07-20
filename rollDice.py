

import tkinter as tk
from PIL import Image, ImageTk
import random

#Config window
window=tk.Tk()
window.geometry('600x600')
window.title('DICE')


#images
dice=['die1.png','die2.png','die3.png','die4.png','die5.png','die6.png']

#Funtion of button
def rollDice():

    colors = ["red", "blue", "green", "yellow", "orange", "purple","gold","salmon","indigo","teal","lime","magenta","cyan"]
    randomColor = random.choice(colors)

    diceImage=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    imageLabel.configure(image=diceImage)
    imageLabel.image=diceImage
    window.configure(background=randomColor)
    imageLabel.configure(background=randomColor)
    lineBlank.configure(background=randomColor)
    lineHead.configure(background=randomColor)

#ADD label in the frame
lineBlank=tk.Label(window, text="")
lineBlank.pack()

#Add label title
lineHead=tk.Label(window,text="ROLL DICE", fg="light green",bg="dark green",font="Helvetica 16 bold italic")
lineHead.pack()

#BUTTON
button=tk.Button(window,text='Roll',fg='blue',command=rollDice)
button.pack(expand=True)


#Start the dice
diceImage=ImageTk.PhotoImage(Image.open(random.choice(dice)))

#label for image
imageLabel=tk.Label(window,image=diceImage)
imageLabel.image=diceImage
imageLabel.pack(expand=True)


#LOOP
window.mainloop()