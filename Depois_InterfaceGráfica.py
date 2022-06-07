import PySimpleGUI as sg

sg.theme('SystemDefaultForReal')

layout = [
    [sg.Image(filename='entra.png')],
    [sg.Text('Usuário', size=(7, 1)), sg.Input()],
    [sg.Text('Senha', size=(7, 1)), sg.Input()],
    [sg.Checkbox('Salvar Login?')],
    [sg.Text('Esqueceu a senha? Clique Aqui')],
    [sg.Button('Entrar'), sg.Button('Cadastrar')],

]

janela = sg.Window('Login', layout=layout, element_justification='c')
janela.read()
janela.close()
#faddfgdgs
