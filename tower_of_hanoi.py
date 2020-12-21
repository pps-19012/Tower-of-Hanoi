# importing OS module to open another file(in a function below), directly from this file, through command prompt
import os

# tkinter is library from which all the graphics are made possible in this program
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk       # PIL is Pillow library; It is used for inserting image on window


# This creates main application window and sets its title and size
root = Tk()
root.title('Tower of Hanoi')
root.geometry('900x600')
root.maxsize(900, 600)


# This makes background image appear and stick to window
photo = Image.open('background.jpg')
photo = photo.resize((900, 600), Image.ANTIALIAS)
converted_photo = ImageTk.PhotoImage(photo)
background = Label(image=converted_photo)
background.pack()


# Labels for the horizontal base and three poles
base = Label(text='', bg='brown', width=100, height=2, borderwidth=3, relief=SUNKEN)
base.place(x=100, y=300)
pole1 = Label(bg='brown', width=2, height=15, borderwidth=2, relief=SUNKEN)
pole1.place(x=200, y=70)
pole2 = Label(bg='brown', width=2, height=15, borderwidth=2, relief=SUNKEN)
pole2.place(x=430, y=70)
pole3 = Label(bg='brown', width=2, height=15, borderwidth=2, relief=SUNKEN)
pole3.place(x=650, y=70)


# These are various Labels of boxes(red,yellow,green,blue) which are possible
# These are named according to position, like smallest box is named 'one' and
# if it is at bottom(or '4'th position) of first pole then it is named one_1_4
# The boxes of first poles are already placed as they must be visible from start of the game
one_1_1 = Label(bg='red', width=5, height=2, borderwidth=3, relief=RAISED)
one_1_1.place(x=190, y=152)
one_1_2 = Label(bg='red', width=5, height=2, borderwidth=3, relief=RAISED)
one_1_3 = Label(bg='red', width=5, height=2, borderwidth=3, relief=RAISED)
one_1_4 = Label(bg='red', width=5, height=2, borderwidth=3, relief=RAISED)
one_2_1 = Label(bg='red', width=5, height=2, borderwidth=3, relief=RAISED)
one_2_2 = Label(bg='red', width=5, height=2, borderwidth=3, relief=RAISED)
one_2_3 = Label(bg='red', width=5, height=2, borderwidth=3, relief=RAISED)
one_2_4 = Label(bg='red', width=5, height=2, borderwidth=3, relief=RAISED)
one_3_1 = Label(bg='red', width=5, height=2, borderwidth=3, relief=RAISED)
one_3_2 = Label(bg='red', width=5, height=2, borderwidth=3, relief=RAISED)
one_3_3 = Label(bg='red', width=5, height=2, borderwidth=3, relief=RAISED)
one_3_4 = Label(bg='red', width=5, height=2, borderwidth=3, relief=RAISED)

two_1_2 = Label(bg='Yellow', width=10, height=2, borderwidth=3, relief=RAISED)
two_1_2.place(x=170, y=189)
two_1_3 = Label(bg='Yellow', width=10, height=2, borderwidth=3, relief=RAISED)
two_1_4 = Label(bg='Yellow', width=10, height=2, borderwidth=3, relief=RAISED)
two_2_2 = Label(bg='Yellow', width=10, height=2, borderwidth=3, relief=RAISED)
two_2_3 = Label(bg='Yellow', width=10, height=2, borderwidth=3, relief=RAISED)
two_2_4 = Label(bg='Yellow', width=10, height=2, borderwidth=3, relief=RAISED)
two_3_2 = Label(bg='Yellow', width=10, height=2, borderwidth=3, relief=RAISED)
two_3_3 = Label(bg='Yellow', width=10, height=2, borderwidth=3, relief=RAISED)
two_3_4 = Label(bg='Yellow', width=10, height=2, borderwidth=3, relief=RAISED)

