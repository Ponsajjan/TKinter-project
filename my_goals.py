import tkinter as tk
import os, random       
class Window(tk.Frame):
    
    def __init__(self, M_window = None):
        tk.Frame.__init__(self, M_window)
        self.M_window = M_window
        self.M_window.iconbitmap(os.path.join ('support', 'smallicon.png'))
        self.inside_M_window()

    def inside_M_window(self):
        self.M_window.title('My_Goals')
        self.M_window.protocol('WM_DELETE_WINDOW', self.closeapp)
        self.Quotes = ["Focus on being productive insterd of busy", "The secret of getting ahead is getting started", "Don't let perfect be enemy of good", "Old habits die hard",
                      "Seek disipline and find liberty", "(Daily consistency) = massive results", '“It’s not that I’m so smart, it’s just that I stay with problems longer.” -Albert Einstein',
                      "Start by doing what’s necessary; then do what’s possible; and suddenly you are doing the impossible", "Discipline is doing what needs to be done, even if you don’t want to",
                      "If you can’t handle stress, you won’t manage success", "Be stubborn about your goals and flexible about your methods", "If it doesn’t challenge you, it won’t change you",
                      "Don’t quit. You’re already in pain. You’re already hurt. Get a reward from it", "Doing what is comfortable is rarely profitable", "Nobody can go back and start a new beginning, but anyone can start today and make a new ending.",
                      "The Distance Between Your Dreams And Reality Is Call Action", "Let choices reflect hope, not fear", "What consumes mind control life", "Sort, Set in order, Shine, Standards, Sustain", "Choose for intended destination",
                      "Those who have cultivated the habit of persistence seem to enjoy insurance against failure", "Don't let fear and greed against yourself. That's the starting of ignorance", "It is your determination and persistence that will make you a successful person",
                      "Do not speak out of reaction but from clear thoughts","Between stimulus and response there is a space. in that space is our power to choose our response. in our response lies our growth and freedom",
                      "Success is not final; failure is not fatal: It is the courage to continue that counts.", " Harder I work, the more luck I seem to have.", "Success is walking from failure to failure with no loss of enthusiasm.",
                      "All progress takes place outside the comfort zone", "Don't let the fear of losing be greater than the excitement of winning","The only limit to our realization of tomorrow will be our doubts of today.",
                      "The way to get started is to quit talking and begin doing", "There are no secrets to success. It is the result of preparation, hard work, and learning from failure", "Success seems to be connected with action. Successful people keep moving. They make mistakes, but they don't quit",
                      "If you really want to do something, you'll find a way. If you don't, you'll find an excuse", "The difference between who you are and who you want to be is what you do", "In order to succeed, we must first believe that we can",
                      "Many of life's failures are people who did not realize how close they were to success when they gave up",  "The secret of success is to do the common thing uncommonly well", "The only place where success comes before work is in the dictionary",
                      "The harder you work for something, the greater you’ll feel when you achieve it",  "You Don’t Have To Be Great To Start, But You Have To Start To Be Great", "The path to success is to take massive, determined action",
                      "Never consider the possibility of failure; as long as you persist, you will be successful", "There are only two mistakes one can make along the road to truth; not going all the way, and not starting",
                      "Conquering any difficulty always gives one a secret joy, for it means pushing back a boundary-line and adding to one’s liberty", "Determination becomes obsession and then it becomes all that matters",
                      "Victory is the child of preparation and determination"]

        
            #LEFT
        self.Recordframe=tk.LabelFrame(self.M_window,text='Record',padx=1 ,pady=5)
        self.Recordframe.grid(column=0, rowspan=3, padx=5 ,pady=5)
        from tkinter import scrolledtext 
        self.Recordcontent= scrolledtext.ScrolledText(self.Recordframe,width=50,height=30,padx=10 ,pady=5, wrap=tk.WORD)
        self.Recordcontent.grid(column=0, row=0,padx=5 ,pady=1)
        with open(os.path.join ('support', 'goals.txt'),'r') as content:
            file_contents = content.read()
            content.close()
  
        self.Recordcontent.insert("1.0", file_contents)
        self.Recordcontent.see('end')

        self.Record_clicklabel=tk.Label(self.M_window, text='Right click to save', fg='blue')
        self.Record_edit = False
        
        self.Recordcontent.bind("<Enter>", self.Recordinfo)
        self.Recordcontent.bind("<Leave>", self.Recordinfo_)
        self.Recordcontent.bind("<Key>", self.edit_Recordcontent)
        self.Recordcontent.bind("<Double-Button-1>", self.rec_fullscreen)
        
            #RIGHT     
        self.Assign_frame= tk.LabelFrame(self.M_window, text='Assign',padx=142 ,pady=20)
        self.Assign_frame.grid(column=1, row=1, ipadx=1 ,ipady=5)

        self.Assigned_frame= tk.LabelFrame(self.M_window, padx=25 ,pady=15)
        self.Assigned_frame.grid(column=1, row=2, ipadx=1 ,ipady=10)
        
        self.label1=tk.Label(self.Assigned_frame)
        self.label1.grid(columnspan=3,row=1)

        self.txt1=scrolledtext.ScrolledText(self.Assigned_frame,width=50,height=5, wrap=tk.WORD)
        self.txt1.grid(columnspan=3,row=2)

        self.label2=tk.Label(self.Assigned_frame)
        self.label2.grid(columnspan=3,row=3)

        self.txt2=scrolledtext.ScrolledText(self.Assigned_frame,width=50,height=5, wrap=tk.WORD)
        self.txt2.grid(columnspan=3,row=4)

        self.label3=tk.Label(self.Assigned_frame)
        self.label3.grid(columnspan=3,row=5)

        self.forgetframe=tk.Frame(self.Assigned_frame)
        self.forgetframe.grid(columnspan=3, row=6)
        self.Deadline_frame=tk.Frame(self.forgetframe)
        
        from tkinter.ttk import Combobox
        import datetime
        self.Date_dl=Combobox(self.Deadline_frame,width=2)
        self.Date_dl['value']=('',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
                               21,22,23,24,25,26,27,28,29,30,31)
        self.Date_dl.current(int(datetime.datetime.now().strftime('%d')))
        self.Date_dl.grid(column=0,row=1)

        self.Month_dl=Combobox(self.Deadline_frame,width=10)
        self.Month_dl['value']=('','January','February','March','April','May','June',
                                'July','August','September','Octumber','November','December')
        self.Month_dl.current(int(datetime.datetime.now().strftime('%m')))
        self.Month_dl.grid(column=1,row=1)

        self.Year_dl=Combobox(self.Deadline_frame,width=4)
        self.Year_dl['value']=('',int(datetime.datetime.now().strftime('%Y')),
                               int(datetime.datetime.now().strftime('%Y'))+1,
                               int(datetime.datetime.now().strftime('%Y'))+2)
        self.Year_dl.current(1)
        self.Year_dl.grid(column=2,row=1)

        self.Setbutton=tk.Button(self.Assigned_frame, text='   Set   ',command=self.set_button)
        self.Setbutton.grid(column=2, row=7)

        self.initial=tk.IntVar()
        self.initial.set(1)
        
        Radiobutton_1=tk.Radiobutton(self.Assign_frame,text='Task',variable=self.initial,value=1, command=self.creat)
        Radiobutton_1.grid(column=0,row=1)
        Radiobutton_2=tk.Radiobutton(self.Assign_frame,text='Progress',variable=self.initial,value=2, command=self.creat)
        Radiobutton_2.grid(column=1,row=2)
        Radiobutton_3=tk.Radiobutton(self.Assign_frame,text='Report',variable=self.initial,value=3, command=self.creat)
        Radiobutton_3.grid(column=2,row=3)
        
    def set_button(self):
        import datetime
        if self.Record_edit == False:
            try:
                if self.txt1.get('1.0', 'end-1c') and self.txt2.get('1.0', 'end-1c'):
                    self.txtt=open(os.path.join ('support', 'goals.txt'),'a')      
                    self.txtt.write(datetime.datetime.now().strftime("\nDate: %d-%B-%Y(%A)")+'  ')
                    self.txtt.write(datetime.datetime.now().strftime("Time: %r")+'\n')
                    self.txtt.write('\n')
                    self.txtt.write(self.label1.cget('text')+'\n')
                    self.txtt.write(self.txt1.get('1.0', 'end-1c')+'\n')                
                    self.txtt.write('\n')
                    self.txtt.write(self.label2.cget('text')+'\n')
                    self.txtt.write(self.txt2.get('1.0', 'end-1c')+'\n')
                    if self.initial.get()==1:
                        self.txtt.write('\n')
                        self.txtt.write('=Dead line= \n')
                        self.txtt.write(self.Date_dl.get()+' ')
                        self.txtt.write(self.Month_dl.get()+' ')
                        self.txtt.write(self.Year_dl.get()+'\n')
                        self.txtt.write('----------------------------------------------Task\n ') 
                        self.txtt.close()
                        
                    elif self.initial.get()==3:
                        self.txtt.write('--------------------------------------------Report\n ') 
                        self.txtt.close()
                        
                    else:
                        self.txtt.write('--------------------------------------------------\n ') 
                        self.txtt.close()
                        
                else:
                    from tkinter import messagebox
                    messagebox.showinfo('hey..!!','Must enter both field')

            except TypeError:
                from tkinter import messagebox
                messagebox.showinfo('hey..!!','       Oops...  !!       ')
                   
            finally:
                if self.txt1.get('1.0', 'end-1c') and self.txt2.get('1.0', 'end-1c'): 
                    self.txt1.delete('1.0', 'end-1c')
                    self.txt2.delete('1.0', 'end-1c')
                    self.Recordcontent.delete('1.0', 'end-1c')
                    with open(os.path.join ('support', 'goals.txt'),'r') as content:
                        file_contents = content.read()
                        content.close()
                        self.Recordcontent.replace("1.0","end-1c",chars=file_contents)
                        self.Recordcontent.see('end')
                        if self.initial.get()==3:
                            from tkinter import messagebox
                            messagebox.showinfo('hey..!!',"Don't lose the momentum, set the next task")
                            self.initial.set(1)
                            self.creat()
                else:
                    pass
        else:
            self.save_record(self.Record_edit)

    def creat(self):
        if self.initial.get()==1:
            self.Assigned_frame.configure(text = 'Task')
            self.label1.configure(text='Task')
            self.label2.configure(text='Statergy')
            self.label3.configure(text='Dead line')
            self.Deadline_frame.grid(columnspan=3, row=6)
            
        if self.initial.get()==2:
            self.Assigned_frame.config(text = 'Progress')
            self.label1.config(text='Achived work')
            self.label2.config(text='Data source')
            self.label3.config(text='')
            self.Deadline_frame.grid_remove()
                      
        if self.initial.get()==3:
            self.Assigned_frame.configure(text = 'Report')
            self.label1.config(text='Task Planned')
            self.label2.config(text='Task Implemented')
            self.label3.config(text='')
            self.Deadline_frame.grid_forget()
            
    #Record        
    def Recordinfo(self, event):
        self.recordinfo = tk.Label(self.M_window, text= random.choice((self.Quotes)))
        self.recordinfo.grid(columnspan=2, row=3)

    def Recordinfo_(self, event):
        self.recordinfo.grid_forget()
                     
    def edit_Recordcontent(self, event): 
        self.Record_edit = True
        self.Record_clicklabel.grid(row=1, column=0)
        self.Recordcontent.bind("<Button-3>", self.right_click)
            
    def right_click(self, event):   
        self.Record_edit = False
        self.Record_clicklabel.grid_forget()
        edited_txt=open(os.path.join ('support', 'goals.txt'),'w')
        edited_txt.write(self.Recordcontent.get('1.0', 'end-1c'))
        edited_txt.close()
        
    def save_record(self, event): 
        self.Record_edit = False
        from tkinter import messagebox
        conform=messagebox.askyesno('hey Conform edit..!!',"Do you want to save changes made in 'Record'.. ?")
        if conform == True:
            self.Record_clicklabel.grid_forget()
            edited_txt=open(os.path.join ('support', 'goals.txt'),'w')
            edited_txt.write(self.Recordcontent.get('1.0', 'end-1c'))
            edited_txt.close()
            self.set_button()
            
        else:
            with open(os.path.join ('support', 'goals.txt'),'r') as content:
                self.Record_clicklabel.grid_forget()
                file_contents = content.read()
                self.Recordcontent.replace("1.0","end-1c",chars=file_contents)
                content.close()
                self.set_button()

    def closeapp(self):
        if self.Record_edit == True:
            from tkinter import messagebox
            close_conform=messagebox.askyesno('hey Conform edit..!!'," Some changes have been made in 'Record'   \n Are you sure you want to close this app.?")
            if close_conform == True:
                root.destroy()
            else:
                pass        
        else:
            root.destroy()
            
    #Record in newscreen 
    def rec_fullscreen(self, event):
        from tkinter import Toplevel, scrolledtext
        self.M_window.withdraw()
        self.rec_newscreen = Toplevel()
        self.rec_newscreen.title("Record")
        self.rec_newscreen.iconbitmap(os.path.join ('support', 'smallicon.png'))
        self.rec_newscreen.geometry("950x555")
        self.newscreencontent= scrolledtext.ScrolledText(self.rec_newscreen)
        self.newscreencontent.pack(expand=tk.TRUE, fill= tk.BOTH)
        self.newscreencontent.insert("1.0", self.Recordcontent.get('1.0', 'end-1c'))
        self.newscreencontent.bind("<Key>", self.editrec_fullscreen)
        self.rec_newscreen.protocol('WM_DELETE_WINDOW', self.close_recfullscreen)
        self.Record_clicklabel_1=tk.Label(self.rec_newscreen, text='Right click to save edit', fg='blue')
        if self.Record_edit == True:
            self.editrec_fullscreen(self.Record_edit)

    def editrec_fullscreen(self, event):
        self.Record_edit = True
        self.Record_clicklabel_1.pack()
        self.newscreencontent.bind("<Button-3>", self.right_clicknew)

    def right_clicknew(self, event):
        self.Record_edit = False
        self.Record_clicklabel_1.pack_forget()
        self.edited_newtxt=open(os.path.join ('support', 'goals.txt','w'))
        self.edited_newtxt.write(self.newscreencontent.get('1.0', 'end-1c'))
        self.edited_newtxt.close()
        
    def close_recfullscreen(self):
        self.M_window.deiconify()
        if self.Record_edit == False:
            with open(os.path.join ('support', 'goals.txt'),'r') as content:
                new_contents = content.read()
                self.Recordcontent.replace("1.0","end-1c",chars=new_contents)
                content.close()
                self.Record_clicklabel.grid_forget()
                self.rec_newscreen.destroy()
        else:
            self.record_newtxt = self.newscreencontent.get('1.0', 'end-1c')
            self.Recordcontent.replace("1.0","end-1c",chars=self.record_newtxt)
            self.edit_Recordcontent(self.Record_edit)
            self.rec_newscreen.destroy()
            
root= tk.Tk()
root.geometry("950x555+{0}+{1}".format(int(root.winfo_screenwidth()/2-475), int(root.winfo_screenheight()/2-330)))
root.resizable(0,0)
app=Window(root)
app.creat()
root.mainloop()
