import PySimpleGUI as sg

layout = [
    [sg.Text('Usuário'), sg.Input()],
    [sg.Text('Senha'), sg.Input()],
    [sg.Checkbox('Salvar Login?')],
    [sg.Text('Esqueceu a senha? Clique Aqui')],
    [sg.Button('Entrar'), sg.Button('Cadastrar')],
]

janela = sg.Window('Login', layout=layout)
janela.read()
janela.close()
