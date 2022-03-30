from tkinter import*
import math



root = Tk()
root.title ("lehavanya Calculator")
root.geometry("416x550+500+40")


calc =Frame (root, bd=20, pady=5, bg= "yellow", relief = RIDGE)
calc.grid()

class Calc ():
    def __init__ (self):
        self.total = 0
        self.current=""
        self.input_value = True
        self.check_sum = False
        self.op=""
        self.result= False
        
    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num) 
        if self.input_value:
             self.current = secondnum
             self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)


    def sum(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

            

    def display(self, value):
        txtDisplay.delete(0,END)
        txtDisplay.insert(0,value)


    def operation(self, op):

        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def valid_function(self):
        if self.op == "P":
            self.total += self.current
        if self.op == "M":
            self.total -= self.current
        if self.op == "Mult":
            self.total *= self.current
        if self.op == "Exp":
            self.total **= self.current
        if self.op == "Div":
            self.total /= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def all_Clear_Entry(self):
        self.Clear_Entry()
        self.total=0


    def Del(self):
        numLen = len(txtDisplay.get())
        txtDisplay.delete(numLen-1,'end')
        if numLen == 1:
            txtDisplay.insert(0,'0')

    def mathPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)


    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)
        
    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

        
        
added_value =Calc()

txtDisplay = Entry(calc, font = ('arial', 16, 'bold'), bd=28, width=28, justify =RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0,'0')


numberpad ="7894561230. "
i=0
btn = []
for j in range (3,7):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=('ariar', 16, 'bold'), bd=4, text=numberpad[i]))
        btn[i].grid (row=j,  column=k, pady=1)
        btn[i] ["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
        i+=1


btnDel = Button(calc, width=6, height=2, text = 'DEL', font=('ariar', 16, 'bold'), bd=4, bg='gainsboro',
                   command = added_value.Del).grid(row=1, column=0,  pady=1)
btnC = Button(calc, width=6, height=2, text = 'C', font=('ariar', 16, 'bold'), bd=4, bg='gainsboro',
                   command = added_value.all_Clear_Entry).grid(row=1, column=1,  pady=1)
btnCE = Button(calc, width=6, height=2, text = 'CE', font=('ariar', 16, 'bold'), bd=4, bg='gainsboro',
                   command = added_value.Clear_Entry).grid(row=1, column=2,  pady=1)
btnPM = Button(calc, width=6, height=2, text = '±', font=('ariar', 16, 'bold'), bd=4, bg='gainsboro',
                   command = added_value.mathPM).grid(row=1, column=3,  pady=1)


btnSq = Button(calc, width=6, height=2, text = '√', font=('ariar', 16, 'bold'), bd=4, bg='gainsboro',
                   command = added_value.squared).grid(row=2, column=0,  pady=1)
btnP = Button(calc, width=6, height=2, text = '+', font=('ariar', 16, 'bold'), bd=4, bg='gainsboro',
                   command = lambda: added_value.operation('P')).grid(row=2, column=3,  pady=1)
btnM = Button(calc, width=6, height=2, text = '-', font=('ariar', 16, 'bold'), bd=4, bg='gainsboro',
                   command = lambda: added_value.operation('M')).grid(row=3, column=3,  pady=1)
btnExponent = Button(calc, width=6, height=2, text = '^', font=('ariar', 16, 'bold'), bd=4, bg='gainsboro',
                   command = lambda: added_value.operation('Exp')).grid(row=4, column=3,  pady=1)
btnDiv = Button(calc, width=6, height=2, text = '/', font=('ariar', 16, 'bold'), bd=4, bg='gainsboro',
                   command = lambda: added_value.operation('Div')).grid(row=5, column=3,  pady=1)
btnMult = Button(calc, width=6, height=2, text = '*', font=('ariar', 16, 'bold'), bd=4, bg='gainsboro',
                   command = lambda: added_value.operation('Mult')).grid(row=6, column=3,  pady=1)


btnSin = Button(calc, width=6, height=2, text = 'Sin', font=('ariar', 16, 'bold'), bd=4, bg='gainsboro',
                   command = added_value.sin).grid(row=2, column=1,  pady=1)
btnCos = Button(calc, width=6, height=2, text = 'Cos', font=('ariar', 16, 'bold'), bd=4, bg='gainsboro',
                   command = added_value.cos).grid(row=2, column=2,  pady=1)

btnEquals = Button(calc, width=6, height=2, text = '=', font=('ariar', 16, 'bold'), bd=4, bg='gainsboro',
                  command = added_value.sum).grid(row=6, column=2,  pady=1)


root.mainloop ()
