
  
from tkinter import ttk
from tkinter import *
class Product:

    def __init__(self, window):
            # Initializations 
            self.wind = window
            self.wind.title('Products Application')

            # Creating a Frame Container 
            frame = LabelFrame(self.wind, text = 'Register new Product')
            frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

            # Name Input
            Label(frame, text = 'Name: ').grid(row = 1, column = 0)
            self.name = Entry(frame)
            self.name.focus()
            self.name.grid(row = 1, column = 1)

            # Price Input
            Label(frame, text = 'Price: ').grid(row = 2, column = 0)
            self.price = Entry(frame)
            self.price.grid(row = 2, column = 1)

            # Button Add Product 
            ttk.Button(frame, text = 'Save Product').grid(row = 3, columnspan = 2, sticky = W + E)

            # Output Messages 
            self.message = Label(text = '', fg = 'red')
            self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

            # Table
            self.tree = ttk.Treeview(height = 10, columns = 2)
            self.tree.grid(row = 4, column = 0, columnspan = 2)
            self.tree.heading('#0', text = 'Name', anchor = CENTER)
            self.tree.heading('#1', text = 'Price', anchor = CENTER)

            # Buttons
            ttk.Button(text = 'DELETE' ).grid(row = 5, column = 0, sticky = W + E)
            ttk.Button(text = 'EDIT').grid(row = 5, column = 1, sticky = W + E)

            # Filling the Rows
           # self.get_products()

if __name__ == '__main__':
        window = Tk()
        application = Product(window)
        window.mainloop()