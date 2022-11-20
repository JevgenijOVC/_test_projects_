from tkinter import *
import tkinter as tk
import pandas as pd

main = Tk()
main.title("Tikamoon Luce 01")
main.geometry('1800x600')


def buttonexit():
    quit()


buttonExit = tk.Button(text="Exit", command=buttonexit)
buttonExit.pack(side=BOTTOM, expand=NO, fill=BOTH)

main.mainloop()

ProductBom = pd.read_excel("TM01-00.000SB.xlsx")

print(ProductBom)
