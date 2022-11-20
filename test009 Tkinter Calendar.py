from tkinter import *
from tkcalendar import *
import datetime

root = Tk()
root.title('Calendar.com')
root.geometry("600x400")

today = datetime.date.today()
cal = Calendar(root)
cal.pack


def grab_date():
    my_label.config(text="Today's Date Is " + cal.get_date())


my_button = Button(root, text="Get Date", command=grab_date)
my_button.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()
