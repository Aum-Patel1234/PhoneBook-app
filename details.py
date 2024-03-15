from tkinter import *
from tkinter import messagebox

import mysql.connector
from registration import Register

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="upsidedown",
    database="App"
)

cursor = mydb.cursor()

number = 0  # global for retrieving  from get_person_page number


class details():
    def __init__(self):
        self.f = ('Comic Sans MS', 30)
        self.f3 = ('Comic Sans MS', 20)
        self.f2 = ('Helvetica', 20)
        self.text = ('Helvetica', 15)
        self.text2 = ('Helvetica', 10)

    def details_page(self):
        root = Tk()
        root.iconbitmap("images//python_104451.ico")
        root.geometry('600x450')
        root.configure(bg='cyan')

        heading = Label(root, text='View Contacts', font=self.f, bg='cyan', fg='navy')
        heading.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Add a frame for viewing contacts
        contact_frame = Frame(root, bg='white', bd=2, relief='ridge')
        contact_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

        # Add a scrollable text area to display contacts
        contacts_text = Text(contact_frame, wrap='word', height=15, width=30, font=('Helvetica', 12))
        contacts_text.pack(side='left', fill='both', expand=True)

        # Add a scrollbar for the text area
        scrollbar = Scrollbar(contact_frame, command=contacts_text.yview)
        scrollbar.pack(side='right', fill='y')
        contacts_text.config(yscrollcommand=scrollbar.set)

        # Example contacts
        cursor.execute("SELECT * FROM People;")

        contacts = cursor.fetchall()
        # print(contacts)

        for contact in contacts:
            contacts_text.insert('end',str(contact)+'\n')

        # Add an Exit button
        exit_button = Button(root, text="Exit", command=root.destroy, width=10, height=2, bg='#FF0000')
        exit_button.grid(row=4, column=1, sticky=W)

        # Ensure resizing behavior
        root.rowconfigure(1, weight=1)
        root.columnconfigure(0, weight=1)

        root.mainloop()

    def details_of_specific_person(self, left, person):
        phone_number = person[0]
        # print(phone_number)

        self.details(phone_number)

    def details(self, phone_number):
        top = Toplevel()
        top.title('Person Name')
        top.geometry('440x300')
        # top.rowconfigure(2, minsize=15)
        top.rowconfigure(4, minsize=15)
        top.rowconfigure(6, minsize=15)
        top.rowconfigure(8, minsize=15)
        top.configure(bg='light gray')  # Changed background color

        content = cursor.execute(f"SELECT * FROM People WHERE phone_number =  {phone_number}")
        content = cursor.fetchall()

        # print(content[0][0])
        Label(top, text='Details of ' + content[0][1], font=self.f3, padx=10, pady=10, anchor="center",
              bg='light gray').grid(row=0, column=0, columnspan=4)  # Adjusted column span and sticky

        Label(top, text='Name', font=self.text, bg='light gray').grid(row=2, column=0, sticky=W)
        Label(top, text='Contact no.', font=self.text, bg='light gray').grid(row=4, column=0, sticky=W)
        Label(top, text='Email id', font=self.text, bg='light gray').grid(row=6, column=0, sticky=W)
        Label(top, text='City', font=self.text, bg='light gray').grid(row=8, column=0, sticky=W)

        for i in range(2, 9, 2):
            Label(top, text=":", pady=5, padx=5, bg='light gray', font=self.text).grid(row=i, column=1)

        Label(top, text="-----------------------------------------------------------------------------------------",
              bg='light gray').grid(row=1, column=0, columnspan=3)
        Label(top, text=content[0][1], font=self.text, bg='light gray').grid(row=2, column=2, sticky=W)
        Label(top, text=content[0][0], font=self.text, bg='light gray').grid(row=4, column=2, sticky=W)
        Label(top, text=content[0][2], font=self.text, bg='light gray').grid(row=6, column=2, sticky=W)
        Label(top, text=content[0][3], font=self.text, bg='light gray').grid(row=8, column=2, sticky=W)

    def add(self):
        obj = Register()
        obj.registration()

    def update(self, phone_number):
        print(phone_number)

        # Check if the phone number is valid
        if not phone_number.isdigit():
            messagebox.showerror("Error", "Invalid phone number")
            return

        cursor.execute("SELECT * FROM People WHERE People.phone_number = %s", (phone_number,))
        contact_person = cursor.fetchall()
        mydb.commit()

        if not contact_person:
            messagebox.showerror("Error", "Contact not found")
            return

        print(contact_person)

        obj = Register()
        obj.registration_given(contact_person)

    def delete(self, phone_number, root):
        # print(phone_number)
        try:
            cursor.execute("DELETE FROM People WHERE phone_number = %s;", (phone_number,))
            messagebox.showinfo("Info", "Deletion Successful !")
            mydb.commit()  # very important
            root.destroy()
        except Exception as e:
            print(e)
            root.destroy()
            messagebox.showerror("Error", "Deletion Failed !")

    def get_person_page(self, flag):
        top = Toplevel()
        top.configure(bg="light blue")
        top.geometry("360x150")

        heading_font = ("Comic Sans MS", 20)
        text_font = ("Helvetica", 12)
        top.rowconfigure(1, minsize=15)
        top.rowconfigure(3, minsize=15)

        Label(top, text="Information", font=heading_font, bg='light blue').grid(row=0, column=0, columnspan=3)
        Label(top, text="Enter Phone Number", font=text_font, bg='light blue').grid(row=2, column=0)
        Label(top, text=":", font=text_font, bg='light blue').grid(row=2, column=1)
        num = Entry(top, width=20, font=text_font)
        num.grid(row=2, column=2)

        def on_enter():
            global number
            number = num.get()
            # print("Entered phone number:", number)
            top.destroy()
            if flag:
                self.update(number)
            else:
                self.delete(int(number), top)

        Button(top, text="Enter", font=text_font, padx=10, pady=5, command=on_enter).grid(row=4, column=2, sticky='e')

        top.mainloop()


if __name__ == "__main__":
    obj = details()
    obj.details_page()
