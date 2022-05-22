from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

def miles_converter():
    conversion = float(input.get()) * 1.609
    result.config(text=conversion)

#Label
equal_to = Label(text="is equal to")
equal_to.grid(column=0, row=1)

#Input
input = Entry(width=10)
input.grid(column=1, row=0)

#Label(km)
result = Label(text=0)
result.grid(column=1, row=1)

#Calculate Button
calculate = Button(text="Calculate", command=miles_converter)
calculate.grid(column=1, row=2)

#Label Miles
miles = Label(text="Miles")
miles.grid(column=2, row=0)

#Label Km
km = Label(text="Km")
km.grid(column=2, row=1)

window.mainloop()