import  pyautogui
import time
import pandas
pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
tabela = pandas.read_csv("C:/Users/calld/OneDrive/Documentos/GitHub/Bot-de-cadastro--RPA-com-Python-/Automações de Tarefas com Python/produtos.csv")
#Entrar no sistema
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
#Fazer login
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=1019, y=465)
pyautogui.write("pythoimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("1234")
pyautogui.press("enter")
time.sleep(3)
#Cadastrar produtos
for linha in tabela.index:
    pyautogui.click(x=974, y=324)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
        pyautogui.press("tab")
        pyautogui.press("enter")
        pyautogui.scroll(5000)
