import PySimpleGUI as sg

class TelaPython:
	def __init__(self):
		# Layout
		layout = [
			[sg.Text('Nome',size=(5,0)),sg.Input(size=(20,0),key='nome')],
			[sg.Text('Idade',size=(5,0)),sg.Input(size=(5,0),key='idade')],
			[sg.Text('Quais provedores de e-mails são aceitos?')],
			[sg.Checkbox('Gmail',key='gmail'),sg.Checkbox('Outlook',key='outlook'),sg.Checkbox('Yahoo',key='yahoo')],
			[sg.Text('Insira seu E-mail',size=(10,0)),sg.Input(size=(30,0),key='email')],
			[sg.Button('Enviar Dados',size=(20,0))],
			[sg.Output(size=(50,20))]
		]
		# Janela
		self.janela = sg.Window("Dados do Usuário").layout(layout)

	def Iniciar(self):
		while True:
			# Extrair os dados da tela
			self.button, self.values = self.janela.Read()
			nome = self.values['nome']
			idade = self.values['idade']
			aceita_gmail = self.values['gmail']
			aceita_outlook = self.values['outlook']
			aceita_yahoo = self.values['yahoo']
			email = self.values['email']
			print(f'Nome: {nome}')
			print(f'Idade: {idade}')
			if aceita_gmail == True:
				print(f'O seu G-mail é "{email}"')
			elif aceita_outlook == True:
				print(f'O seu Outlook é "{email}"')
			elif aceita_yahoo == True:
				print(f'O seu Yahoo é "{email}"')
			else:
				print('Voce não selecionou nenhuma opção de E-mail')


tela = TelaPython()
tela.Iniciar()
