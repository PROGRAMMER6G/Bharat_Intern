import tkinter as tk
from tkinter import messagebox
from functools import partial

temp_Val = "Celsius"

def store_temp(set_temp):
    global temp_Val
    temp_Val = set_temp

def convert_temperature(inputn, result_entry):
    temp = inputn.get()
    
    if temp_Val == 'Celsius':
        
        f = float((float(temp) * 9 / 5) + 32)
        result_entry.delete(0, tk.END)  # Clear the Entry
        result_entry.insert(0, "%.1f Fahrenheit" % f)
        messagebox.showinfo("Temperature Converter",
                            "Successfully converted to Fahrenheit")
        
    if temp_Val == 'Fahrenheit':
        
        c = float((float(temp) - 32) * 5 / 9)
        result_entry.delete(0, tk.END)  # Clear the Entry
        result_entry.insert(0, "%.1f Celsius" % c)
        messagebox.showinfo("Temperature Converter",
                            "Successfully converted to Celsius")

root = tk.Tk()

root.geometry('465x150')

root.title('Temperature Converter')
root.configure(bg='#368BC1')
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)

inputNumber = tk.StringVar()
var = tk.StringVar()

input_label = tk.Label(root, font=21,text="Enter Temperature:",bg='#368BC1',fg='black')
input_entry = tk.Entry(root, textvariable=inputNumber,font=21,bg='#F1E5AC',bd=2)
input_label.grid(row=1)
input_entry.grid(row=1, column=1)

result_entry = tk.Entry(root,font=21,bd=2)
result_entry.grid(row=3, columnspan=4)

dropDownList = ["Celsius", "Fahrenheit"]
drop_down = tk.OptionMenu(root, var, *dropDownList,
                          command=store_temp)
var.set(dropDownList[0])
drop_down.grid(row=1, column=2)

convert_button = partial(convert_temperature, input_entry, result_entry)
result_button = tk.Button(root,font=18, text="Convert", command=convert_button,bg='light green')
result_button.grid(row=2,columnspan=6)

root.grid_rowconfigure(3, weight=2)

root.mainloop()