three_1_3 = Label(bg='Green', width=15, height=2, borderwidth=3, relief=RAISED)
three_1_3.place(x=155, y=226)
three_1_4 = Label(bg='Green', width=15, height=2, borderwidth=3, relief=RAISED)
three_2_3 = Label(bg='Green', width=15, height=2, borderwidth=3, relief=RAISED)
three_2_4 = Label(bg='Green', width=15, height=2, borderwidth=3, relief=RAISED)
three_3_3 = Label(bg='Green', width=15, height=2, borderwidth=3, relief=RAISED)
three_3_4 = Label(bg='Green', width=15, height=2, borderwidth=3, relief=RAISED)

four_1_4 = Label(bg='Blue', width=20, height=2, borderwidth=3, relief=RAISED)
four_1_4.place(x=140, y=263)
four_2_4 = Label(bg='Blue', width=20, height=2, borderwidth=3, relief=RAISED)
four_3_4 = Label(bg='Blue', width=20, height=2, borderwidth=3, relief=RAISED)


# These lists will help in placing all the boxes at any moves
# so contain all the labels
one1 = [one_1_4, one_1_3, one_1_2, one_1_1]
one2 = [one_2_4, one_2_3, one_2_2, one_2_1]
one3 = [one_3_4, one_3_3, one_3_2, one_3_1]
two1 = [two_1_4, two_1_3, two_1_2, 0]
two2 = [two_2_4, two_2_3, two_2_2, 0]
two3 = [two_3_4, two_3_3, two_3_2, 0]
three1 = [three_1_4, three_1_3, 0, 0]
three2 = [three_2_4, three_2_3, 0, 0]
three3 = [three_3_4, three_3_3, 0, 0]
four1 = [four_1_4, 0, 0, 0]
four2 = [four_2_4, 0, 0, 0]
four3 = [four_3_4, 0, 0, 0]


# These are actual list(in the order of 'pole') which will help in identifying validity of move
# and will keep on changing
# like here 1st pole in intially filled with boxes from bottom to top as 4,3,2,1
a = [4, 3, 2, 1]
b = []
c = []

# the variable 'score' can now be used in any function also without defining it at first in a function
global score
score = 0

# blank input box
input_from_user = Entry(width=6, font = 'Verdana 20 bold')
input_from_user.place(x=100, y=425)

# this will make the 'instructions.py', i.e. the instruction(how to play) window appear through command prompt
def help() :
    os.system('python instructions.py')

