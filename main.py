from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Gowebkit.com - Learn To Code")
root.iconbitmap("c:/gui/gowebkit.ico")
root.geometry("400x400")

conn = sqlite3.connect("address_book.db")
c = conn.cursor()

# c.execute("""CREATE TABLE addresses
#                     (
#                         first_name text,
#                         last_name text,
#                         address text,
#                         city text,
#                         state text,
#                         zipcode integer
#                     )
#                 """)

f_name = Entry()

conn.commit()
conn.close()

root.mainloop()