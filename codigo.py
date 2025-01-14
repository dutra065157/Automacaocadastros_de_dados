import pandas as pd
import pyautogui

import time


pyautogui.PAUSE = 1

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(5)
pyautogui.click(x=597, y=409)
pyautogui.write("renato065157@gmail.com")
pyautogui.press("tab")
pyautogui.write("renato123")
pyautogui.press("tab")

pyautogui.press("enter")


tabela = pd.read_csv("produtos (2).csv")
time.sleep(5)
# cadastrar produtos
for linha in tabela.index:

    pyautogui.click(x=599, y=296)

    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preco_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    # obs
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write("obs")
    pyautogui.press("tab")
    pyautogui.press("enter")  # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
