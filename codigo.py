import pyautogui
import time
import pandas

pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.PAUSE = 5
pyautogui.press("enter")
pyautogui.PAUSE = 1
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=630, y=405)
pyautogui.hotkey("ctrl","a")
pyautogui.write("gamasouza56@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.click(x=666, y=562)
time.sleep(3)

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
    pyautogui.click(x=592, y=298)
    
    codigo = str(tabela.loc[linha,"codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    
    marca = str(tabela.loc[linha,"marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str(tabela.loc[linha,"tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    
    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    
    preco = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    
    custo = str(tabela.loc[linha,"custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    
    pyautogui.click(x=592, y=572)

    pyautogui.scroll(1000)