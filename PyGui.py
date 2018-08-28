from tkinter import *

# class MyFirstGUI:
#     def __init__(self, master):
#         self.master = master
#         master.title("A simple GUI")
#         master.geometry("360x300")
#
#         self.label = Label(master, text="This is our first GUI!", pady=10)
#         self.label.pack()
#
#         self.greet_button = Button(master, text="Greet", command=self.greet)
#         self.greet_button.pack()
#
#         self.close_button = Button(master, text="Close", command=master.quit)
#         self.close_button.pack()
#
#     def greet(self):
#         print("Greetings!")
#
# root = Tk()
# my_gui = MyFirstGUI(root)
# root.mainloop()

counter = 0


def counter_label(label):
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)
    count()


root = Tk()
root.title("Counting Seconds")
label = Label(root, fg="green")
label.pack()
counter_label(label)
button = Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()