import PySimpleGUI as sg


class TelaPython:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text("Login", size=(5, 0)), sg.Input(
                "Dite seu login", size=(10, 0))],
            [sg.Text("Senha", size=(5, 0)), sg.Input(
                "Digite sua senha", size=(10, 0))],
            [sg.Button('Entrar')]

        ]
        # janela
        self.janela = sg.Window("Tela de Login").Layout(layout)

    def Iniciar(self):
        # Extrair dados da tela
        self.button, self.values = self.janela.Read()


tela = TelaPython()
tela.Iniciar()
