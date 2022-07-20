from selenium import webdriver as wd
import PySimpleGUI as sg
from selenium.webdriver.common.by import By
from time import sleep
import random

sg.theme('reddit')

layout = [
    [sg.Text('BEM-VINDO', font=('Gotham-Bold', 35))],
    [sg.Text('Faça seu Login ou cadastre-se', font=('Gotham-light', 12))],
    [sg.Text('Login', size=(5, 1)), sg.Input(size=(40, 1))],
    [sg.Text('Senha', size=(5, 1)), sg.Input(size=(40, 1))],
    [sg.Text('Esqueceu a senha? Clique aqui!', font=('Gotham-light', 10))],
    [sg.Button('Entrar'), sg.Button('Cadastrar')],
    [],
]

janela = sg.Window('Tela Inicial', layout=layout, element_justification='c')
janela.read()
janela.close()