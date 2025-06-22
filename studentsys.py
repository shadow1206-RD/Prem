from tkinter import *
from tkinter import ttk 
from tkinter import messagebox  


class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.frame1 = Frame(self.root, bd=5, width=1200,height=40,relief="groove",bg="YELLOW")
        self.frame1.pack()
        self.frame1.pack_propagate(False)

        self.title = Label(self.frame1, text="Student Management System", font=("arial", 20, "bold"), bg="YELLOW", fg="black")
        self.title.pack()

        self.frame2=Frame(self.root,bg="yellow",relief=GROOVE,bd=2,height=500,width=400)
        self.frame2.pack(side=LEFT,fill=Y)
        self.frame2.pack_propagate(False)

        self.id_var = IntVar()
        self.name_var = StringVar()
        self.age_var = IntVar()
        self.place_var = StringVar()
        self.phone_var = IntVar()


        self.id=Label(self.frame2,text="ID",font=("times new roman",16,"bold"),bg="yellow").place(x=10,y=10)
        self.entry_id=Entry(self.frame2,font=("times new roman",16,"bold"),bg="white",width=20,textvariable=self.id_var).place(x=170,y=10)
        self.id_var.set("")

        self.name=Label(self.frame2,text="Name",font=("times new roman",16,"bold"),bg="yellow").place(x=10,y=50)
        self.entry_name=Entry(self.frame2,font=("times new roman",16,"bold"),bg="white",width=20,textvariable=self.name_var).place(x=170,y=50)

        self.age=Label(self.frame2,text="Age",font=("times new roman",16,"bold"),bg="yellow").place(x=10,y=90)
        self.entry_age=Entry(self.frame2,font=("times new roman",16,"bold"),bg="white",width=20,textvariable=self.age_var).place(x=170,y=90)
        self.age_var.set("")

        self.place=Label(self.frame2,text="Place",font=("times new roman",16,"bold"),bg="yellow").place(x=10,y=130)
        self.entry_place=Entry(self.frame2,font=("times new roman",16,"bold"),bg="white",width=20,textvariable=self.place_var).place(x=170,y=130)

        self.phoneno=Label(self.frame2,text="Phone Number",font=("times new roman",16,"bold"),bg="yellow").place(x=10,y=170)
        self.entry_pho=Entry(self.frame2,font=("times new roman",16,"bold"),bg="white",width=20,textvariable=self.phone_var).place(x=170,y=170)
        self.phone_var.set("")


        def Add_tree():
            try: 
                id=self.id_var.get()
                name=self.name_var.get()
                age=self.age_var.get()
                place=self.place_var.get()
                phone=self.phone_var.get()
           
                if id=="" or name=="" or age=="" or place=="" or phone=="":
                    messagebox.showerror("Error","All fields are required") 
                else:
                    self.treeview.insert("", "end", values=(id, name, age, place, phone))
                    self.id_var.set("")
                    self.name_var.set("")
                    self.age_var.set("")
                    self.place_var.set("")
                    self.phone_var.set("")
                    messagebox.showinfo("Success", "Record added successfully")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
     

        def clear_fields():
            self.id_var.set("")
            self.name_var.set("")
            self.age_var.set("")
            self.place_var.set("") 
            self.phone_var.set("")
        

        def delete():
            try:
                selected=self.treeview.selection()[0]
                if not selected:
                    messagebox.showerror("Error", "Please select a record to delete")
                else:
                    self.treeview.delete(selected)
            except Exception as e   :
                pass
        

        def update():  
            try:
                select=self.treeview.selection()[0] 
                if not select:
                    messagebox.showerror("Error", "Please select a record to update")
                else:
                    id=self.id_var.get()
                    name=self.name_var.get()
                    age=self.age_var.get()
                    place=self.place_var.get()
                    phone=self.phone_var.get()

                    if id=="" or name=="" or age=="" or place=="" or phone=="":
                        messagebox.showerror("Error","All fields are required") 
                    else:
                        self.treeview.item(select, values=(id, name, age, place, phone))
                        self.id_var.set("")
                        self.name_var.set("")
                        self.age_var.set("")
                        self.place_var.set("")
                        self.phone_var.set("")
                        messagebox.showinfo("Success", "Record updated successfully")
            except Exception as e:
                messagebox.showerror("Error",f"An error occured:{e}")
                    

        self.Clear=Button(self.frame2,text="Clear",font=("times new roman",16,"bold"),bg="grey",fg="white",width=10,command=clear_fields).pack(fill=X,side=BOTTOM,pady=10)
        self.Delete=Button(self.frame2,text="Delete",font=("times new roman",16,"bold"),bg="red",fg="white",width=10,command=delete).pack(fill=X,side=BOTTOM,pady=10)
        self.Update=Button(self.frame2,text="Update",font=("times new roman",16,"bold"),bg="blue",fg="white",width=10,command=update).pack(fill=X,side=BOTTOM,pady=10)
        self.Add=Button(self.frame2,text="Add",font=("times new roman",16,"bold"),bg="green",fg="white",width=10,command=Add_tree).pack(fill=X,side=BOTTOM,pady=10)


        self.frame3=Frame(self.root,bg="yellow",relief=GROOVE,bd=5,height=500,width=1200)
        self.frame3.pack(side=RIGHT,fill=BOTH)
        self.frame3.pack_propagate(False)

        self.treeview=ttk.Treeview(self.frame3,columns=("ID","Name","Age","Place","Phone Number"),show="headings")
        self.treeview.pack(expand=True,fill=BOTH)
        self.treeview.heading("ID",text="ID")
        self.treeview.heading("Name",text="Name")
        self.treeview.heading("Age",text="Age")
        self.treeview.heading("Place",text="Place")
        self.treeview.heading("Phone Number",text="Phone Number")
        self.treeview.column("ID",width=100,anchor=CENTER)
        self.treeview.column("Name",width=200,anchor=CENTER)
        self.treeview.column("Age",width=100,anchor=CENTER)
        self.treeview.column("Place",width=200,anchor=CENTER)
        self.treeview.column("Phone Number",width=200,anchor=CENTER)


arc=Tk()
arc.title("Studennt management system ")
arc.geometry("1200x600")
arc.config(bg="black")
arc.resizable(False,False)

StudentManagementSystem(arc)

arc.mainloop()