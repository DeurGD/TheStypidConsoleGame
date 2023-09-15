import time
from rich import print
import keyboard
import os

clear = lambda: os.system('cls')

Sel2 = 1

def Var1():
    clear()
    print("\n\n        [b dark_khaki]Бомж: ", end="")
    print("Нууу я всего лишь тебя спас, можешь не паниковать 🤗")
    time.sleep(2)
    clear()
    print("\n\n        [b dark_khaki]Бомж: ", end="")
    print("Нууу я всего лишь тебя спас, можешь не паниковать 🤗\n\n\n[bold][light_sky_blue1]    > Как это, ты меня спас? От кого?!?!")
    while True:
        time.sleep(0.1)
        if keyboard.is_pressed('e'):
            time.sleep(0.1)
            clear()
            break
    print("\n\n        [b dark_khaki]Бомж: ", end="")
    print("Ну вы там когда героином нахуячились, приехали менты..")
    time.sleep(5)
    clear()
    print("\n\n        [b dark_khaki]Бомж: ", end="")
    print("Твой друг в окно, ну и ебанулся прямо на меня")
    time.sleep(5)
    clear()
    print("\n\n        [b dark_khaki]Бомж: ", end="")
    print("Я подумал 'нехуя там мясо' и решил пойти к вам")
    time.sleep(5)
    clear()
    print("\n\n        [b dark_khaki]Бомж: ", end="")
    print("Побежал наперекор ментам, закрыл дверь в подьезд и прибежав к тебе увидел что ты уже овощ")
    time.sleep(6)
    clear()
    print("\n\n        [b dark_khaki]Бомж: ", end="")
    print("Пока менты ломали дверь я тебя спрятал в подвал подьезда")
    time.sleep(5)
    clear()
    print("\n\n        [b dark_khaki]Бомж: ", end="")
    print("Ну и вот мы тут, а менты еще там роются 😉")
    time.sleep(2)
    clear()
    print("\n\n        [b dark_khaki]Бомж: ", end="")
    print("Ну и вот мы тут, а менты еще там роются 😉\n\n\n[bold][light_sky_blue1]    > Ох.. Спасибо тебе")
    while True:
        time.sleep(0.1)
        if keyboard.is_pressed('e'):
            time.sleep(0.1)
            clear()
            break
    print("\n\n        [b dark_khaki]Бомж: ", end="")
    print("Да незачто, мне наоборот скучно было. Зато тепер ебать как весело 😂\n\n\n[bold][light_sky_blue1]    > Хех.. И что теперь делать будем?")
    while True:
        time.sleep(0.1)
        if keyboard.is_pressed('e'):
            time.sleep(0.1)
            clear()
            break
    print("\n\n        [b dark_khaki]Бомж: ", end="")
    print("Думаю просто сидеть и не рыпатся 😶\n\n\n[bold][light_sky_blue1]    > Раскажешь о себе? Каким хером ты докатился до такой жизни?")
    while True:
        time.sleep(0.1)
        if keyboard.is_pressed('e'):
            time.sleep(0.1)
            clear()
            break
    
def gamepl1():
    clear()
    time.sleep(1)
    print('\n\n     [grey35]однажды один человек нахуярился героином...')
    time.sleep(4)
    clear()
    print('\n\n     [grey35]этот человек.... ты...')
    time.sleep(4)
    clear()
    print('\n\n     [grey35]после приступа ты очнулся в непонятном подвале...')
    time.sleep(4)
    clear()
    print('\n\n     [grey35]и к тебе подошол какой-то грязный и бородатый бомж...')
    time.sleep(4)
    clear()
    
    
    print("\n\n        [b dark_khaki]Бомж: ", end="")
    print("Ну привет\n\n\n[bold][light_sky_blue1]    > Ты кто?[default]       Какого хуя?")
    
    while True:
        
        Sel2 = 1
        
        time.sleep(0.1)
        if keyboard.is_pressed('d'):
            time.sleep(0.1)
            clear()
            print("\n\n        [b dark_khaki]Бомж: ", end="")
            print("Ну привет\n\n\n[bold][default]      Ты кто?[light_sky_blue1]     > Какого хуя?")
            Sel2 = 2
        elif keyboard.is_pressed('a'):
            time.sleep(0.1)
            clear()
            print("\n\n        [b dark_khaki]Бомж: ", end="")
            print("Ну привет\n\n\n[bold][light_sky_blue1]    > Ты кто?[default]       Какого хуя?")
            Sel2 = 1
        elif keyboard.is_pressed('e') and Sel2 == 1:
            time.sleep(0.1)
            clear()
            Var1()
            break
        elif keyboard.is_pressed('e') and Sel2 == 2:
            time.sleep(0.1)
            clear()
            Var1()
            break
    
Var1()