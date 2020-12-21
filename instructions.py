from tkinter import *                 # tkinter is library from which all the graphics are made possible in this program
from PIL import Image, ImageTk        # PIL is Pillow library; It is used for inserting image on window


# This creates main application window and sets its title and size
root = Tk()
root.title('Instructions')
root.geometry('700x400')
root.maxsize(700, 400)
root.minsize(700,400)

# This makes background image appear and stick to window
photo = Image.open('background.jpg')
photo = photo.resize((900, 600), Image.ANTIALIAS)
converted_photo = ImageTk.PhotoImage(photo)
background = Label(image=converted_photo)
background.pack()

# this label is for heading
head = Label(text='Instructions ', width=30, height=1, bg ='red', fg='white', font='Verdana 19 bold',relief=RAISED)
head.place(x=75, y=3)

# this label displays the main content or the instructions
main = Label(text='''
Objective of the game is simple: 
You have to make same arrangements of blocks on third pole as you see on the first pole.
And do it in minimum number of moves.

To do that, type in input box:
 (pole from which you want to move) space (pole to which you want to move)
 Example: If you want to move from pole 1 to 2, type : 1 2
 To finally execute click on Enter button
 
 Certain rules must be followed in these moves:
 - Only the block on the topmost position of every pole can move
 - Small blocks can be placed on large box
   but large blocks cannot be place on small
 
 Note : For every valid move, the Moves counter would increase by one
 otherwise it woud remain same.
 
 Happy Playing!!''',bg='yellow', fg='black',font='Times 13 ',relief=SUNKEN)
main.place(x=45,y=35)

# this makes application stay as long as user do not close it
root.mainloop()