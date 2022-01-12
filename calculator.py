import tkinter as tk
import math
import tkinter.messagebox


root = tk.Tk()
root.title("CalculatorApp")
root.configure(background="coral1")
root.resizable(width=False,height=False)
root.geometry("335x448+750+300")

calc = tk.Frame(root)
calc.grid()

root.history = True

ans = 0
var = ''
tocalc = tk.IntVar()
toshow = tk.IntVar()

def getValues():

    global ans
    global var
    v=tocalc.get()
    var= var+">"+str(v)
    ans += v
    tocalc.set(float(ans))
    toshow.set(var)

# CLASSES AND METHODS
 
class Calc:
    
    def __init__(self):
        
        self.total = 0
        self.current = ''
        self.ip_val = True
        self.check_sum = False
        self.op = ''
        self.result = False
        
    def numberEnter(self,num):
        self.result = False
        first_num = txtDisplay.get()
        second_num = str(num)

        if self.ip_val:
            self.current = second_num
            self.ip_val = False
        else:
            if second_num == '.':
                if second_num in first_num:
                    return
            self.current = first_num + second_num
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def valid_function(self):
        if self.op == '+':
            self.total += self.current
        elif self.op == '-':
            self.total -= self.current
        elif self.op == '*':
            self.total *= self.current
        elif self.op == '/':
            self.total /= self.current
        elif self.op == 'mod':
            self.total %= self.current

        self.ip_val = True
        self.check_sum = False
        self.display(self.total)

    def operation(self,op):    
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.ip_val = True
        self.check_sum = True
        self.op = op
        self.result = False

# MANIPULATION OF DISPLAY

    def display(self, value):
        txtDisplay.delete(0, tk.END)
        txtDisplay.insert(0, value)

    def clear_entry(self):
        self.result = False
        self.current = '0'
        self.display(0)
        self.ip_val = True

    def clear_all(self):
        self.clear_entry()
        self.total = 0
        
# FUNCTIONS FOR STANDARD CONSTANTS

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)
    
    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

