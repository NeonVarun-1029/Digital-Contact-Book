from tkinter import *
                                                                
username = 'admin'

password = 'admin'

userInput = input("What is your username: ")

if userInput == username:
    a=input("Enter Password: ")   
    if a == password:
        print("Welcome!")
    else:
        print("That is the wrong password.")
else:
    print("That is the wrong username.")


root = Tk()
root.geometry('500x600')
root.config(bg = 'SlateGray3')
root.title('Digital ContactBook-161,163,167')
root.resizable(0,0)
contactlist = [
    ['1 NATIONAL EMERGENCY NUMBER',  '112' , '', '', '' ,''],
    ['2 POLICE',  '100','','','',''],
    ['3 FIRE',   '101','','','',''],
    ['4 AMBULANCE','102','','','',''],
    ['5 Disaster Management Service',   '108','','','',''],
    ['6 Women Helpline' , '1091','','','',''],
    ]

Name = StringVar()
Number = StringVar()
Email = StringVar()
Zipcode = StringVar()
City = StringVar()
State = StringVar()


frame = Frame(root)
frame.pack(side = RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=15)
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)



def Selected():
    return int(select.curselection()[0])
    
def AddContact():
    contactlist.append([Name.get(), Number.get(), Email.get(), Zipcode.get(), City.get(), State.get()])
    Select_set()

def EDIT():
    contactlist[Selected()] = [Name.get(), Number.get(), Email.get(), Zipcode.get(), City.get(), State.get()]
    Select_set()
    
def DELETE():
    del contactlist[Selected()]
    Select_set()
   
def VIEW():
    NAME, PHONE ,EMAIL ,ZIPCODE ,CITY ,STATE= contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)
    Email.set(EMAIL)
    Zipcode.set(ZIPCODE)
    City.set(CITY)
    State.set(STATE)


def EXIT():
    root.destroy()

def RESET():
    Name.set('')
    Number.set('')
    Email.set('')
    Zipcode.set('')
    City.set('')
    State.set('')

def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    for name,phone,email,zipcode,city,State in contactlist :
        select.insert (END, name)
Select_set()




Label(root, text = 'NAME:', font='arial 12 bold', bg = 'SlateGray3').place(x= 30, y=20)
Entry(root, textvariable = Name).place(x= 100, y=20)
Label(root, text = 'PHONE NO:', font='arial 12 bold',bg = 'SlateGray3').place(x= 30, y=60)
Entry(root, textvariable = Number).place(x= 150, y=60)
Label(root, text = 'EMAIL:', font='arial 12 bold',bg = 'SlateGray3').place(x= 30, y=100)
Entry(root, textvariable = Email).place(x= 110, y=100)
Label(root, text = 'Zipcode:', font='arial 12 bold',bg = 'SlateGray3').place(x= 30, y=140)
Entry(root, textvariable = Zipcode).place(x= 120, y=140)
Label(root, text = 'City:', font='arial 12 bold',bg = 'SlateGray3').place(x= 30, y=180)
Entry(root, textvariable = City).place(x= 80, y=180)
Label(root, text = 'State:', font='arial 12 bold',bg = 'SlateGray3').place(x= 30, y=220)
Entry(root, textvariable = State).place(x= 95, y=220)


Button(root,text=" ADD", font='arial 12 bold',bg='Green', command = AddContact).place(x= 50, y=280)
Button(root,text="VIEW", font='arial 12 bold',bg='Blue', command = VIEW).place(x= 50, y=330)
Button(root,text="EDIT", font='arial 12 bold',bg='Yellow',command = EDIT).place(x= 50, y=380)
Button(root,text="DELETE", font='arial 12 bold',bg='Red',command = DELETE).place(x= 50, y=430)
Button(root,text="RESET", font='arial 12 bold',bg='SlateGray4', command = RESET).place(x= 50, y=480)
Button(root,text="EXIT", font='arial 12 bold',bg='tomato', command = EXIT).place(x= 390, y=510)


root.mainloop()