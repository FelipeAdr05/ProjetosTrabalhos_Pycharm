import PySimpleGUI as sg

sg.theme('SystemDefaultForReal')

layout = [
    [sg.Image(filename='entra.png')],
    [sg.Text('Usuário', size=(7, 1)), sg.Input()],
    [sg.Text('Senha', size=(7, 1)), sg.Input()],
    [sg.Checkbox('Salvar Login?')],
    [sg.Text('Esqueceu a senha? Clique Aqui')],
    [sg.Button('Entrar', font=('bold', 10)), sg.Button('Cadastrar', font=('bold', 10))],
]

janela = sg.Window('Tela de Login', layout=layout, element_justification='center')
janela.read()
janela.close()


'''
comandos: 

sg.Image
sg.theme

formatações:

filename=
size=
element_justification=
'''
