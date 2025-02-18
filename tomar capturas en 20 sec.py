
import pyautogui 
import time

a=0

while a<10:
    direccion=f"d:\\trabajos de progra\\ConsoleApp1\\screenshot{a}.png"
    a=a+1
    imagen=pyautogui.screenshot()
    imagen.save(direccion)
    time.sleep(2)
