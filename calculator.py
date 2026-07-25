import tkinter as tk
import winsound

window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")

display = tk.Entry(window, font=("Arial", 24), justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(value):
    winsound.Beep(1000, 100)
    display.insert(tk.END, value)

def calculate():
    winsound.Beep(1200, 150)
    expression = display.get()
    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def clear():
    winsound.Beep(600, 150)
    display.delete(0, tk.END)

def key_press(event):
    key = event.char
    if key in "0123456789+-*/.":
        display.insert(tk.END, key)
    elif key == "\r":
        calculate()

btn7 = tk.Button(window, text="7", font=("Arial", 18), command=lambda: button_click("7"))
btn7.grid(row=1, column=0)

btn8 = tk.Button(window, text="8", font=("Arial", 18), command=lambda: button_click("8"))
btn8.grid(row=1, column=1)

btn9 = tk.Button(window, text="9", font=("Arial", 18), command=lambda: button_click("9"))
btn9.grid(row=1, column=2)

btn_divide = tk.Button(window, text="/", font=("Arial", 18), command=lambda: button_click("/"))
btn_divide.grid(row=1, column=3)

btn4 = tk.Button(window, text="4", font=("Arial", 18), command=lambda: button_click("4"))
btn4.grid(row=2, column=0)

btn5 = tk.Button(window, text="5", font=("Arial", 18), command=lambda: button_click("5"))
btn5.grid(row=2, column=1)

btn6 = tk.Button(window, text="6", font=("Arial", 18), command=lambda: button_click("6"))
btn6.grid(row=2, column=2)

btn_multiply = tk.Button(window, text="*", font=("Arial", 18), command=lambda: button_click("*"))
btn_multiply.grid(row=2, column=3)

btn1 = tk.Button(window, text="1", font=("Arial", 18), command=lambda: button_click("1"))
btn1.grid(row=3, column=0)

btn2 = tk.Button(window, text="2", font=("Arial", 18), command=lambda: button_click("2"))
btn2.grid(row=3, column=1)

btn3 = tk.Button(window, text="3", font=("Arial", 18), command=lambda: button_click("3"))
btn3.grid(row=3, column=2)

btn_minus = tk.Button(window, text="-", font=("Arial", 18), command=lambda: button_click("-"))
btn_minus.grid(row=3, column=3)

btn0 = tk.Button(window, text="0", font=("Arial", 18), command=lambda: button_click("0"))
btn0.grid(row=4, column=0, columnspan=2)

btn_plus = tk.Button(window, text="+", font=("Arial", 18), command=lambda: button_click("+"))
btn_plus.grid(row=4, column=2)

btn_equals = tk.Button(window, text="=", font=("Arial", 18), command=calculate)
btn_equals.grid(row=4, column=3)

btn_decimal = tk.Button(window, text=".", font=("Arial", 18), command=lambda: button_click("."))
btn_decimal.grid(row=5, column=0)

btn_clear = tk.Button(window, text="C", font=("Arial", 18), command=clear)
btn_clear.grid(row=5, column=1, columnspan=3)

window.bind("<Key>", key_press)

window.mainloop()