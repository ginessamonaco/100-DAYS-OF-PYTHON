import tkinter

window = tkinter.Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=300, height=150)
window.config(padx=30, pady=30)

def calculate():
    miles = float(input.get())
    km = round(miles * 1.609)
    number_label.config(text=km)
    
input = tkinter.Entry()
input.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles", font=("Courier", 10, "bold"))
miles_label.grid(column=2, row=0)

equal_to_label = tkinter.Label(text="is equal to", font=("Courier", 10, "bold"))
equal_to_label.grid(column=0, row=1)

number_label = tkinter.Label(text=0, font=("Courier", 10, "bold"))
number_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Kilometers", font=("Courier", 10, "bold"))
km_label.grid(column=2, row=1)

button = tkinter.Button(text="Calculate", font=("Courier", 10, "bold"), command=calculate)
button.grid(column=1, row=2)

window.mainloop()