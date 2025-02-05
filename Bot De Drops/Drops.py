
import pyautogui 
import time 

#Servidor da Karuta

link = "https://discord.com/channels/866899041375223819/1292965515815551006"

# 1 passo - Abrir Navegadores

# 1 - Brave

pyautogui.hotkey("win","s")
time.sleep(3)
pyautogui.write("brave")
pyautogui.press("enter")
time.sleep(5)
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(5)

# 2 - Opera

pyautogui.hotkey("win","s")
time.sleep(3)
pyautogui.write("Opera")
pyautogui.press("enter")
time.sleep(5)
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

# 3 - Chrome
pyautogui.hotkey("win","s")
time.sleep(3)
pyautogui.write("Chrome")
pyautogui.press("enter")
time.sleep(5)
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

# 2 passo - Primeiro pick - Chrome =================================================================================================

def executar_picks2():
    time.sleep(4)

    # -- CHROME --

    pyautogui.click(x=35, y=116) # Selecionar o aba principal do discord
    time.sleep(2)
    pyautogui.click(x=168, y=112) # Barra de busca do servidores
    time.sleep(2)
    pyautogui.write("phd") # Nome do servidor
    time.sleep(2)
    pyautogui.click(x=151, y=316) # Selecionar o chat-karuta
    time.sleep(2)
    pyautogui.click(x=1485, y=722) # Clicar foda das cartas para que n interompa o processo
    time.sleep(2)
    pyautogui.hotkey("fn","end") # caso o chat esteja muito acima n e possivel pegar as cartas pela posicao do mouse
    time.sleep(3)   
    pyautogui.write("kd") # kd -> comando usado para karuta dropa cartas, so pode ser usado a cada 30 min
    time.sleep(2)
    pyautogui.click(x=408, y=934) # pegar a primeira carta
    time.sleep(4)

    pyautogui.click(x=1181, y=1056) # Selecionando proximo navegado
    time.sleep(4)

    # -- BRAVE --

    pyautogui.click(x=37, y=147) # Selecionar o aba principal do discord
    time.sleep(2)
    pyautogui.click(x=177, y=141) # Barra de busca do servidores
    time.sleep(2)
    pyautogui.write("phd") # Nome do servidor
    time.sleep(2)
    pyautogui.click(x=168, y=352) # Selecionar o chat-karuta
    time.sleep(2)
    pyautogui.click(x=1544, y=751) # Clicar foda das cartas para que n interompa o processo
    time.sleep(2)
    pyautogui.hotkey("fn","end") # caso o chat esteja muito acima n e possivel pegar as cartas pela posicao do mouse
    time.sleep(3)
    pyautogui.click(x=461, y=907) # pegar a segunda carta
    time.sleep(4)

    pyautogui.click(x=1132, y=1064) # Selecionando proximo navegador
    time.sleep(4)

    # -- Opera -- 

    pyautogui.click(x=77, y=101) # Selecionar o aba principal do discord
    time.sleep(2)
    pyautogui.click(x=208, y=98) # Barra de busca do servidores
    time.sleep(2)
    pyautogui.write("phd") # Nome do servidor
    time.sleep(2)
    pyautogui.click(x=228, y=303) # Selecionar o chat-karuta
    time.sleep(2)
    pyautogui.click(x=1564, y=751) # Clicar foda das cartas para que n interompa o processo
    time.sleep(2)
    pyautogui.hotkey("fn","end") # caso o chat esteja muito acima n e possivel pegar as cartas pela posicao do mouse
    time.sleep(3)
    pyautogui.click(x=557, y=869) # pegar a terceira carta
    time.sleep(4)

    time.sleep(610) # time para dar o segundo KD - 1 pick pode ser feito a cada 10 min coloquei mais 10/s para n dar erro de tempo

    # ==============================================================================================================================

    # 2 - Segundo pick -- OPERA --  

    pyautogui.click(x=77, y=101) # Selecionar o aba principal do discord
    time.sleep(2)
    pyautogui.click(x=208, y=98) # Barra de busca do servidores
    time.sleep(2)
    pyautogui.write("phd") # Nome do servidor
    time.sleep(2)
    pyautogui.click(x=228, y=303) # Selecionar o chat-karuta
    time.sleep(2)
    pyautogui.click(x=1564, y=751) # Clicar foda das cartas para que n interompa o processo
    time.sleep(2)
    pyautogui.hotkey("fn","end") # caso o chat esteja muito acima n e possivel pegar as cartas pela posicao do mouse
    time.sleep(3)   
    pyautogui.write("kd") # kd -> comando usado para karuta dropa cartas, so pode ser usado a cada 30 min
    time.sleep(2)
    pyautogui.click(x=445, y=932) # pegar a primeira carta
    time.sleep(4)

    pyautogui.click(x=1082, y=1070) # Selecionando proximo navegador
    time.sleep(4)

    # -- CHROME --

    pyautogui.click(x=35, y=116) # Selecionar o aba principal do discord
    time.sleep(2)
    pyautogui.click(x=168, y=112) # Barra de busca do servidores
    time.sleep(2)
    pyautogui.write("phd") # Nome do servidor
    time.sleep(2)
    pyautogui.click(x=151, y=316) # Selecionar o chat-karuta
    time.sleep(2)
    pyautogui.click(x=1485, y=722) # Clicar foda das cartas para que n interompa o processo
    time.sleep(2)
    pyautogui.hotkey("fn","end") # caso o chat esteja muito acima n e possivel pegar as cartas pela posicao do mouse
    time.sleep(3)
    pyautogui.click(x=462, y=904) # pegar a segunda carta
    time.sleep(4)

    pyautogui.click(x=1181, y=1056) # Selecionando proximo navegador
    time.sleep(4)

    # -- BRAVE --

    pyautogui.click(x=37, y=147) # Selecionar o aba principal do discord
    time.sleep(2)
    pyautogui.click(x=177, y=141) # Barra de busca do servidores
    time.sleep(2)
    pyautogui.write("phd") # Nome do servidor
    time.sleep(2)
    pyautogui.click(x=168, y=352) # Selecionar o chat-karuta
    time.sleep(2)
    pyautogui.click(x=1564, y=751) # Clicar foda das cartas para que n interompa o processo
    time.sleep(2)
    pyautogui.hotkey("fn","end") # caso o chat esteja muito acima n e possivel pegar as cartas pela posicao do mouse
    time.sleep(3)
    pyautogui.click(x=508, y=869) # pegar a terceira carta
    time.sleep(4)

    time.sleep(610) # time para dar o terceiro KD - 1 pick pode ser feito a cada 10 min

    # ==============================================================================================================================

    # 3 - Terceiro pick -- BRAVE --  

    pyautogui.click(x=37, y=147) # Selecionar o aba principal do discord
    time.sleep(2)
    pyautogui.click(x=177, y=141) # Barra de busca do servidores
    time.sleep(2)
    pyautogui.write("phd") # Nome do servidor
    time.sleep(2)
    pyautogui.click(x=168, y=352) # Selecionar o chat-karuta
    time.sleep(2)
    pyautogui.click(x=1564, y=751) # Clicar foda das cartas para que n interompa o processo
    time.sleep(2)
    pyautogui.hotkey("fn","end") # caso o chat esteja muito acima n e possivel pegar as cartas pela posicao do mouse
    time.sleep(3)   
    pyautogui.write("kd") # kd -> comando usado para karuta dropa cartas, so pode ser usado a cada 30 min
    time.sleep(2)
    pyautogui.click(x=397, y=935) # pegar a primeira carta
    time.sleep(4)

    pyautogui.click(x=1133, y=1058) # Selecionando proximo navegador
    time.sleep(4)

    # -- OPERA --

    pyautogui.click(x=77, y=101) # Selecionar o aba principal do discord
    time.sleep(2)
    pyautogui.click(x=208, y=98) # Barra de busca do servidores
    time.sleep(2)
    pyautogui.write("phd") # Nome do servidor
    time.sleep(2)
    pyautogui.click(x=228, y=303) # Selecionar o chat-karuta
    time.sleep(2)
    pyautogui.click(x=1564, y=751) # Clicar foda das cartas para que n interompa o processo
    time.sleep(2)
    pyautogui.hotkey("fn","end") # caso o chat esteja muito acima n e possivel pegar as cartas pela posicao do mouse
    time.sleep(3)
    pyautogui.click(x=503, y=906) # pegar a segunda carta
    time.sleep(4)

    pyautogui.click(x=1086, y=1071) # Selecionando proximo navegador
    time.sleep(4)

    # -- CHROME --

    pyautogui.click(x=35, y=116) # Selecionar o aba principal do discord
    time.sleep(2)
    pyautogui.click(x=168, y=112) # Barra de busca do servidores
    time.sleep(2)
    pyautogui.write("phd") # Nome do servidor
    time.sleep(2)
    pyautogui.click(x=151, y=316) # Selecionar o chat-karuta
    time.sleep(2)
    pyautogui.click(x=1485, y=722) # Clicar foda das cartas para que n interompa o processo
    time.sleep(2)
    pyautogui.hotkey("fn","end") # caso o chat esteja muito acima n e possivel pegar as cartas pela posicao do mouse
    time.sleep(3)
    pyautogui.click(x=517, y=874) # pegar a terceira carta
    time.sleep(4)

    time.sleep(610) # time para dar o terceiro KD - 1 pick pode ser feito a cada 10 min

    # RESETE DO CICLO DE PICKS

while True:
    executar_picks2()



































