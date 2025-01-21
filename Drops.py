
import pyautogui 
import time 

#Servidor da Karuta
link = "https://discord.com/channels/866899041375223819/1292965515815551006"

kd = pyautogui.write("kd")

#posicao_1 = x=411, y=959
#posicao_2 = x=464, y=925
#posicao_3 = x=511, y=858

#posicao_1 google/brave = x=396, y=941
#posicao_2 google/brave = x=458, y=902
#posicao_3 google/brave = x=514, y=878

#cliqueN1 = x=1197, y=1061
#cliqueN2 = x=1155, y=1063
#cliqueN3 = x=1110, y=1054

# 1 passo - Abrir Navegadores

# 1 - Opera

pyautogui.hotkey("win","s")
time.sleep(1)
pyautogui.write("brave")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

# 2 - Google 

pyautogui.hotkey("win","s")
time.sleep(1)
pyautogui.write("Chrome")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

# 3 - Brave

pyautogui.hotkey("win","s")
time.sleep(1)
pyautogui.write("opera")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

# 2 passo - Primeiro kd e grabs =================================================================================================

def executar_picks():
    time.sleep(5)

    pyautogui.click(x=1568, y=731)
    time.sleep(2)
    pyautogui.click(x=503, y=988)
    time.sleep(2)
    #pyautogui.write(kd)kd
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.click(x=448, y=933) # posicao 1 - opera
    time.sleep(2)

    pyautogui.click(x=1197, y=1061)
    time.sleep(5)
    pyautogui.click(x=462, y=909) # posicao 2 - chrome
    time.sleep(2)

    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    time.sleep(0.2)
    pyautogui.press('tab')
    pyautogui.keyUp('alt')

    time.sleep(5)
    pyautogui.click(x=1502, y=764)
    time.sleep(2)
    pyautogui.click(x=514, y=878) # posicao 3 - brave
    time.sleep(610)
    #termina pelo brave

    # 2 REPETIÇÃO - Comencando pelo brave ==========================================================================================

    pyautogui.click(x=1502, y=764)
    time.sleep(2)
    pyautogui.click(x=396, y=992) # posição do chat
    time.sleep(5)
    #kdpyautogui.write(kd)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.click(x=400, y=934) # posicao 1 - brave
    time.sleep(5)


    pyautogui.click(x=1105, y=1056)
    time.sleep(5)
    pyautogui.click(x=1491, y=737)
    time.sleep(2)
    pyautogui.click(x=465, y=905) # posicao 2 - chrome
    time.sleep(5)


    pyautogui.click(x=1215, y=1065)
    time.sleep(5)
    pyautogui.click(x=556, y=874) # posicao 3 - opera
    time.sleep(610)


    # 3 REPETIÇÃO - Començando pelo Chorme ===========================================================================================

    pyautogui.click(x=1491, y=737)
    time.sleep(2)
    pyautogui.click(x=445, y=998)
    #pyautogui.write(kd)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.click(x=403, y=940) # posicao 1 - chrome
    time.sleep(5)


    pyautogui.click(x=1157, y=1064)
    time.sleep(5)
    pyautogui.click(x=1502, y=764)
    time.sleep(2)
    pyautogui.click(x=456, y=908) # posicao 2 - brave
    time.sleep(5)


    pyautogui.click(x=1215, y=1065)
    time.sleep(5)
    pyautogui.click(x=1568, y=731)
    time.sleep(2)
    pyautogui.click(x=556, y=874) # posicao 3 - opera
    time.sleep(610)

    pyautogui.click(x=456, y=993)

while True:
    executar_picks()



































