from tkinter import * 

app = Tk()
app.geometry("430x540")
app.title("pycalc")

entry = Entry(app, font = ('Cantarell 20'))
entry.place(x=0, y=100, height=100, width=430) # height is below and width is horizontal


def press(num):
    entry.insert(100, num)
    return

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "ERROR")
    return

def clear():
    entry.delete(0, END)
    return

def back():
    entry.delete()





# Buttons 
b1 = Button(app, text = "1", font=('Cantarell 20'), command=lambda: press("1"))
b1.place(x = 5, y = 205, height=80, width=80)
b2 = Button(app, text = "2", font=('Cantarell 20'), command=lambda: press("2"))
b2.place(x = 90, y = 205, height=80, width=80)
b3 = Button(app, text = "3", font=('Cantarell 20'), command=lambda: press("3"))
b3.place(x = 175, y = 205, height=80, width=80)
b4 = Button(app, text = "4", font=('Cantarell 20'), command=lambda: press("4"))
b4.place(x = 260, y = 205, height=80, width=80)
b5 = Button(app, text = "5", font=('Cantarell 20'), command=lambda: press("5"))
b5.place(x = 345, y = 205, height=80, width=80)
b6 = Button(app, text = "6", font=('Cantarell 20'), command=lambda: press("6"))
b6.place(x = 5, y = 290, height=80, width=80)
b7 = Button(app, text = "7", font=('Cantarell 20'), command=lambda: press("7"))
b7.place(x = 90, y = 290, height=80, width=80)
b8 = Button(app, text = "8", font=('Cantarell 20'), command=lambda: press("8"))
b8.place(x = 175, y = 290, height=80, width=80)
b9 = Button(app, text = "9", font=('Cantarell 20'), command=lambda: press("9"))
b9.place(x = 260, y = 290, height=80, width=80)
b0 = Button(app, text = "0", font=('Cantarell 20'), command=lambda: press("0"))
b0.place(x = 260, y = 375, height=80, width=80)
b_plus = Button(app, text = "+", font=('Cantarell 20'), command=lambda: press("+"))
b_plus.place(x = 345, y = 290, height=165, width=80)
b_minus = Button(app, text = "-", font=('Cantarell 20'), command=lambda: press("-"))
b_minus.place(x = 5, y = 375, height=80, width=80)
b_product = Button(app, text = "x", font=('Cantarell 20'), command=lambda: press("*"))
b_product.place(x = 90, y = 375, height=80, width=80)
b_divide = Button(app, text = "/", font=('Cantarell 20'), command=lambda: press("/"))
b_divide.place(x = 175, y = 375, height=80, width=80)
b_clear = Button(app, text = "C", font=('Cantarell 20'), command=lambda: clear())
b_clear.place(x = 5, y = 460, height=80, width=80)
b_equal = Button(app, text = "=", font=('Cantarell 20'), command=lambda: equal())
b_equal.place(x = 245, y = 460, height=80, width=180)
b_back = Button(app, text = "B", font=('Cantarell 20'), command=lambda: back())
b_back.place(x = 90, y = 460, height=80, width=150)





app.mainloop()