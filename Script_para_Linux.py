import pyautogui
import time
import random
import string

def gerar_palavra_aleatoria(tamanho):
    letras = string.ascii_lowercase
    return ''.join(random.choice(letras) for _ in range(tamanho))

tamanho_palavra = 8

pyautogui.press('win')
pyautogui.write('linux')
pyautogui.press('enter')
time.sleep(5) 
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('win','tab')
time.sleep(2)
pyautogui.press('right')
time.sleep(3)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(60)
pyautogui.press('space')
time.sleep(1)
pyautogui.write('vitor')
time.sleep(30)
pyautogui.press('win')
pyautogui.write('firefox')

count = 0
while count < 10:   
  
    palavra_aleatoria = gerar_palavra_aleatoria(tamanho_palavra)
    print(f"Palavra aleatória gerada: {palavra_aleatoria}")

    pyautogui.hotkey('ctrl', 't')    
    pyautogui.write(palavra_aleatoria)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'f4')
    
    count += 1