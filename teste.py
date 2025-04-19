"""import pyautogui
import time """

"""pyautogui.hotkey('win','tab')
time.sleep(2)
pyautogui.press('right')
time.sleep(3)"""

import pyautogui
import time
import random
import string

def gerar_palavra_aleatoria(tamanho):
    letras = string.ascii_lowercase
    return ''.join(random.choice(letras) for _ in range(tamanho))

# Exemplo de uso
tamanho_palavra = 8
#palavra_aleatoria = gerar_palavra_aleatoria(tamanho_palavra)

time.sleep(4)

count = 0
while count < 10:   
    pyautogui.press('win')
    pyautogui.write('firefox')
    pyautogui.press('enter')    
    time.sleep(4)
    
    palavra_aleatoria = gerar_palavra_aleatoria(tamanho_palavra)
    print(f"Palavra aleatória gerada: {palavra_aleatoria}")
    
    pyautogui.write(palavra_aleatoria)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'f4')
    
    count += 1

"""pyautogui.hotkey('alt')
pyautogui.hotkey('alt','tab')
pyautogui.hotkey('alt')
pyautogui.hotkey('alt','tab')
pyautogui.hotkey('alt')
pyautogui.hotkey('alt','tab')"""