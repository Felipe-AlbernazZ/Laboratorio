from tkinter import *


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Cria uma tela de entrada
        self.screen = Entry(master, width=25, font=("Arial", 16))
        self.screen.grid(row=0, column=0, columnspan=4, pady=10)

        # Cria os botões
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)
        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)
        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("=", 4, 2)
        self.create_button("+", 4, 3)

        # Cria o botão "Clear"
        self.clear_button = Button(
            master, text="Clear", width=20, height=2, command=self.clear_screen)
        self.clear_button.grid(row=5, column=0, columnspan=4)

    def create_button(self, text, row, column):
        button = Button(self.master, text=text, width=5, height=2,
                        command=lambda: self.button_click(text))
        button.grid(row=row, column=column)

    def button_click(self, text):
        if text == "=":
            result = str(eval(self.screen.get()))
            self.screen.delete(0, END)
            self.screen.insert(0, result)
        else:
            self.screen.insert(END, text)

    def clear_screen(self):
        self.screen.delete(0, END)


root = Tk()
calculator = Calculator(root)
root.mainloop()
