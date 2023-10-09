import time
from rich import print
import keyboard
import os
import Harter_1.Harter1GamePlay1
import pickle

clear = lambda: os.system('cls')

clear()

MenuSelect = 1

def CheckUserAge():
    clear()
    try:
        UserAge = int(input("\n\n       Сколько тебе лет: "))
        if UserAge < 18:
            clear()
            print("[red bold]\n\n       Тебе нет 18, а эта игра строго 18+")
            time.sleep(3)
            CheckUserAge()
        elif UserAge > 100:
            clear()
            print("[red bold]\n\n       Староват ты для таких игр!")
            time.sleep(3)
            CheckUserAge()
        elif UserAge < -1 or 0:
            clear()
            print("[red bold]\n\n       ТЫ что нахуй, ебанутый????")
            time.sleep(3)
            CheckUserAge()
        else:
            with open('UserAge.sav', 'wb') as f:
                pickle.dump(UserAge, f)
    except ValueError:
        UserAge = None
        clear()
        print("\n\n       [pale_turquoise1]Цифрами пожалуйста!")
        time.sleep(2)
        CheckUserAge()

def CheckUserName():
    clear()
    UserName = input("\n\n       Твое имя: ")
    with open('UserName.sav', 'wb') as f:
        pickle.dump(UserName, f)

try:
    with open('UserAge.sav', 'rb') as f:
        UserAge = pickle.load(f)
except FileNotFoundError:
    CheckUserAge()

try:
    with open('UserName.sav', 'rb') as f:
        UserName = pickle.load(f)
except FileNotFoundError:
    CheckUserName()


with open('UserAge.sav', 'rb') as f:
        UserAge = pickle.load(f)
with open('UserName.sav', 'rb') as f:
        UserName = pickle.load(f)

clear()
time.sleep(0.1)
print("\n\n       [grey74 bold]The[bold light_goldenrod1]Stypid[bold deep_pink1]Console[bold violet]Game\n\n[light_slate_blue]          ➮ Новая игра\n[grey50]            Продолжить\n[grey50]            Настройки")
while True:
    time.sleep(0.1)
    if keyboard.is_pressed('s') and MenuSelect == 1:
        time.sleep(0.1)
        clear()
        print("\n\n       [grey74 bold]The[bold light_goldenrod1]Stypid[bold deep_pink1]Console[bold violet]Game\n\n[grey50]            Новая игра\n[light_slate_blue]          ➮ Продолжить\n[grey50]            Настройки")
        MenuSelect = 2
    elif keyboard.is_pressed('w') and MenuSelect == 2:
        time.sleep(0.1)
        clear()
        print("\n\n       [grey74 bold]The[bold light_goldenrod1]Stypid[bold deep_pink1]Console[bold violet]Game\n\n[light_slate_blue]          ➮ Новая игра\n[grey50]            Продолжить\n[grey50]            Настройки")
        MenuSelect = 1
    elif keyboard.is_pressed('s') and MenuSelect == 2:
        time.sleep(0.1)
        clear()
        print("\n\n       [grey74 bold]The[bold light_goldenrod1]Stypid[bold deep_pink1]Console[bold violet]Game\n\n[grey50]            Новая игра\n[grey50]            Продолжить\n[light_slate_blue]          ➮ Настройки")
        MenuSelect = 3
    elif keyboard.is_pressed('w') and MenuSelect == 3:
        time.sleep(0.1)
        clear()
        print("\n\n       [grey74 bold]The[bold light_goldenrod1]Stypid[bold deep_pink1]Console[bold violet]Game\n\n[grey50]            Новая игра\n[light_slate_blue]          ➮ Продолжить\n[grey50]            Настройки")
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