# FUNCTIONS FOR CALCULATION

    def PM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def sq_rt(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def ln(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(txtDisplay.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    def radians(self):
        self.result = False
        self.current = math.radians(float(txtDisplay.get()))
        self.display(self.current)


res = Calc()

def History():

    getValues()

    top = tk.Toplevel()
    top.geometry("250x100+700+500")
    top.title("CalculatorApp - History")
    top.resizable(False,False)
    txtDisplay.delete(0, tk.END)
    txtDisplay.insert(0, "0")
    label1 = tk.Label(top, text="PREVIOUS RESULTS:", anchor=tk.CENTER)
    label1.pack()
    result_label = tk.Label(top, textvariable=toshow)
    result_label.place(y=30)
    top.transient(root)
    top.grab_set()
    root.wait_window(top)

# GRID BUILD


txtDisplay = tk.Entry(calc,font=('Terminal',20,'italic'),bd=30,bg='LightGoldenrod1',width=28,justify=tk.CENTER,textvariable=tocalc)
txtDisplay.pack()
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.bind("<Key>", lambda a: "break")

txtDisplay.event_add('<<commit1>>', '<KeyRelease-1>')
txtDisplay.bind("<<commit1>>",lambda e: res.numberEnter(1))
txtDisplay.event_add('<<commit2>>','<KeyRelease-2>')
txtDisplay.bind('<<commit2>>',lambda e: res.numberEnter(2))
txtDisplay.event_add('<<commit3>>','<KeyRelease-3>')
txtDisplay.bind('<<commit3>>',lambda e: res.numberEnter(3))
txtDisplay.event_add('<<commit4>>','<KeyRelease-4>')
txtDisplay.bind('<<commit4>>',lambda e: res.numberEnter(4))
txtDisplay.event_add('<<commit5>>','<KeyRelease-5>')
txtDisplay.bind('<<commit5>>',lambda e: res.numberEnter(5))
txtDisplay.event_add('<<commit6>>','<KeyRelease-6>')
txtDisplay.bind('<<commit6>>',lambda e: res.numberEnter(6))
txtDisplay.event_add('<<commit7>>','<KeyRelease-7>')
txtDisplay.bind('<<commit7>>',lambda e: res.numberEnter(7))
txtDisplay.event_add('<<commit8>>','<KeyRelease-8>')
txtDisplay.bind('<<commit8>>',lambda e: res.numberEnter(8))
txtDisplay.event_add('<<commit9>>','<KeyRelease-9>')
txtDisplay.bind('<<commit9>>',lambda e: res.numberEnter(9))
txtDisplay.event_add('<<commit0>>','<KeyRelease-0>')
txtDisplay.bind('<<commit0>>',lambda e: res.numberEnter(0))

txtDisplay.event_add('<<commit?>>','<KeyRelease-.>')
txtDisplay.bind('<<commit?>>',lambda e: res.numberEnter('.'))

txtDisplay.event_add('<<commitenter>>','<KeyRelease-Return>')
txtDisplay.bind('<<commitenter>>',lambda e: res.sum_of_total())




# NUMPAD - CODE

numpad = '789456123'
i=0
btn = []

for j in range(2,5):
    for k in range(3):
        btn.append(tk.Button(calc,width=6,height=2,font=('terminal',20,'italic'),bd=4,text=numpad[i],bg="azure"))
        btn[i].grid(row=j,column=k,pady=1)
        btn[i]['command'] = lambda x = numpad [i]:res.numberEnter(x)
        i+=1

# STANDARD CALCULATOR - CODE

tk.Button(calc,text=chr(67),width=6,height=2,font=('terminal',20,'italic'),bd=4,bg="azure",command = res.clear_entry).grid(row=1,column=0,pady=1)

tk.Button(calc,text=chr(67)+chr(69),width=6,height=2,font=('terminal',20,'italic'),bd=4,bg="azure",command = res.clear_all).grid(row=1,column=1,pady=1)

tk.Button(calc,text=u'\u221A',width=6,height=2,font=('terminal',20,'italic'),bd=4,bg="azure",command = res.sq_rt).grid(row=1,column=2,pady=1)

tk.Button(calc,text='ADD',width=6,height=2,font=('terminal',20,'italic'),bd=4,bg="medium sea green",command = lambda: res.operation('+')).grid(row=1,column=3,pady=1)

tk.Button(calc,text='SUB',width=6,height=2,font=('terminal',20,'italic'),bd=4,bg="firebrick1",command = lambda: res.operation('-')).grid(row=2,column=3,pady=1)

tk.Button(calc,text='MUL',width=6,height=2,font=('terminal',20,'italic'),bd=4,bg="MediumOrchid1",command = lambda: res.operation('*')).grid(row=3,column=3,pady=1)

tk.Button(calc,text='DIV',width=6,height=2,font=('terminal',20,'italic'),bd=4,bg="royal blue",command = lambda: res.operation('/')).grid(row=4,column=3,pady=1)

tk.Button(calc,text='=',width=6,height=2,font=('terminal',20,'italic'),bd=4,bg="azure",command = res.sum_of_total).grid(row=5,column=3,pady=1)

tk.Button(calc,text='.',width=6,height=2,font=('terminal',20,'italic'),bd=4,bg="azure",command = lambda: res.numberEnter('.')).grid(row=5,column=0,pady=1)

tk.Button(calc,text='0',width=6,height=2,font=('terminal',20),bd=4,bg="azure",command = lambda: res.numberEnter('0')).grid(row=5,column=1,pady=1)

tk.Button(calc,text=chr(177),width=6,height=2,font=('terminal',20,'italic'),bd=4,bg="azure",command = res.PM).grid(row=5,column=2,pady=1)

# SCIENTIFIC CALCULATOR - CODE

tk.Button(calc,text=u'\u03C0',width=6,height=2,font=('terminal',20,'italic'),bd=4,bg="azure",command = res.pi).grid(row=1,column=4,pady=1)

tk.Button(calc,text='sin',width=6,height=2,font=('terminal',20,'italic'),bd=4,bg="azure",command = res.sin).grid(row=2,column=4,pady=1)

tk.Button(calc,text='cos',width=6,height=2,font=('terminal',20,'italic'),bd=4,bg="azure",command = res.cos).grid(row=2,column=5,pady=1)

tk.Button(calc,text='tan',width=6,height=2,font=('terminal',20,'italic'),bd=4,bg="azure",command = res.tan).grid(row=2,column=6,pady=1)        

tk.Button(calc,text='LOG',width=6,height=2,font=('terminal',20,'italic'),bd=4,bg="azure",command = res.log).grid(row=4,column=4,pady=1)

tk.Button(calc,text='sinh',width=6,height=2,font=('terminal',20,'italic'),bd=4,bg="azure",command = res.sinh).grid(row=3,column=4,pady=1)

tk.Button(calc,text='cosh',width=6,height=2,font=('terminal',20,'italic'),bd=4,bg="azure",command = res.cosh).grid(row=3,column=5,pady=1)

tk.Button(calc,text='tanh',width=6,height=2,font=('terminal',20,'italic'),bd=4,bg="azure",command = res.tanh).grid(row=3,column=6,pady=1)

tk.Button(calc,text='ln',width=6,height=2,font=('terminal',20,'italic'),bd=4,bg="azure",command = res.ln).grid(row=4,column=5,pady=1)

tk.Button(calc,text='exp',width=6,height=2,font=('terminal',20,'italic'),bd=4,bg="azure",command = res.exp).grid(row=1,column=6,pady=1)

tk.Button(calc,text='mod',width=6,height=2,font=('terminal',20,'italic'),bd=4,bg="azure",command = lambda: res.operation('mod')).grid(row=5,column=6,pady=1)

tk.Button(calc,text='e',width=6,height=2,font=('terminal',20,'italic'),bd=4,bg="azure",command = res.e).grid(row=1,column=5,pady=1)

tk.Button(calc,text='log2',width=6,height=2,font=('terminal',20,'italic'),bd=4,bg="azure",command = res.log2).grid(row=4,column=6,pady=1)

tk.Button(calc,text='deg',width=6,height=2,font=('terminal',20,'italic'),bd=4,bg="azure",command = res.degrees).grid(row=5,column=4,pady=1)

tk.Button(calc,text='rad',width=6,height=2,font=('terminal',20,'italic'),bd=4,bg="azure",command = res.radians).grid(row=5,column=5,pady=1)

# MENUS

def Exit():
    if tkinter.messagebox.askyesno("CalculatorApp","Are you sure you want to exit?") > 0:
        root.destroy()
        return

def Sci():
    root.resizable(width=False,height=False)
    root.geometry("565x448+750+300")

def Std():
    root.resizable(width=False,height=False)
    root.geometry("335x448+750+300")

def new_window():
    tkinter.messagebox.showinfo("ABOUT","CREATED BY: AKASH SONLALL")

menubar = tk.Menu(calc)

file_menu = tk.Menu(menubar,tearoff=0)
another_menu = tk.Menu(menubar,tearoff=0)

menubar.add_cascade(label="FILE",menu=file_menu)
menubar.add_separator()

menubar.add_cascade(label="OPTIONS",menu=another_menu)
another_menu.add_command(label="PREVIOUS RESULT",command=History)
another_menu.add_command(label="ABOUT",command=new_window)

file_menu.add_command(label="STANDARD",command=Std)
file_menu.add_command(label="SCIENTIFIC",command=Sci)
file_menu.add_separator()
file_menu.add_command(label="EXIT",command=Exit)

root.config(menu=menubar)
root.mainloop()
