from tkinter import *

# Configure
calc = Tk()
calc.title('Calculator')
calc.geometry('371x185+500+400')
calc.resizable(0, 0)
calc.configure(bg='old lace')
# Display
entrybox = Entry(calc, width=40, bg='powder blue',
                 fg='black', borderwidth=10)
entrybox.grid(column=0, row=0, columnspan=5, padx=5, pady=5)
# Pick focus
entrybox.focus()


# Defined functions
# Clear display window
def clear():
    entrybox.delete(0, END)


# What happens when the button is pressed
def equal():
    val = entrybox.get()
    entrybox.delete(0, END)
    # Delete first and last element if it´s ban_element
    f_ban_elements = ['+', '*', '/']
    l_ban_elements = ['+', '-', '*', '/']
    for n in range(0, len(f_ban_elements)):
        if val[0] == f_ban_elements[n]:
            entrybox.delete(0, END)
            entrybox.insert(0, val[1::])
        if val[-1] == l_ban_elements[n]:
            entrybox.delete(0, END)
            entrybox.insert(0, val[0:-1])

    # Addition numbers
    for ma in val:
        if ma == '+':
            val_split = val.split('+')
            for ia in range(0, len(val_split)):
                val_split[ia] = int(val_split[ia])
            entrybox.insert(0, sum(val_split))
            break
    # Subtraction numbers
    for mS in val:
        if mS == '-':
            val_split = val.split('-')
            for iS in range(0, len(val_split)):
                val_split[iS] = int(val_split[iS])
            entrybox.insert(0, val_split[0] - sum(val_split[1::]))
            break
    # Multiplication numbers
    for mm in val:
        if mm == '*':
            val_split = val.split('*')
            for im in range(0, len(val_split)):
                val_split[im] = int(val_split[im])
            result = 1
            for x in val_split:
                result = result * x
            entrybox.insert(0, result)
            return result
    # Division numbers
    for md in val:
        if md == '/':
            val_split = val.split('/')
            for id in range(0, len(val_split)):
                val_split[id] = int(val_split[id])
            result = val_split[0]
            for x in val_split[1::]:
                result = result / x
            entrybox.insert(0, result)
            return result


# Add new element
def add_element(number):
    current_add = entrybox.get()
    entrybox.delete(0, END)
    entrybox.insert(0, str(current_add) + str(number))


# Delete last element
def button_del():
    current_del = entrybox.get()
    entrybox.delete(0, END)
    entrybox.insert(0, current_del[0:-1])


# Square of the element
def square():
    val = entrybox.get()
    entrybox.delete(0, END)
    # Delete first and last element if it´s ban_element
    ban_elements = ['+', '-', '*', '/']
    for nq in range(0, len(ban_elements)):
        if val[0] == ban_elements[nq]:
            entrybox.delete(0, END)
            entrybox.insert(0, val[1::])
    for nq in range(0, len(ban_elements)):
        if val[-1] == ban_elements[nq]:
            entrybox.delete(0, END)
            entrybox.insert(0, val[0:-1])

    square_val = int(val) * int(val)
    entrybox.insert(0, square_val)


# Define Buttons
button_1 = Button(calc, text='1', padx=34, pady=5, command=lambda: add_element(1))
button_2 = Button(calc, text='2', padx=35, pady=5, command=lambda: add_element(2))
button_3 = Button(calc, text='3', padx=35, pady=5, command=lambda: add_element(3))
button_4 = Button(calc, text='4', padx=34, pady=5, command=lambda: add_element(4))
button_5 = Button(calc, text='5', padx=35, pady=5, command=lambda: add_element(5))
button_6 = Button(calc, text='6', padx=35, pady=5, command=lambda: add_element(6))
button_7 = Button(calc, text='7', padx=34, pady=5, command=lambda: add_element(7))
button_8 = Button(calc, text='8', padx=35, pady=5, command=lambda: add_element(8))
button_9 = Button(calc, text='9', padx=35, pady=5, command=lambda: add_element(9))
button_0 = Button(calc, text='0', padx=34, pady=5, command=lambda: add_element(0))
button_plus = Button(calc, text='+', padx=20, pady=5, command=lambda: add_element('+'))
button_minus = Button(calc, text='-', padx=22, pady=5, command=lambda: add_element('-'))
button_multiply = Button(calc, text='*', padx=22, pady=5, command=lambda: add_element('*'))
button_division = Button(calc, text='/', padx=22, pady=5, command=lambda: add_element('/'))
button_square = Button(calc, text='^2', padx=17, pady=5, command=square)
button_equal = Button(calc, text='=', padx=76, pady=5, command=equal)
button_clear = Button(calc, text='C', padx=21, pady=22, command=clear)
button_delete = Button(calc, text='Del', padx=16, pady=5, command=button_del)
# Put the buttons ordered by row
# row 1
button_7.grid(column=0, row=1)
button_8.grid(column=1, row=1)
button_9.grid(column=2, row=1)
button_plus.grid(column=4, row=1)
button_multiply.grid(column=5, row=1)
# row 2
button_4.grid(column=0, row=2)
button_5.grid(column=1, row=2)
button_6.grid(column=2, row=2)
button_minus.grid(column=4, row=2)
button_division.grid(column=5, row=2)
# row 3
button_1.grid(column=0, row=3)
button_2.grid(column=1, row=3)
button_3.grid(column=2, row=3)
button_delete.grid(column=4, row=3)
button_clear.grid(column=5, row=3, rowspan=2)
# row 4
button_0.grid(column=0, row=4)
button_square.grid(column=4, row=4)
button_equal.grid(column=1, row=4, columnspan=2)

calc.mainloop()
