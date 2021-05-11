from tkinter import *

window = Tk()
window.title("Miles to Km converter")
window.config(padx=20, pady=20)


def calculate():
    distance_km = float(input.get())
    distance_miles = round(distance_km * 1.609)
    result_label.config(text=f"{distance_miles}")


# label
label = Label(text="is equal to", font=("Arial", 18, "normal"))
label.grid(column=0, row=1)

# input entry
input = Entry(width=20)
input.grid(column=1, row=0)

# result label
result_label = Label(text=0, font=("Arial", 18, "normal"))
result_label.grid(column=1, row=1)

# button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

# miles label
miles_label = Label(text="Miles", font=("Arial", 18, "normal"))
miles_label.grid(column=2, row=0)

# Km label
km_label = Label(text="Km", font=("Arial", 18, "normal"))
km_label.grid(column=2, row=1)

window.mainloop()