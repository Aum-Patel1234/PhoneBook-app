from tkinter import *
from details import details
from registration import Register

details_obj = details()
register_obj = Register()

root = Tk()
root.geometry("380x320")
root.configure(bg="light blue")
text = ("Helvetica", 15)

# Setting padding between rows


# Setting padding between columns
root.rowconfigure(1,minsize=20)
root.rowconfigure(3,minsize=15)

root.columnconfigure(0,minsize=40)
root.columnconfigure(2,minsize=20)


# Title Label
Label(root, text="Phonebook App", font=("Comic Sans MS", 30, "bold"), bg="light blue").grid(row=0, column=1, columnspan=4)

# Buttons
Button(root, text="ADD", font=text, bg="light gray", width=12, height=3, anchor="center",command=lambda : details_obj.add()).grid(row=2, column=1)
Button(root, text="VIEW", font=text, bg="light gray", width=12, height=3, anchor="center",command=lambda : details_obj.details_page()).grid(row=2, column=3)
Button(root, text="UPDATE", font=text, bg="light gray", width=12, height=3, anchor="center",command=lambda : details_obj.get_person_page(True)).grid(row=4, column=1)
Button(root, text="DELETE", font=text, bg="light gray", width=12, height=3, anchor="center",command=lambda : details_obj.get_person_page(False)).grid(row=4, column=3)

root.mainloop()