# function which will carry out all opertaions/moves on clicking Enter button
def clicked():
    conf_var = 0
    res = input_from_user.get().split()
    input_from_user.delete(0, END)
    # below there are 6 if,elif which consider all situations of movements(which are 6)
    # like moving from 1 to 2, 1 to 3, 2 to 1, 2 to 3, 3 to 1, 3 to 2
    # same block of code is repeated 6 times with some change to compare different things
    if int(res[0]) == 1 and int(res[1]) == 2:
        if a[-1] == 1:
            if len(b) == 0 :           # this code at all places, checks if b/a/c is empty
                conf_var = 1           # or top block of b/a/c is greater than block which is going to be placed
            elif 1 < b[-1] :           # if any condition satisfy then it vhanges flag variable
                conf_var = 1
            if conf_var == 1 :
                i = a.index(1)
                if len(b) == 0:
                    (one1[i]).place_forget()            # this code at all places, vanishes the moving block
                    one_2_4.place(x=420, y=263)         # from original place and moves it to new place
                    a.remove(1)
                    b.append(1)                         # this code at all places, make changes in lists
                elif len(b) == 1:                       # a,b,c which will perform actual operations
                    (one1[i]).place_forget()
                    one_2_3.place(x=420, y=226)
                    a.remove(1)
                    b.append(1)
                elif len(b) == 2:
                    (one1[i]).place_forget()
                    one_2_2.place(x=420, y=189)
                    a.remove(1)
                    b.append(1)
                elif len(b) == 3:
                    (one1[i]).place_forget()
                    one_2_1.place(x=420, y=152)
                    a.remove(1)
                    b.append(1)
        elif a[-1] == 2:
            if len(b) == 0 :
                conf_var = 1
            elif 2 < b[-1] :
                conf_var = 1
            if conf_var == 1 :
                i = a.index(2)
                if len(b) == 0:
                    (two1[i]).place_forget()
                    two_2_4.place(x=400, y=263)
                    a.remove(2)
                    b.append(2)
                elif len(b) == 1:
                    (two1[i]).place_forget()
                    two_2_3.place(x=400, y=226)
                    a.remove(2)
                    b.append(2)
                elif len(b) == 2:
                    (two1[i]).place_forget()
                    two_2_2.place(x=400, y=189)
                    a.remove(2)
                    b.append(2)
        elif a[-1] == 3:
            if len(b) == 0:
                conf_var = 1
            elif 3 < b[-1]:
                conf_var = 1
            if conf_var == 1:
                i = a.index(3)
                if len(b) == 0:
                    (three1[i]).place_forget()
                    three_2_4.place(x=385, y=263)
                    a.remove(3)
                    b.append(3)
                elif len(b) == 1:
                    (three1[i]).place_forget()
                    three_2_3.place(x=385, y=226)
                    a.remove(3)
                    b.append(3)
        elif a[-1] == 4:
            if len(b) == 0 :
                conf_var = 1
            elif 4 < b[-1] :
                conf_var = 1
            if conf_var == 1 :
                i = a.index(4)
                if len(b) == 0:
                    (four1[i]).place_forget()
                    four_2_4.place(x=370, y=263)
                    a.remove(4)
                    b.append(4)
    if int(res[0]) == 1 and int(res[1]) == 3:
        if a[-1] == 1:
            if len(c) == 0:
                conf_var = 1
            elif 1 < c[-1]:
                conf_var = 1
            if conf_var == 1:
                i = a.index(1)
                if len(c) == 0:
                    (one1[i]).place_forget()
                    one_3_4.place(x=640, y=263)
                    a.remove(1)
                    c.append(1)
                elif len(c) == 1:
                    (one1[i]).place_forget()
                    one_3_3.place(x=640, y=226)
                    a.remove(1)
                    c.append(1)
                elif len(c) == 2:
                    (one1[i]).place_forget()
                    one_3_2.place(x=640, y=189)
                    a.remove(1)
                    c.append(1)
                elif len(c) == 3:
                    (one1[i]).place_forget()
                    one_3_1.place(x=640, y=152)
                    a.remove(1)
                    c.append(1)
        elif a[-1] == 2:
            if len(c) == 0:
                conf_var = 1
            elif 2 < c[-1]:
                conf_var = 1
            if conf_var == 1:
                i = a.index(2)
                if len(c) == 0:
                    (two1[i]).place_forget()
                    two_3_4.place(x=620, y=263)
                    a.remove(2)
                    c.append(2)
                elif len(c) == 1:
                    (two1[i]).place_forget()
                    two_3_3.place(x=620, y=226)
                    a.remove(2)
                    c.append(2)
                elif len(c) == 2:
                    (two1[i]).place_forget()
                    two_3_2.place(x=620, y=189)
                    a.remove(2)
                    c.append(2)
        elif a[-1] == 3:
            if len(c) == 0:
                conf_var = 1
            elif 3 < c[-1]:
                conf_var = 1
            if conf_var == 1:
                i = a.index(3)
                if len(c) == 0:
                    (three1[i]).place_forget()
                    three_3_4.place(x=605, y=263)
                    a.remove(3)
                    c.append(3)
                elif len(c) == 1:
                    (three1[i]).place_forget()
                    three_3_3.place(x=605, y=226)
                    a.remove(3)
                    c.append(3)
        elif a[-1] == 4:
            if len(c) == 0:
                conf_var = 1
            elif 4 < c[-1]:
                conf_var = 1
            if conf_var == 1:
                i = a.index(4)
                if len(c) == 0:
                    (four1[i]).place_forget()
                    four_3_4.place(x=590, y=263)
                    a.remove(4)
                    c.append(4)
    if int(res[0]) == 2 and int(res[1]) == 1:
        if b[-1] == 1:
            if len(a) == 0:
                conf_var = 1
            elif 1 < a[-1]:
                conf_var = 1
            if conf_var == 1:
                i = b.index(1)
                if len(a) == 0:
                    (one2[i]).place_forget()
                    one_1_4.place(x=190, y=263)
                    b.remove(1)
                    a.append(1)
                elif len(a) == 1:
                    (one2[i]).place_forget()
                    one_1_3.place(x=190, y=226)
                    b.remove(1)
                    a.append(1)
                elif len(a) == 2:
                    (one2[i]).place_forget()
                    one_1_2.place(x=190, y=189)
                    b.remove(1)
                    a.append(1)
                elif len(a) == 3:
                    (one2[i]).place_forget()
                    one_1_1.place(x=190, y=152)
                    b.remove(1)
                    a.append(1)
        elif b[-1] == 2:
            if len(a) == 0:
                conf_var = 1
            elif 2 < a[-1]:
                conf_var = 1
            if conf_var == 1:
                i = b.index(2)
                if len(a) == 0:
                    (two2[i]).place_forget()
                    two_1_4.place(x=170, y=263)
                    b.remove(2)
                    a.append(2)
                elif len(a) == 1:
                    (two2[i]).place_forget()
                    two_1_3.place(x=170, y=226)
                    b.remove(2)
                    a.append(2)
                elif len(a) == 2:
                    (two2[i]).place_forget()
                    two_1_2.place(x=170, y=189)
                    b.remove(2)
                    a.append(2)
        elif b[-1] == 3:
            if len(a) == 0:
                conf_var = 1
            elif 3 < a[-1]:
                conf_var = 1
            if conf_var == 1:
                i = b.index(3)
                if len(a) == 0:
                    (three2[i]).place_forget()
                    three_1_4.place(x=155, y=263)
                    b.remove(3)
                    a.append(3)
                elif len(a) == 1:
                    (three2[i]).place_forget()
                    three_1_3.place(x=155, y=226)
                    b.remove(3)
                    a.append(3)
        elif b[-1] == 4:
            if len(a) == 0:
                conf_var = 1
            elif 4 < a[-1]:
                conf_var = 1
            if conf_var == 1:
                i = b.index(4)
                if len(a) == 0:
                    (four2[i]).place_forget()
                    four_1_4.place(x=140, y=263)
                    b.remove(4)
                    a.append(4)
    if int(res[0]) == 2 and int(res[1]) == 3:
        if b[-1] == 1:
            if len(c) == 0:
                conf_var = 1
            elif 1 < c[-1]:
                conf_var = 1
            if conf_var == 1:
                i = b.index(1)
                if len(c) == 0:
                    (one2[i]).place_forget()
                    one_3_4.place(x=640, y=263)
                    b.remove(1)
                    c.append(1)
                elif len(c) == 1:
                    (one2[i]).place_forget()
                    one_3_3.place(x=640, y=226)
                    b.remove(1)
                    c.append(1)
                elif len(c) == 2:
                    (one2[i]).place_forget()
                    one_3_2.place(x=640, y=189)
                    b.remove(1)
                    c.append(1)
                elif len(c) == 3:
                    (one2[i]).place_forget()
                    one_3_1.place(x=640, y=152)
                    b.remove(1)
                    c.append(1)
        elif b[-1] == 2:
            if len(c) == 0:
                conf_var = 1
            elif 2 < c[-1]:
                conf_var = 1
            if conf_var == 1:
                i = b.index(2)
                if len(c) == 0:
                    (two2[i]).place_forget()
                    two_3_4.place(x=620, y=263)
                    b.remove(2)
                    c.append(2)
                elif len(c) == 1:
                    (two2[i]).place_forget()
                    two_3_3.place(x=620, y=226)
                    b.remove(2)
                    c.append(2)
                elif len(c) == 2:
                    (two2[i]).place_forget()
                    two_3_2.place(x=620, y=189)
                    b.remove(2)
                    c.append(2)
        elif b[-1] == 3:
            if len(c) == 0:
                conf_var = 1
            elif 3 < c[-1]:
                conf_var = 1
            if conf_var == 1:
                i = b.index(3)
                if len(c) == 0:
                    (three2[i]).place_forget()
                    three_3_4.place(x=605, y=263)
                    b.remove(3)
                    c.append(3)
                elif len(c) == 1:
                    (three2[i]).place_forget()
                    three_3_3.place(x=605, y=226)
                    b.remove(3)
                    c.append(3)
        elif b[-1] == 4:
            if len(c) == 0:
                conf_var = 1
            elif 4 < c[-1]:
                conf_var = 1
            if conf_var == 1:
                i = b.index(4)
                if len(c) == 0:
                    (four2[i]).place_forget()
                    four_3_4.place(x=590, y=263)
                    b.remove(4)
                    c.append(4)
    if int(res[0]) == 3 and int(res[1]) == 1:
        if c[-1] == 1:
            if len(a) == 0:
                conf_var = 1
            elif 1 < a[-1]:
                conf_var = 1
            if conf_var == 1:
                i = c.index(1)
                if len(a) == 0:
                    (one3[i]).place_forget()
                    one_1_4.place(x=190, y=263)
                    c.remove(1)
                    a.append(1)
                elif len(a) == 1:
                    (one3[i]).place_forget()
                    one_1_3.place(x=190, y=226)
                    c.remove(1)
                    a.append(1)
                elif len(a) == 2:
                    (one3[i]).place_forget()
                    one_1_2.place(x=190, y=189)
                    c.remove(1)
                    a.append(1)
                elif len(a) == 3:
                    (one3[i]).place_forget()
                    one_1_1.place(x=190, y=152)
                    c.remove(1)
                    a.append(1)
        elif c[-1] == 2:
            if len(a) == 0:
                conf_var = 1
            elif 2 < a[-1]:
                conf_var = 1
            if conf_var == 1:
                i = c.index(2)
                if len(a) == 0:
                    (two3[i]).place_forget()
                    two_1_4.place(x=170, y=263)
                    c.remove(2)
                    a.append(2)
                elif len(a) == 1:
                    (two3[i]).place_forget()
                    two_1_3.place(x=170, y=226)
                    c.remove(2)
                    a.append(2)
                elif len(a) == 2:
                    (two3[i]).place_forget()
                    two_1_2.place(x=170, y=189)
                    c.remove(2)
                    a.append(2)
        elif c[-1] == 3:
            if len(a) == 0:
                conf_var = 1
            elif 3 < a[-1]:
                conf_var = 1
            if conf_var == 1:
                i = c.index(3)
                if len(a) == 0:
                    (three3[i]).place_forget()
                    three_1_4.place(x=155, y=263)
                    c.remove(3)
                    a.append(3)
                elif len(a) == 1:
                    (three3[i]).place_forget()
                    three_1_3.place(x=155, y=226)
                    c.remove(3)
                    a.append(3)
        elif c[-1] == 4:
            if len(a) == 0:
                conf_var = 1
            elif 4 < a[-1]:
                conf_var = 1
            if conf_var == 1:
                i = c.index(4)
                if len(a) == 0:
                    (four3[i]).place_forget()
                    four_1_4.place(x=140, y=263)
                    c.remove(4)
                    a.append(4)
    if int(res[0]) == 3 and int(res[1]) == 2:
        if c[-1] == 1:
            if len(b) == 0 :
                conf_var = 1
            elif 1 < b[-1] :
                conf_var = 1
            if conf_var == 1 :
                i = c.index(1)
                if len(b) == 0:
                    (one3[i]).place_forget()
                    one_2_4.place(x=420, y=263)
                    c.remove(1)
                    b.append(1)
                elif len(b) == 1:
                    (one3[i]).place_forget()
                    one_2_3.place(x=420, y=226)
                    c.remove(1)
                    b.append(1)
                elif len(b) == 2:
                    (one3[i]).place_forget()
                    one_2_2.place(x=420, y=189)
                    c.remove(1)
                    b.append(1)
                elif len(b) == 3:
                    (one3[i]).place_forget()
                    one_2_1.place(x=420, y=152)
                    c.remove(1)
                    b.append(1)
        elif c[-1] == 2:
            if len(b) == 0 :
                conf_var = 1
            elif 2 < b[-1] :
                conf_var = 1
            if conf_var == 1 :
                i = c.index(2)
                if len(b) == 0:
                    (two3[i]).place_forget()
                    two_2_4.place(x=400, y=263)
                    c.remove(2)
                    b.append(2)
                elif len(b) == 1:
                    (two3[i]).place_forget()
                    two_2_3.place(x=400, y=226)
                    c.remove(2)
                    b.append(2)
                elif len(b) == 2:
                    (two3[i]).place_forget()
                    two_2_2.place(x=400, y=189)
                    c.remove(2)
                    b.append(2)
        elif c[-1] == 3:
            if len(b) == 0:
                conf_var = 1
            elif 3 < b[-1]:
                conf_var = 1
            if conf_var == 1:
                i = c.index(3)
                if len(b) == 0:
                    (three3[i]).place_forget()
                    three_2_4.place(x=385, y=263)
                    c.remove(3)
                    b.append(3)
                elif len(b) == 1:
                    (three3[i]).place_forget()
                    three_2_3.place(x=385, y=226)
                    c.remove(3)
                    b.append(3)
        elif c[-1] == 4:
            if len(b) == 0 :
                conf_var = 1
            elif 4 < b[-1] :
                conf_var = 1
            if conf_var == 1 :
                i = c.index(4)
                if len(b) == 0:
                    (four3[i]).place_forget()
                    four_2_4.place(x=370, y=263)
                    c.remove(4)
                    b.append(4)

    if conf_var == 1 :          # here, it is checked if flag variable has changed
        global score            # if it is, then move must be valid and so count of 'score' variable increase
        score = score + 1
        scoreLabel.configure(text='Moves:' + str(score))  # this makes text (eg.Moves: 30) set in label

    if c == [4,3,2,1] :                                   # this checks if boxes in 3rd pole are arranged as
        if score == 15 :                                  # expected for a solution
            message = 'Your solution was optimal'         # if they are then a 'Result' messagebox appears and
        else :                                            # it says moves and say if solution was optimal or not
            message = 'Your solution was not optimal'
        messagebox.showinfo('Result',f'''Congratulations!!
Moves: {score}
{message}''')
        root.destroy()    # this closes application as game is completed

# this label shows current of moves,i.e. the text(eg. Moves: 30)
scoreLabel = Label(text ='Moves:' + str(score), font='Verdana 14 bold', bg = 'red', fg='yellow', width=10, height=2, borderwidth=3, relief = RIDGE)
scoreLabel.place(x=600, y=425)

# this will make 'How to Play' button visible and we can click it to see instructions window
instructions = Button(text ='How To Play', font='Verdana 14 bold', bg = 'yellow', fg='black', width=10, height=1, borderwidth=3, relief = RIDGE, command = help)
instructions.place(x=600,y=500)

# this creates Enter button which has 'clicked' command defined
# and on clicking everything written in input box is checked and applied if it is valid
enter_button = Button(text='Enter', bg ='Black', fg='white',font='Verdana 14 bold', height=1 ,width=10, command=clicked)
enter_button.place(x=240, y=425)

# this makes application stay as long as user do not close it and continue giving responses
root.mainloop()