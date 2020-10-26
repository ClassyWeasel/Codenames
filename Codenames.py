import pandas as pd
from tkinter import *
from tkinter import ttk
import random

pd.options.display.width = 0  # This is so that the outputs aren't truncated
df = pd.read_csv('codenames.csv')

# Functions for computing and displaying


# Function for choosing different words
word_array = ["" for x in range(25)]
blue_array = ["" for x in range(9)]
blue_count = 9
red_array = ["" for x in range(8)]
red_count = 8
bystander_array = ["" for x in range(7)]
bystander_count = 7
assassin = ""
reset_pressed = FALSE
def reset():
    # Global variables
    global word_array
    global reset_pressed
    global blue_array
    global blue_count
    global red_array
    global red_count
    global bystander_array
    global bystander_count
    global assassin

    rand_list = random.sample(range(0,len(df)), 25)
    rand_array = [None] * 25
    count = 0
    for x in rand_list:
        rand_array[count] = x
        count += 1
    for i in range(0,25):
        word_array[i] = df.iloc[rand_array[i],0]

    # Configure button text
    count = 0
    for j in range(1,6):
        for i in range(1,6):
            globals()['btn%s' % j + '_%s' % i] = Button(tab1, text= word_array[count], command = lambda idx = word_array[count], btn1 = j, btn2 = i: card_flipped(idx, btn1, btn2), height=4, width=13, font=("Arial", 15))
            globals()['btn%s' % j + '_%s' % i].grid(column=i-1, row=j-1)
            count += 1

    # Configure Spymaster grid
    count = 0
    for j in range(1, 6):
        for i in range(1, 6):
            globals()['bttn%s' % j + '_%s' % i] = Button(tab3, text=word_array[count], height=4, width=13, font=("Arial", 15))
            globals()['bttn%s' % j + '_%s' % i].grid(column=i - 1, row=j - 1)
            count += 1

    orig_array = [None] * 25
    for i in range(0,25):
        orig_array[i] = word_array[i]

    random.shuffle(word_array)
    # Fill blue and red word array, along with innocent bystanders and assassin
    for i in range(0,9):
        blue_array[i] = word_array[i]
        if i < 8:
            red_array[i] = word_array[i+9]
        if i < 7:
            bystander_array[i] = word_array[i+17]
        assassin = word_array[24]
    if reset_pressed:
        T_blue.config(text=blue_array)
        T_red.config(text=red_array)
        T_by.config(text=bystander_array)
        T_assassin.config(text=assassin)

    count = 0
    for j in range(1, 6):
        for i in range(1, 6):
            card_flipped2(orig_array[count], j, i)
            count += 1

    reset_pressed = TRUE
    blue_count = 9
    red_count = 8
    bystander_count = 7
    T1 = Text(tab1, height=3, width=33)
    T1.grid(column=5, row=0)
    T1.insert(END, f"Remaining Blue Cards: {blue_count}\nRemaining Red Cards: {red_count}\nRemaining Innocent Bystanders: {bystander_count}")


# Function for when a card is flipped over
def card_flipped(idx, j, i):
    # Global variables
    global blue_array
    global blue_count
    global red_array
    global red_count
    global bystander_array
    global bystander_count
    global assassin

    # If the card is blue...
    if idx in blue_array:
        blue_count = blue_count - 1
        globals()['btn%s' % j + '_%s' % i].config(bg="blue", fg="white", state="disabled")
    # If the card is red...
    if idx in red_array:
        red_count = red_count - 1
        globals()['btn%s' % j + '_%s' % i].config(bg="red", fg="white", state="disabled")
    # If the card is a bystander...
    if idx in bystander_array:
        bystander_count = bystander_count - 1
        globals()['btn%s' % j + '_%s' % i].config(bg="yellow", fg="black", state="disabled")
    if idx == assassin:
        globals()['btn%s' % j + '_%s' % i].config(bg="black", fg="white", state="disabled")
        for j in range(1, 6):
            for i in range(1, 6):
                globals()['btn%s' % j + '_%s' % i].config(state="disabled")

    T1 = Text(tab1, height=3, width=33)
    T1.grid(column=5, row=0)
    T1.insert(END, f"Remaining Blue Cards: {blue_count}\nRemaining Red Cards: {red_count}\nRemaining Innocent Bystanders: {bystander_count}")


# Function for displaying Spymaster grid
def card_flipped2(idx, j, i):
    # Global variables
    global blue_array
    global blue_count
    global red_array
    global red_count
    global bystander_array
    global bystander_count
    global assassin
    # If the card is blue...
    if idx in blue_array:
        globals()['bttn%s' % j + '_%s' % i].config(bg="blue", fg="white")
    # If the card is red...
    if idx in red_array:
        globals()['bttn%s' % j + '_%s' % i].config(bg="red", fg="white")
    # If the card is a bystander...
    if idx in bystander_array:
        globals()['bttn%s' % j + '_%s' % i].config(bg="yellow", fg="black")
    if idx == assassin:
        globals()['bttn%s' % j + '_%s' % i].config(bg="black", fg="white")




# Setup window
window = Tk()
window.title("Codenames!")
window.geometry('1100x602')

# All of our tabs are here
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Codenames board')
tab_control.add(tab2, text='Spymaster words')
tab_control.add(tab3, text='Spymaster grid')
tab_control.grid(column=1)
reset()

# Tab 1 - Codenames board

# Board is displayed within the reset() function

# Reset button:
reset_btn = Button(tab1, text="Reset board", height=5, width=10, command=reset)
reset_btn.grid(column=5, row=4)

# Number of remaining cards:
T1 = Text(tab1, height=3, width=33)
T1.grid(column=5, row=0)
T1.insert(END, f"Remaining Blue Cards: {blue_count}\nRemaining Red Cards: {red_count}\nRemaining Innocent Bystanders: {bystander_count}")


# Tab 2 - Spymaster words

# Blue words
Label1 = Label(tab2, text="Blue cards:", font=("Arial Bold", 25))
Label1.grid(column=0, row=0)
T_blue = Label(tab2, text=blue_array, font=("Arial", 20))
T_blue.grid(column=0, row=1)
# Red words
Label2 = Label(tab2, text="Red cards:", font=("Arial Bold", 25))
Label2.grid(column=0, row=2)
T_red = Label(tab2, text=red_array, font=("Arial", 20))
T_red.grid(column=0, row=3)
# Bystander words
Label3 = Label(tab2, text="Bystander cards:", font=("Arial Bold", 25))
Label3.grid(column=0, row=4)
T_by = Label(tab2, text=bystander_array, font=("Arial", 20))
T_by.grid(column=0, row=5)
# Assassin word
Label4 = Label(tab2, text="Assassin card:", font=("Arial Bold", 25))
Label4.grid(column=0, row=6)
T_assassin = Label(tab2, text=assassin, font=("Arial", 20), fg="red")
T_assassin.grid(column=0, row=7)

# Reset button:
reset_btn = Button(tab2, text="Reset board", height=5, width=10, command=reset)
reset_btn.grid(column=0, row=8)


window.mainloop()