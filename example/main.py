from homunculusbotapi import HomuncBot
import gpt
import recognizer as rts
import pyautogui
import subprocess
import txt2sph as golos
import ctypes


ab = HomuncBot(golos.say, rts.recognize_speech, call_when_initialize=[golos.turn_on], greet='К вашим услугам')


@ab.activate(transmission=['привет'])
def greet():
    ab.tell('Приветствую тебя сердечно!')


@ab.activate(transmission=['смени раскладку на русский', 'сделай русскую раскладку', 'поставь русскую раскладку', 'переключи раскладку на русский'])
def change_ru():
    pyautogui.hotkey('win', 'space')  # сочетание клавиш для смены раскладки
    pyautogui.press('ru')
    ab.tell('Раскладка изменена на русский')


@ab.activate(transmission=["смени раскладку на английский", 'поставь английскую раскладку', 'сделай английскую раскладку', 'переключи раскладку на английский'])
def change_ru():
    pyautogui.hotkey('win', 'space')  # сочетание клавиш для смены раскладки
    pyautogui.press('en')
    ab.tell('Раскладка изменена на английский')


@ab.activate(transmission=["калькулятор", "открой калькулятор", "открыть калькулятор"])
def open_calc():
    subprocess.Popen(["calc.exe"])


@ab.activate(transmission=["меню", "пуск", "открой меню", "открой пуск", "меню пуск", "открыть меню", "пуск меню", "открыть пуск", "открыть меню пуск", "открой меню пуск"])
def open_windows_menu():
    pyautogui.hotkey('win')


@ab.activate(transmission=['дисковод открыть', 'открыть дисковод'])
def eject():
    ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
    ab.tell('Выдвигаю дисковод')


@ab.activate(transmission=['дисковод закрыть', 'закрыть дисковод'])
def close():
    ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door closed", None, 0, None)
    ab.tell('Задвигаю дисковод')


@ab.activate(transmission='ANY')
def aimode(prompt):
    if (prompt is not None) and (prompt != ''):
        ab.tell('Хм, дайте подумать...')
        ab.tell(gpt.generate(prompt))


ab.poll()
