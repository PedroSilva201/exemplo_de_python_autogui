import pyautogui
import time

# Aguarda alguns segundos para o usuário se preparar
time.sleep(3)

# Abre o menu iniciar (atalho do Windows)
pyautogui.press("win")

# Digita "Bloco de Notas" e pressiona Enter
pyautogui.write("Bloco de Notas")
pyautogui.press("enter")

# Aguarda o Bloco de Notas abrir
time.sleep(5)

# Digita o texto no Bloco de Notas
pyautogui.write("Episodio 1:")
pyautogui.press("enter")
time.sleep(2)
# Digita o texto no Bloco de Notas
pyautogui.write("Episodio 2:")
pyautogui.press("enter")
time.sleep(2)
# Digita o texto no Bloco de Notas
pyautogui.write("Episodio 3:")
pyautogui.press("enter")
time.sleep(2)
# Digita o texto no Bloco de Notas
pyautogui.write("Episodio 4:")
pyautogui.press("enter")
time.sleep(2)
# Digita o texto no Bloco de Notas
pyautogui.write("Episodio 5:")
pyautogui.press("enter")
time.sleep(2)
# Digita o texto no Bloco de Notas
pyautogui.write("Episodio 6:")
pyautogui.press("enter")
time.sleep(2)
# Digita o texto no Bloco de Notas
pyautogui.write("Episodio 7:")
pyautogui.press("enter")
time.sleep(2)
# Digita o texto no Bloco de Notas
pyautogui.write("Episodio 8:")
pyautogui.press("enter")
time.sleep(2)

# Simula a combinação de teclas Ctrl+S para salvar
pyautogui.hotkey("ctrl", "s")

# Digita o nome do arquivo e salva
pyautogui.write("Arquivo-5")
pyautogui.press("enter")
