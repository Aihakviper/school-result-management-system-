from tkinter import *
from PIL import Image,ImageTk
from course import course_class 
from student import student_class
class RMS:
    def __init__(self,root):
        self.root = root
        self.root.title("student result management system")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="black")
        #icons
        self.logo = Image.open("Image/logo.png")
        self.logo_dash = self.logo.resize((50,40))
        self.logo_dash = ImageTk.PhotoImage(self.logo_dash)
        
        #title
        title = Label(self.root,text="student management system",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="black",fg="yellow").place(x=0,y=0,relwidth=1,height=50)
        #menu
        m_frame = LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="black",fg="yellow")
        m_frame.place(x=10,y=70,width=1340,height=80)
        
        button_course = Button(m_frame,text="course",font=("goudy old style",15,"bold"),bg="black",fg="yellow",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        button_student = Button(m_frame,text="student",font=("goudy old style",15,"bold"),bg="black",fg="yellow",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)
        button_result = Button(m_frame,text="result",font=("goudy old style",15,"bold"),bg="black",fg="yellow",cursor="hand2").place(x=460,y=5,width=200,height=40)
        button_view = Button(m_frame,text="view student result",font=("goudy old style",15,"bold"),bg="black",fg="yellow",cursor="hand2").place(x=680,y=5,width=200,height=40)
        button_logout = Button(m_frame,text="log out",font=("goudy old style",15,"bold"),bg="black",fg="yellow",cursor="hand2").place(x=900,y=5,width=200,height=40)
        button_exit = Button(m_frame,text="exit",font=("goudy old style",15,"bold"),bg="black",fg="yellow",cursor="hand2").place(x=1120,y=5,width=200,height=40)
        #contet
        self.bg_img = Image.open("Image\pngtree-programmer-engineering-and-coding-png-image_4696387.png")
        self.bg_img  = self.bg_img.resize((829,350),Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        
        self.label_bg = Label(self.root,image=self.bg_img).place(x=400,y=189,width=920,height=350)
        
        #updated details
        self.label_course = Label(self.root,text="total courses\n[ 0 ]",font=("goudy old style",20),bd=20,relief=RIDGE,bg="black",fg="yellow")
        self.label_course.place(x=400,y=530,width=300,height=100)
        
        self.label_student = Label(self.root,text="total student\n[ 0 ]",font=("goudy old style",20),bd=20,relief=RIDGE,bg="black",fg="yellow")
        self.label_student.place(x=710,y=530,width=300,height=100)
        
        self.label_result = Label(self.root,text="total result\n[ 0 ]",font=("goudy old style",20),bd=20,relief=RIDGE,bg="black",fg="yellow")
        self.label_result.place(x=1020,y=530,width=300,height=100)
        #footer
        footer = Label(self.root,text="AIHAK-student management system\ncontact us for any technical issues: 08105978667",font=("goudy old style",12,),bg="#262626",fg="yellow").pack(side=BOTTOM,fill=X)
        
        
    def add_course(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = course_class(self.new_window)
        
    def add_student(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = student_class(self.new_window)
    
    
    
if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()