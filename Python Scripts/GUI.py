from tkinter import *
from tkinter import messagebox
import main

root = Tk()
root.title("ATM")
root.geometry("700x600")
root.config(background="white")


def test_func(res):
    if len(res) == 16:
        access = main.run(int(res))
        if access == 1:
            createNewWindow()
        elif access == -1:
            messagebox.showinfo("Error", "Access Denied!")
        elif access == 2:
            messagebox.showinfo("Error", "Access Denied!")
        elif access == 3:
            None
    else:
        enterpin.delete(0, 'end')
        messagebox.showinfo("Error", "Enter 16-digit pin number")


def createNewWindow():
    root.destroy()
    top = Tk()
    top.geometry("700x600")
    top.title("ATM")
    top.config(background="white")

    def destroyNewWindow():
        top.destroy()

    labeltext = Label(top,
                      text="***** Bank", font=("Times", 24, "bold"), background="white")
    labeltext.pack(pady=(40, 10))

    canvas = Canvas(top)
    canvas.config(width=500, height=500, background="#d4d6d9")
    canvas.pack(side="left", padx=10, pady=30)

    buttonexit = Button(top,
                        text="              EXIT              ", background="#323c4d", foreground="white", bd=7, font=("Times", 10), command=destroyNewWindow)
    buttonexit.pack(side="bottom", pady=(10, 160))

    buttonpin = Button(top, text="      CHANGE PIN      ", background="#323c4d", foreground="white", bd=7, font=("Times", 10))
    buttonpin.pack(side="bottom", pady=(10, 30))

    buttonbalance = Button(top, text="  CHECK BALANCE  ", background="#323c4d", foreground="white", bd=7, font=("Times", 10))
    buttonbalance.pack(side="bottom", pady=(30, 30))

    buttonexit = Button(top, text="      WITHDRAW      ", background="#323c4d", foreground="white", bd=7, font=("Times", 10))
    buttonexit.pack(side="bottom", pady=10)

    top.mainloop()


labeltext = Label(root, text="***** Bank", font=("Times", 24, "bold"), background="white")
labeltext.pack(pady=(40, 20))

labelinstructions = Label(root, text="READ THE FOLLOWING INSTRUCTIONS CAREFULLY!", font=("Consolas", 18), justify="center", foreground="red", background="white")
labelinstructions.pack(pady=(20, 30))

labelrule0 = Label(root,
                   text="", background="#607596", width=100)
labelrule0.pack()

labelrules1 = Label(root, text="1. Only ONE person will operate the machine.", width=100,
                    font=("Times", 15), justify="center", bd=10,
                    background="#607596", foreground="white")
labelrules1.pack()

labelsrules2 = Label(root,
                     text="2. Before inserting the card remove SCARF, HELMET, MASK, etc if wearing any.", width=100, font=("Times", 15), justify="center", bd=10, background="#607596", foreground="white"
                     )
labelsrules2.pack()

labelrule3 = Label(root,
                   text="3. Make sure your face is clearly seen without any obstruction.", width=100, font=("Times", 15), justify="center", bd=10, background="#607596", foreground="white")
labelrule3.pack()


labelrule4 = Label(root,
                   text="4. After inserting the card stand properly facing the console.", width=100, font=("Times", 15), justify="center", bd=10, background="#607596",
                   foreground="white")
labelrule4.pack()


labelrule5 = Label(root,
                   text="", background="#607596", width=100)
labelrule5.pack()

labelpin = Label(root,
                 text="Enter your card number here :", font=("Times", 14), background="white", justify="center")
labelpin.pack(pady=(30, 5))


enterpin = Entry(root)
enterpin.pack()


buttonscan = Button(root, text='   INSERT CARD   ', bd=10, font=("Times", 12), command=lambda: test_func(enterpin.get())
                    )

buttonscan.pack(pady=30)

root.mainloop()
