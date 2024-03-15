from tkinter import *
from tkinter import messagebox
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="upsidedown",
    database="App"
)

cursor = mydb.cursor()


class Register:
    def __init__(self):
        self.heading_font = ("Comic Sans MS", 30, "bold")
        self.text = ("Helvetica", 10)
        self.text_bold = ("Helvetica", 10, "bold")

        self.address = None
        self.email_id = None
        self.phone_number = None
        self.name = None

    def registration(self):
        root = Toplevel()
        root.title("Login Page")
        root.geometry("450x400")
        root.config(bg="light blue")

        label1 = Label(root, text="Registration Form", font=self.heading_font, bg="light blue")
        label2 = Label(root, text="ENTER NAME ", bg="light blue", font=self.text)
        label3 = Label(root, text="ENTER MOBILE NO.  ", bg="light blue", font=self.text)
        label4 = Label(root, text="ENTER EMAIL ID ", bg="light blue", font=self.text)
        label5 = Label(root, text="ADDRESS ", bg="light blue", font=self.text)
        Btn = Button(root, text="Register", bg="cyan", width=15, height=2, font=self.text_bold,
                     command=lambda: self.act(root), anchor="center")

        for i in range(2, 10, 2):
            Label(root, text=":", bg="light blue", font=self.text_bold).grid(row=i, column=1)

        label1.grid(row=0, column=0, columnspan=3)
        label2.grid(row=2, column=0, sticky=W)
        label3.grid(row=4, column=0, sticky=W)
        label4.grid(row=6, column=0, sticky=W)
        label5.grid(row=8, column=0, sticky=W)
        Btn.grid(row=10, column=2)

        root.rowconfigure(1, minsize=15)
        root.rowconfigure(3, minsize=15)
        root.rowconfigure(5, minsize=15)
        root.rowconfigure(7, minsize=15)
        root.rowconfigure(9, minsize=15)

        self.name = Entry(root, font=self.text, width=26)
        self.phone_number = Entry(root, font=self.text, width=26)
        self.email_id = Entry(root, font=self.text, width=26)
        self.address = Entry(root, font=self.text, width=26)

        self.name.grid(row=2, column=2, padx="20", pady="10", ipady="5", ipadx="40")
        self.phone_number.grid(row=4, column=2, padx="20", pady="10", ipady="5", ipadx="40")
        self.email_id.grid(row=6, column=2, padx="20", pady="10", ipady="5", ipadx="40")
        self.address.grid(row=8, column=2, padx="20", pady="10", ipady="5", ipadx="40")

        root.mainloop()

        # Details_page = details()
        # Details_page.details_page()


    def registration_given(self, contact_person):

        root = Toplevel()
        root.title("Login Page")
        root.geometry("450x400")
        root.config(bg="light blue")

        label1 = Label(root, text="Phone Book App", font=self.heading_font, bg="light blue")
        label2 = Label(root, text="ENTER NAME ", bg="light blue", font=self.text)
        label3 = Label(root, text="ENTER MOBILE NO.  ", bg="light blue", font=self.text)
        label4 = Label(root, text="ENTER EMAIL ID ", bg="light blue", font=self.text)
        label5 = Label(root, text="ADDRESS ", bg="light blue", font=self.text)
        Btn = Button(root, text="Register", bg="cyan", width=15, height=2, font=self.text_bold,
                     command=lambda: self.update(contact_person,root), anchor="center")

        for i in range(2, 10, 2):
            Label(root, text=":", bg="light blue", font=self.text_bold).grid(row=i, column=1)

        label1.grid(row=0, column=0, columnspan=3)
        label2.grid(row=2, column=0, sticky=W)
        label3.grid(row=4, column=0, sticky=W)
        label4.grid(row=6, column=0, sticky=W)
        label5.grid(row=8, column=0, sticky=W)
        Btn.grid(row=10, column=2)

        root.rowconfigure(1, minsize=15)
        root.rowconfigure(3, minsize=15)
        root.rowconfigure(5, minsize=15)
        root.rowconfigure(7, minsize=15)
        root.rowconfigure(9, minsize=15)

        self.name = Entry(root, font=self.text, width=26)
        self.phone_number = Entry(root, font=self.text, width=26)
        self.email_id = Entry(root, font=self.text, width=26)
        self.address = Entry(root, font=self.text, width=26)

        self.name.grid(row=2, column=2, padx="20", pady="10", ipady="5", ipadx="40")
        self.phone_number.grid(row=4, column=2, padx="20", pady="10", ipady="5", ipadx="40")
        self.email_id.grid(row=6, column=2, padx="20", pady="10", ipady="5", ipadx="40")
        self.address.grid(row=8, column=2, padx="20", pady="10", ipady="5", ipadx="40")

        self.name.insert(0,contact_person[0][1])
        self.phone_number.insert(0,contact_person[0][0])
        self.email_id.insert(0,contact_person[0][2])
        self.address.insert(0,contact_person[0][3])

        root.mainloop()
        root.destroy()

        # Details_page = details()
        # Details_page.details_page()


    def act(self,root):
        name = str(self.name.get())
        phone_number = int(self.phone_number.get())
        email_id = str(self.email_id.get())
        address = str(self.address.get())

        try:
            # cursor.execute(f"Use App;")
            cursor.execute("INSERT INTO People (phone_number, name, email_id, address) VALUES (%s, %s, %s, %s);",(phone_number, name, email_id, address))
            mydb.commit()
            root.destroy()
            self.registration_successful()
        except Exception as e:
            print(e)
            root.destroy()
            self.registration_unsuccessful()



    def update(self,contact_person,root):
        name = str(self.name.get())
        phone_number = int(self.phone_number.get())
        email_id = str(self.email_id.get())
        address = str(self.address.get())

        try:
            # cursor.execute(f"Use App;")
            cursor.execute("UPDATE People SET phone_number = %s,name =%s,email_id=%s, Address=%s  WHERE phone_number = %s",
                           (phone_number, name, email_id, address,contact_person[0][0]))
            mydb.commit()
            root.destroy()
            self.registration_successful()
        except Exception as e:
            print(e)
            root.destroy()
            messagebox.showerror("Info","Failed To Update !")

    def registration_successful(self):
        # Create a new Toplevel window
        messagebox.showinfo("Information", "Registration Successful !")

    def registration_unsuccessful(self):
        # Create a new Toplevel window
        messagebox.showinfo("Error", "Registration Unsuccessful !")


if __name__ == "__main__":
    obj = Register()
    obj.registration()
