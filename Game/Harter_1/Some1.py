import time
from rich import print
import keyboard
import os
from Harter_1.Some2 import *

clear = lambda: os.system('cls')

Sel1 = 1

def Var1():
    print("\n\n        [b]Разраб: ", end="")
    print("[light_cyan1]О ебать, давно тут некого небыло...")
    time.sleep(3)
    clear()
    print("\n\n        [b]Разраб: ", end="")
    print("[light_cyan1]Прочем я рад что ты сдесь 🙂")
    time.sleep(4)
    clear()
    print("\n\n        [b]Разраб: ", end="")
    print("[light_cyan1]Думаю ты уже хочешь играть, поэтому что я хотел сказать")
    time.sleep(5)
    clear()
    print("\n\n        [b]Разраб: ", end="")
    print("[light_cyan1]Каждый твой [b]выбор влияет на сюжет")
    time.sleep(4)
    clear()
    print("\n\n        [b]Разраб: ", end="")
    print("[light_cyan1]Ну удачной игры!")
    time.sleep(3)
    clear()
    print("\n\n        [b]Разраб: ", end="")
    print("[light_cyan1]Полный бред начнется через 5 секунд...")
    time.sleep(5)
    clear()
    gamepl1()
    
def Var2():
    print("\n\n        [b]Разраб: ", end="")
    print("[light_cyan1]О ебать, давно тут некого небыло...")
    time.sleep(3)
    clear()
    print("\n\n        [b]Разраб: ", end="")
    print("[light_cyan1]ЕЩЕ РАЗ ПОШЛЕШЬ МЕНЯ НАХУЙ Я ТЕБЕ ТВОЯН ЗАКАЧАЮ! 😃")
    time.sleep(4)
    clear()
    print("\n\n        [b]Разраб: ", end="")
    print("[light_cyan1]Думаю ты уже хочешь играть, поэтому что я хотел сказать")
    time.sleep(5)
    clear()
    print("\n\n        [b]Разраб: ", end="")
    print("[light_cyan1]Каждый твой [b]выбор влияет на сюжет")
    time.sleep(4)
    clear()
    print("\n\n        [b]Разраб: ", end="")
    print("[light_cyan1]Ну иди нахуй!")
    time.sleep(3)
    clear()
    print("\n\n        [b]Разраб: ", end="")
    print("[light_cyan1]Полный бред начнется через 5 секунд...")
    time.sleep(5)
    clear()
    gamepl1()
    

def NewGame():
    Sel1 = 1
    clear()
    time.sleep(0.5)
    print("\n\n        [b]Некто: ", end="")
    print("[grey35]эй сдесь есть кто нибуть?")
    time.sleep(1)
    clear()
    print("\n\n        [b]Некто: ", end="")
    print("[grey35]эй сдесь есть кто нибуть?\n\n\n[bold][light_sky_blue1]          > Я сдесь[default]       Иди нахуй")
    while True:
        time.sleep(0.1)
        if keyboard.is_pressed('d'):
            time.sleep(0.1)
            clear()
            print("\n\n        [b]Некто: ", end="")
            print("[grey35]эй сдесь есть кто нибуть?\n\n\n[bold][default]            Я сдесь[light_sky_blue1]     > Иди нахуй")
            Sel1 = 2
        elif keyboard.is_pressed('a'):
            time.sleep(0.1)
            clear()
            print("\n\n        [b]Некто: ", end="")
            print("[grey35]эй сдесь есть кто нибуть?\n\n\n[bold][light_sky_blue1]          > Я сдесь[default]       Иди нахуй")
            Sel1 = 1
        elif keyboard.is_pressed('e') and Sel1 == 1:
            time.sleep(0.1)
            clear()
            Var1()
            break
        elif keyboard.is_pressed('e') and Sel1 == 2:
            time.sleep(0.1)
            clear()
            Var2()
            break