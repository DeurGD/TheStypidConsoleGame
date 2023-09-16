import time
from rich import print
import keyboard
import os
import Harter_1.Some1 # это такой тупой импорт из за бага

clear = lambda: os.system('cls')

MenuSelect = 1

clear()
print("\n\n                       [red bold]ВНИМАНИЕ!!!\n")
print("Это просто тупая консольная игра, думаю дисклеймер к ней не нужен.\n         Переключатся на \"w, s, a, d\" выбрать \"e\"")
time.sleep(8)

clear()
time.sleep(0.1)
print("\n\n       [grey74 bold]The[bold light_goldenrod1]Stypid[bold deep_pink1]Console[bold violet]Game\n\n[chartreuse1]          > Новая игра\n[pale_turquoise1]            Продолжить\n[pale_turquoise1]            Настройки")
while True:
    time.sleep(0.1) # это чтобы как бы цикл работал с задержкой и небыло бага + нагрева компа, попрошу тебя делать так же
    if keyboard.is_pressed('s') and MenuSelect == 1:
        time.sleep(0.1)
        clear()
        print("\n\n       [grey74 bold]The[bold light_goldenrod1]Stypid[bold deep_pink1]Console[bold violet]Game\n\n[pale_turquoise1]            Новая игра\n[chartreuse1]          > Продолжить\n[pale_turquoise1]            Настройки")
        MenuSelect = 2
    elif keyboard.is_pressed('w') and MenuSelect == 2:
        time.sleep(0.1)
        clear()
        print("\n\n       [grey74 bold]The[bold light_goldenrod1]Stypid[bold deep_pink1]Console[bold violet]Game\n\n[chartreuse1]          > Новая игра\n[pale_turquoise1]            Продолжить\n[pale_turquoise1]            Настройки")
        MenuSelect = 1
    elif keyboard.is_pressed('s') and MenuSelect == 2:
        time.sleep(0.1)
        clear()
        print("\n\n       [grey74 bold]The[bold light_goldenrod1]Stypid[bold deep_pink1]Console[bold violet]Game\n\n[pale_turquoise1]            Новая игра\n[pale_turquoise1]            Продолжить\n[chartreuse1]          > Настройки")
        MenuSelect = 3
    elif keyboard.is_pressed('w') and MenuSelect == 3:
        time.sleep(0.1)
        clear()
        print("\n\n       [grey74 bold]The[bold light_goldenrod1]Stypid[bold deep_pink1]Console[bold violet]Game\n\n[pale_turquoise1]            Новая игра\n[chartreuse1]          > Продолжить\n[pale_turquoise1]            Настройки")
        MenuSelect = 2
    elif keyboard.is_pressed('e') and MenuSelect == 1:
        Harter_1.Some1.NewGame()
        break
    elif keyboard.is_pressed('e') and MenuSelect == 2:
        () # тут и ниже запуск настроек и продолжить лол
        break
    elif keyboard.is_pressed('e') and MenuSelect == 3:
        ()
        break