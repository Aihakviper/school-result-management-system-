from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3

class student_class:

    def __init__(self,root):
        self.root = root
        self.root.title("student result management system")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="black")
        self.root.focus_force()

        #title
        title = Label(self.root,text="managing course details",font=("goudy old style",20,"bold"),bg="black",fg="yellow").place(x=10,y=15,width=1180,height=35)
        #variables
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()

        
        #widget
        label_course_name = Label(self.root,text="course name",font=("goudy old style",15,"bold"),bg="black",fg="yellow").place(x=10,y=60)
        label_duration = Label(self.root,text="duration",font=("goudy old style",15,"bold"),bg="black",fg="yellow").place(x=10,y=100)
        label_charges = Label(self.root,text="charges",font=("goudy old style",15,"bold"),bg="black",fg="yellow").place(x=10,y=140,)
        label_description = Label(self.root,text="description",font=("goudy old style",15,"bold"),bg="black",fg="yellow").place(x=10,y=180)
      
        #entry fields
        self.text_course_name = Entry(self.root,textvariable=self.var_course,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.text_course_name.place(x=150,y=60,width=200)
        text_duration = Entry(self.root,textvariable=self.var_duration,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=100,width=200)
        text_charges = Entry(self.root,textvariable=self.var_charges,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=140,width=200)
        self.text_description = Text(self.root,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.text_description.place(x=150,y=180,width=500,height=130)
      
        #buttons
        self.button_add = Button(self.root,text="save",font=("goudy old style",15,"bold"),bg="black",fg="yellow",cursor="hand2",command=self.add)
        self.button_add.place(x=150,y=400,width=110,height=40) 
        self.button_update = Button(self.root,text="update",font=("goudy old style",15,"bold"),bg="black",fg="yellow",cursor="hand2",command=self.update)
        self.button_update.place(x=270,y=400,width=110,height=40) 
        self.button_delete = Button(self.root,text="delete",font=("goudy old style",15,"bold"),bg="black",fg="yellow",cursor="hand2",command=self.delete)
        self.button_delete.place(x=390,y=400,width=110,height=40) 
        self.button_clear = Button(self.root,text="clear",font=("goudy old style",15,"bold"),bg="black",fg="yellow",cursor="hand2",command=self.clear)
        self.button_clear.place(x=510,y=400,width=110,height=40) 
        #search panel
        self.var_search = StringVar()
        search_course_name = Label(self.root,text="course name",font=("goudy old style",15,"bold"),bg="black",fg="yellow").place(x=720,y=60)
        text_search_course_name = Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=870,y=60,width=180)
        button_search = Button(self.root,text="search",font=("goudy old style",15,"bold"),bg="black",fg="yellow",cursor="hand2",command=self.search).place(x=1070,y=60,width=120,height=28)
        #content
        self.course_frame = Frame(self.root,bd=2,relief=RIDGE)
        self.course_frame.place(x=720,y=100,width=470,height=340)
        
        scroll_y = Scrollbar(self.course_frame,orient=VERTICAL)
        scroll_x= Scrollbar(self.course_frame,orient=HORIZONTAL)
        self.course_table = ttk.Treeview(self.course_frame,columns=("cid","name","duration","charges","description"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.course_table.xview)
        scroll_y.config(command=self.course_table.yview)
        self.course_table.heading("cid",text="Course ID")
        self.course_table.heading("name",text="Name")
        self.course_table.heading("duration",text="Duration")
        self.course_table.heading("charges",text="Charges")
        self.course_table.heading("description",text="Description")
        self.course_table["show"] = "headings"
        self.course_table.column("cid",width=100)
        self.course_table.column("name",width=100)
        self.course_table.column("duration",width=100)
        self.course_table.column("charges",width=100)
        self.course_table.column("description",width=150)
        self.course_table.pack(fill=BOTH,expand=1)
        self.course_table.bind("<ButtonRelease-1>",self.get_data)
        self.show()
 #=====================================
    def clear(self):
         self.show()
         self.var_course.set("")
         self.var_duration.set("")
         self.var_search.set("")
         self.var_charges.set("") 
         self.text_description.delete("1.0",END)
         self.text_course_name.config(state=NORMAL)
         
         
    def delete(self):
        connection = sqlite3.connect(database="school result management.db")
        cursor = connection.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error","course name should be required",parent=self.root)
            else:
                cursor.execute("select * from course where name=?",(self.var_course.get(),))
                row= cursor.fetchone()
                if row ==  None:
                    messagebox.showerror("Error","please select course from list",parent=self.root)
                else:
                    op = messagebox.askyesno("confirm","do you really want to delete?",parent=self.root)
                    if op== True:
                        cursor.execute("delete from course where name=?",(self.var_course.get(),))
                        connection.commit()
                        messagebox.showinfo("delete","course deleted succesfully",parent=self.root)
                        self.clear()
                        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        
        
        
    def get_data(self,ev):
        self.text_course_name.config(state="readonly")
        self.text_course_name
        r = self.course_table.focus()
        content = self.course_table.item(r)
        row =  content["values"]
        
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.text_description.delete("1.0",END)
        self.text_description.insert(END, row[4])
        
    def add(self):
        connection = sqlite3.connect(database="school result management.db")
        cursor = connection.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error","course name should be required",parent=self.root)
            else:
                cursor.execute("select * from course where name=?",(self.var_course.get(),))
                row= cursor.fetchone()
                if row !=  None:
                    messagebox.showerror("Error","course name already present",parent=self.root)
                else:
                    cursor.execute("insert into course (name,duration,charges,description) values(?,?,?,?)",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.text_description.get("1.0",END)
                    ))
                    connection.commit()
                    messagebox.showinfo("success","course added succesfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        
        
    def update(self):
        connection = sqlite3.connect(database="school result management.db")
        cursor = connection.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error","course name should be required",parent=self.root)
            else:
                cursor.execute("select * from course where name=?",(self.var_course.get(),))
                row= cursor.fetchone()
                if row ==  None:
                    messagebox.showerror("Error","select course from list",parent=self.root)
                else:
                    cursor.execute("update course set duration=?,charges=?,description=? where name=?",(
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.text_description.get("1.0",END),
                        self.var_course.get()
                    ))
                    connection.commit()
                    messagebox.showinfo("success","course updated succesfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        
        
    def show(self):
        connection = sqlite3.connect(database="school result management.db")
        cursor = connection.cursor()
        try:
            cursor.execute("select * from course")
            rows = cursor.fetchall()
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert("", END,values=row)         
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        
    def search(self):
        connection = sqlite3.connect(database="school result management.db")
        cursor = connection.cursor()
        try:
            cursor.execute(f"select * from course where name LIKE '%{self.var_search.get()}%'")
            rows = cursor.fetchall()
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert("", END,values=row)         
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        
           
if __name__ == "__main__":

    root = Tk()

    obj = student_class(root)

    root.mainloop()