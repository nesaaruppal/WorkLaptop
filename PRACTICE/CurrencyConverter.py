from tkinter import Tk, Text, END, Button, END, messagebox
from exchange_rates import get_rates

tk_instance = Tk()
tk_instance.title("Currency Converter")

text_area = Text(tk_instance, font=("sans-serif", 16))
text_area.pack()


def convert_currency():
    from_currency = from_currency_entry.get()
    to_currency = to_currency_entry.get()
    amount = float(amount_entry.get())
    rates = get_rates()
    converted_amount = amount * rates[to_currency] / rates[from_currency]
    output_text = f"{amount} {from_currency} is equal to {converted_amount} {to_currency}"
    text_area.insert(END, output_text + "\n")


from_currency_label = Label(tk_instance, text="From Currency: ")
from_currency_label.pack()
from_currency_entry = Entry(tk_instance)
from_currency_entry.pack()

to_currency_label = Label(tk_instance, text="To Currency: ")
to_currency_label.pack()
to_currency_entry = Entry(tk_instance)
to_currency_entry.pack()

amount_label = Label(tk_instance, text="Amount: ")
amount_label.pack()
amount_entry = Entry(tk_instance)
amount_entry.pack()

button = Button(tk_instance, text="Convert", command=convert_currency)
button.pack()

tk_instance.mainloop()
