
import pyautogui
import time

# este programa ja foi transformado em um arquivo .exe usando pyinstaller

print('='*30)
print('VER POSITION X, Y DO MOUSE')
print('='*30)

print('-'*80)
print('para descobrir o x e y do seu mouse \ndeixe o seu mouse parado em cima de onde voce quer descobrir a posição e aguarde.')
print('-'*80)

ver = input('deseja ver a posição x e y do seu mouse S / N ?: ')

u = ver.upper()

# função msg de error.
def error():

    err = ('voce precisa digitar um valor valido!!! ')
    print(err)
    deseja()

# função que pergunta se o usuario deseja continuar a execução do programa.
def deseja():

    dsj = input('deseja executar o programa novamente S / N ?: ')
    up = dsj.upper()

    if up == 'S':
        descobre()
    elif up == 'N':
        exit()    
    else:
        error()

# função que mostra os valores da posição do mouse
def descobre():

    time.sleep(3)
    vp = pyautogui.position()
    vl = 'o x e y do seu mouse são: {}'.format(vp)
    print(vl)

    deseja()

if u == 'S':

    descobre()
elif u == 'N':

    exit()
else:
    
    error()

dsj = input('deseja executar o programa novamente S / N ?: ')