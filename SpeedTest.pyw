from tkinter import *
import random
import difflib
from datetime import datetime

root = Tk()
root.title('Typing Speed Tester')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.resizable(False, False)
root.configure(bg="#a9a0d2")  

entered = StringVar()
start_time = None  # Variable to store the start time

words = [
    'The quick brown fox jumps over the lazy dog, or so they say!',
    'Speed typing improves your accuracy and focus—let\'s see how fast!',
    'TypIng speed is a greAt sk!ll tO enh@nce, but only with practice.',
    'Let\'s mix numb3rs & symb0ls: 5, 10, 15, @, #, &, *; Typ3 faster!',
    'Debugging code can b3 challeng!ng, especially when errors lurk.',
    'A typist’s precision matters m0r3 than just raw sp33d—focus!',
    '123 + $peci@l characters = a t0ugh typing ch@llenge!',
    'Keep your eyes on the screen and type with lightning-fast accuracy!',
    'In 2023, developers learn AI, Blockchain, & Quantum Computing!',
    'F@st typ1ng under pressure? 99% accuracy or bust—don’t miss a beat!',
    'Challenges make us stronger; so d0 typing tests—are you ready?',
    'Acc3ss d3nied: Permission erro® 0X0000; What went wrong?',
    'Can you type: "This isn’t a challenge—it’s a typist’s dream!"',
    'JavaScript && Python code go hand-in-hand for full-stack mastery.',
    '5! * 4 + 6^2 / (3-1) tests your typ!ng, math & foc@us skills!'
]

word = "Ready Or Not ??"

def check():
    global entered
    global word
    global start_time

    if start_time is None:  # If typing hasn't started, don't calculate results
        return

    string = f"{entered.get()}"
    today2 = datetime.now()
    end = today2.strftime("%H:%M:%S")
    
    FMT = "%H:%M:%S"
    s_time = (datetime.strptime(end, FMT) - datetime.strptime(start_time, FMT)).total_seconds()

    try:
        speed = round(len(string.split()) * 60 / s_time, 2)
    except ZeroDivisionError:
        speed = 0

    if string == word:
        Msg1 = "Time= " + str(s_time) + ' seconds'
        Msg2 = " Accuracy= 100% "
        Msg3 = " Speed= " + str(speed) + ' wpm'
    else:
        accuracy = difflib.SequenceMatcher(None, word, string).ratio()
        accuracy = str(round(accuracy * 100, 2))
        Msg1 = "Time= " + str(s_time) + ' seconds'
        Msg2 = " Accuracy= " + accuracy + '%'
        Msg3 = " Speed= " + str(speed) + ' wpm'  # words per minute

    Label(root, font=('arial', 15, 'bold'), text=Msg1).grid(row=7, columnspan=3)
    Label(root, font=('arial', 15, 'bold'), text=Msg2).grid(row=8, columnspan=3)
    Label(root, font=('arial', 15, 'bold'), text=Msg3).grid(row=9, columnspan=3)

def play():
    global word
    global entered
    global start_time

    word = random.choice(words)
    label.config(text=word)
    
    Label(root, font=('arial', 15), text="Type here").place(relx=0.5, rely=0.6, anchor=CENTER)

    entered.set("")  # Clear previous text
    entry = Entry(root, textvariable=entered, font=('arial', 15), width=80)
    entry.place(relx=0.5, rely=0.7, anchor=CENTER)
    entry.bind("<KeyPress>", start_timer)  # Bind the start_timer function to the keypress event

    check_button.grid(row=6, columnspan=6)

def start_timer(event):
    global start_time
    if start_time is None:  # Start the timer only once
        today = datetime.now()
        start_time = today.strftime("%H:%M:%S")

label = Label(root, font=('arial', 20, 'bold'), text=word)
label.place(relx=0.5, rely=0.4, anchor=CENTER)

start_button = Button(root, text="Start Typing", command=play, bg="DodgerBlue2", fg="white", font=('arial', 14), width=20, height=2)
start_button.place(relx=0.5, rely=0.23, anchor=CENTER)

check_button = Button(root, text="Check", command=check, bg="DodgerBlue2", fg="white", font=('arial', 12))
check_button.grid(row=6, columnspan=6)

entry_bar = Entry(root, textvariable=entered, font=('arial', 15), width=80)
entry_bar.place(relx=0.5, rely=0.7, anchor=CENTER)

mainloop()
