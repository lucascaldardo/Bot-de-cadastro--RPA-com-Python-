import pyautogui
import time
import pandas as pd
from pyautogui import alert, confirm  # para mensagens visuais

# Configurações iniciais
pyautogui.PAUSE = 0.8          # Pausa entre ações (aumentei um pouco para mais segurança)
pyautogui.FAILSAFE = True      # Mova o mouse para o canto superior esquerdo para emergencial parar

# === CONFIGURAÇÕES - ALTERE AQUI ===
URL_SISTEMA = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
EMAIL = "pythoimpressionador@gmail.com"
SENHA = "1234"
CAMINHO_CSV = "C:\Users\calld\OneDrive\Desktop\PC\Estudos\Python\Automações de Tarefas e Bots  Jornada Python [Aula 1]\produtos.csv"
# === FIM DAS CONFIGURAÇÕES ===

# Lê a tabela de produtos
try:
    tabela = pd.read_csv(CAMINHO_CSV)
    print(f" Arquivo lido com sucesso! {len(tabela)} produtos para cadastrar.")
except FileNotFoundError:
    alert("ERRO: Arquivo CSV não encontrado no caminho informado!")
    exit()
except Exception as e:
    alert(f"Erro ao ler o CSV: {str(e)}")
    exit()

# Abre o Chrome
pyautogui.press("win")
time.sleep(0.5)
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(4)  # Tempo para o navegador abrir

# Digita o link e entra
pyautogui.write(URL_SISTEMA)
pyautogui.press("enter")
time.sleep(5)  # Espera carregar a página de login (aumente se sua internet for lenta)

# Faz login
try:
    # Clique no campo de email (ajuste coordenada se necessário)
    pyautogui.click(x=1019, y=465)   # ← AJUSTE ESSA COORDENADA
    pyautogui.write(EMAIL)
    pyautogui.press("tab")
    pyautogui.write(SENHA)
    pyautogui.press("enter")
    time.sleep(5)  # Espera carregar o sistema após login
    print("Login realizado!")
except Exception as e:
    alert(f"Erro durante o login: {str(e)}\nVerifique as coordenadas ou conexão.")
    exit()

# Cadastro dos produtos
for indice, linha in tabela.iterrows():
    print(f"Cadastrando produto {indice + 1}/{len(tabela)} → {linha['codigo']}")
    
    try:
        # Clique no botão "Cadastrar novo" (ajuste coordenada!)
        pyautogui.click(x=974, y=324)   # ← AJUSTE ESSA COORDENADA
        time.sleep(1.5)  # Espera o formulário abrir
        
        # Preenche os campos
        pyautogui.write(str(linha["codigo"]))
        pyautogui.press("tab")
        
        pyautogui.write(str(linha["marca"]))
        pyautogui.press("tab")
        
        pyautogui.write(str(linha["tipo"]))
        pyautogui.press("tab")
        
        pyautogui.write(str(linha["categoria"]))
        pyautogui.press("tab")
        
        pyautogui.write(str(linha["preco_unitario"]))
        pyautogui.press("tab")
        
        pyautogui.write(str(linha["custo"]))
        pyautogui.press("tab")
        
        obs = str(linha["obs"])
        if obs != "nan" and obs.strip() != "":
            pyautogui.write(obs)
        
        pyautogui.press("tab")  # Vai para o botão de enviar
        pyautogui.press("enter")  # Envia o formulário
        time.sleep(2)  # Espera processar o cadastro
        
        # Em vez de scroll fixo, um pequeno delay + confirmação visual (opcional)
        # Se o sistema voltar para a lista, pode clicar novamente no "novo"
        
    except Exception as e:
        print(f"Erro no produto {linha['codigo']}: {str(e)}")
        resposta = confirm(
            f"Erro ao cadastrar {linha['codigo']}. Continuar com o próximo?",
            buttons=["Sim", "Parar"]
        )
        if resposta == "Parar":
            break

# Finaliza
alert(f"Cadastro finalizado!\nTotal de produtos processados: {indice + 1}")
print("=== BOT FINALIZADO ===")