from tkinter import * 

app = Tk()
app.geometry("430x540")
app.title("pycalc")

entry = Entry(app, font = ('Cantarell 20')).place(x=0, y=100, height=100, width=430) # height is below and width is horizontal


# Buttons 
b1 = Button(app, text = "1", font=('Cantarell 20')).place(x = 5, y = 205, height=80, width=80)
b2 = Button(app, text = "2", font=('Cantarell 20')).place(x = 90, y = 205, height=80, width=80)
b3 = Button(app, text = "3", font=('Cantarell 20')).place(x = 175, y = 205, height=80, width=80)
b4 = Button(app, text = "4", font=('Cantarell 20')).place(x = 260, y = 205, height=80, width=80)
b5 = Button(app, text = "5", font=('Cantarell 20')).place(x = 345, y = 205, height=80, width=80)
b6 = Button(app, text = "6", font=('Cantarell 20')).place(x = 5, y = 290, height=80, width=80)
b7 = Button(app, text = "7", font=('Cantarell 20')).place(x = 90, y = 290, height=80, width=80)
b8 = Button(app, text = "8", font=('Cantarell 20')).place(x = 175, y = 290, height=80, width=80)
b9 = Button(app, text = "9", font=('Cantarell 20')).place(x = 260, y = 290, height=80, width=80)
b0 = Button(app, text = "0", font=('Cantarell 20')).place(x = 260, y = 375, height=80, width=80)
b_plus = Button(app, text = "+", font=('Cantarell 20')).place(x = 345, y = 290, height=165, width=80)
b_minus = Button(app, text = "-", font=('Cantarell 20')).place(x = 5, y = 375, height=80, width=80)
b_product = Button(app, text = "x", font=('Cantarell 20')).place(x = 90, y = 375, height=80, width=80)
b_divide = Button(app, text = "/", font=('Cantarell 20')).place(x = 175, y = 375, height=80, width=80)
b_clear = Button(app, text = "C", font=('Cantarell 20')).place(x = 5, y = 460, height=80, width=80)
b_equal = Button(app, text = "=", font=('Cantarell 20')).place(x = 245, y = 460, height=80, width=180)
b_back = Button(app, text = "B", font=('Cantarell 20')).place(x = 90, y = 460, height=80, width=150)





app.mainloop()