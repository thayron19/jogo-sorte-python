import random
import tkinter
import keyboard
# ---------------------------------------------------------------------------------------------------------------------
janela = tkinter.Tk()

janela.title('Jogo da sorte')

largura_janela = 300
altura_janela = 190

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

posicaol = float(largura_janela / 2 - largura_tela / 2)
posicaoa = float(altura_janela / 2 - altura_tela / 2)

janela.geometry("%dx%d%d%d" % (largura_janela, altura_janela, posicaol, posicaoa))
janela.resizable(width=False, height=False)


# ---------------------------------------------------------------------------------------------------------------------
def adivinha(num):
    aleatorio = random.randint(1, 7)

    if aleatorio == num:
        jogo_result_var.set(f'Seu número foi {num}.\n\nMeu número era {aleatorio}.\n\nVocê acertou!')
    else:
        jogo_result_var.set(f'Seu número foi {num}.\n\nMeu número era {aleatorio}.\n\nVocê errou!')


# ---------------------------------------------------------------------------------------------------------------------
jogo_texto = tkinter.Label(janela, text='Pensei em um número de 1 a 7, qual é?', font=('', 12))
jogo_texto.place(x=10, y=10)
# ---------------------------------------------------------------------------------------------------------------------
jogo_btn = tkinter.Button(janela, text='1', command=lambda: adivinha(1))
jogo_btn.place(x=10, y=40, width=30)

jogo_btn = tkinter.Button(janela, text='2', command=lambda: adivinha(2))
jogo_btn.place(x=50, y=40, width=30)

jogo_btn = tkinter.Button(janela, text='3', command=lambda: adivinha(3))
jogo_btn.place(x=90, y=40, width=30)

jogo_btn = tkinter.Button(janela, text='4', command=lambda: adivinha(4))
jogo_btn.place(x=130, y=40, width=30)

jogo_btn = tkinter.Button(janela, text='5', command=lambda: adivinha(5))
jogo_btn.place(x=170, y=40, width=30)

jogo_btn = tkinter.Button(janela, text='6', command=lambda: adivinha(6))
jogo_btn.place(x=210, y=40, width=30)

jogo_btn = tkinter.Button(janela, text='7', command=lambda: adivinha(7))
jogo_btn.place(x=250, y=40, width=30)
# ---------------------------------------------------------------------------------------------------------------------
jogo_result_var = tkinter.StringVar()
jogo_result_texto = tkinter.Label(janela, textvariable=jogo_result_var, font=('', 12), justify='center')
jogo_result_texto.place(x=10, y=80, width=300)
# ---------------------------------------------------------------------------------------------------------------------
keyboard.on_press_key('1', lambda _: adivinha(1))
keyboard.on_press_key('2', lambda _: adivinha(2))
keyboard.on_press_key('3', lambda _: adivinha(3))
keyboard.on_press_key('4', lambda _: adivinha(4))
keyboard.on_press_key('5', lambda _: adivinha(5))
keyboard.on_press_key('6', lambda _: adivinha(6))
keyboard.on_press_key('7', lambda _: adivinha(7))

keyboard.on_press_key('ESC', lambda _: janela.destroy())
# ---------------------------------------------------------------------------------------------------------------------
janela.mainloop()
