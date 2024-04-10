# Passo a Passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pip install pyautogui
import pyautogui
import time

pyautogui.PAUSE = 0.5
# pyautogui.click -> Clicar em algum lugar da tela
# pyautogui.write -> escrever um texto
# pyautogui.press -> precionar 1 tecka do teclado 

# abrir o navegador (chrome)
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# entrar no site
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')

# dar uma pausa um pouco maior (3 segundos)
time.sleep(3)
 
    
# Passo 2: Fazer login
pyautogui.click(x=1361, y=394)
pyautogui.write('pythonteste@gmail.com')

# escrever a senha
pyautogui.press('tab')
pyautogui.write('senha')

# clicar no botao de logar
pyautogui.click(x=1450, y=532)
time.sleep(3)

# Passo 3: Importar a base de dados
# pip install pandas numpy openpyxl
import pandas

tabela = pandas.read_csv('produtos.csv')


# Passo 4: Cadastrar 1 poroduto
# para cada linha da minha tabela
for linha in tabela.index:
    # clicar no primeiro campo
    pyautogui.click(x=1372, y=287)
    #codigo do produto
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')
    #marca do produto
    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')
    #tipo do produto
    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')
    #Categoria do produto
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    #preco do produto
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    #custo do produto
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    #obs do produto
    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):    
        pyautogui.write(obs)
    pyautogui.press('tab')
    #enviar
    pyautogui.press('enter')
    pyautogui.scroll(10000000)


# Passo 5: Repetir o processo de cadastro ate acabar a base de dados
