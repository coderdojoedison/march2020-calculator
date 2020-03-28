from tkinter import *


expression = " "
def press(num):
  global expression
  expression = expression +str(num)
  equation.set(expression)

def equalpress():
  try:
    global expression
    total = str(eval(expression))
    equation.set(total)
    expression = " "
  except:
    equation.set("error")
    expression = ""
def clear():
  global expression
  expression = ""
  equation.set("")

if __name__ == "__main__":
  gui = Tk()
  gui.configure(background="white")
  gui.title("Calculator")
  gui.geometry("420x300")
  equation = StringVar()
  expression_field = Entry(gui, textvariable=equation)
  expression_field.grid(columnspan=5, ipadx = 70)
  equation.set('Enter your expression')
  button1 = Button(gui, text=' 1 ', fg='grey', bg='black',
                   command=lambda: press(1), height=4, width=7)
  button1.grid(row=2, column=0)
  button2 = Button(gui, text=' 2 ', fg='grey', bg='black',
                    command=lambda: press(2), height=4, width=7)
  button2.grid(row=2, column=1)
  button3 = Button(gui, text=' 3 ', fg='grey', bg='black',
                    command=lambda: press(3), height=4, width=7)
  button3.grid(row=2, column=2)
  button4 = Button(gui, text=' 4 ', fg='grey', bg='black',
                    command=lambda: press(4), height=4, width=7)
  button4.grid(row=3, column=0)
  button5 = Button(gui, text=' 5 ', fg='grey', bg='black',
                    command=lambda: press(5), height=4, width=7)
  button5.grid(row=3, column=1)
  button6 = Button(gui, text=' 6 ', fg='grey', bg='black',
                    command=lambda: press(6), height=4, width=7)
  button6.grid(row=3, column=2)
  button7 = Button(gui, text=' 7 ', fg='grey', bg='black',
                   command=lambda: press(7), height=4, width=7)
  button7.grid(row=4, column=0)
  button8 = Button(gui, text=' 8 ', fg='grey', bg='black',
                    command=lambda: press(8), height=4, width=7)
  button8.grid(row=4, column=1)
  button9 = Button(gui, text=' 9 ', fg='grey', bg='black',
                    command=lambda: press(9), height=4, width=7)
  button9.grid(row=4, column=2)
  button0 = Button(gui, text=' 0 ', fg='grey', bg='black',
                    command=lambda: press(0), height=4, width=7)
  button0.grid(row=5, column=0)
  buttonplus = Button(gui, text=' + ', fg='grey', bg='black',
                    command=lambda: press("+"), height=4, width=7)
  buttonplus.grid(row=2, column=3)
  buttonminus = Button(gui, text=' - ', fg='grey', bg='black',
                    command=lambda: press("-"), height=4, width=7)
  buttonminus.grid(row=3, column=3)
  buttonmultiply = Button(gui, text=' * ', fg='grey', bg='black',
                    command=lambda: press("*"), height=4, width=7)
  buttonmultiply.grid(row=4, column=3)
  buttondivide = Button(gui, text=' / ', fg='grey', bg='black',
                    command=lambda: press("/"), height=4, width=7)
  buttondivide.grid(row=5, column=3)
  buttonpower = Button(gui, text = "^", fg = 'grey', bg = 'black',
                       command=lambda: press("**"), height=4, width =7)
  buttonpower.grid(row=5, column=4)
  buttonsqrt = Button(gui, text = "sqrt", fg = 'grey', bg = 'black',
                       command=lambda: press("**(1/2)"), height=4, width =7)
  buttonsqrt.grid(row=4, column=4)
  buttonparenth = Button(gui, text=' ( ', fg='grey', bg='black',
                    command=lambda: press("("), height=4, width=7)
  buttonparenth.grid(row=3, column=4)
  buttoncparenth = Button(gui, text=' ) ', fg='grey', bg='black',
                    command=lambda: press(")"), height=4, width=7)
  buttoncparenth.grid(row=2, column=4)
  buttonequal = Button(gui, text=' = ', fg='grey', bg='black',
                    command=equalpress, height=4, width=7)
  buttonequal.grid(row=5, column=2)
  buttonclear = Button(gui, text=' clear ', fg='grey', bg='black',
                    command=clear, height=4, width=7)
  buttonclear.grid(row=5, column=1)

gui.mainloop()
