import configparser
import os.path
import tkinter as tk

class Config(object):
    global general_setting, style_setting, style
    def __init__(self):
        global general_settings
        settings_path = "settings/settings.ini"
        settings_exists = os.path.exists(settings_path)
        if settings_exists == True:

            print("Файл конфигуряции основных настроек найден")
            general_settings = configparser.ConfigParser()  # создаём объекта парсера
            general_settings.read(settings_path)  # читаем конфиг
            general_setting(self)
            style(self)
            Window()
        else:
            print("Проверьте существование файла")

    def style(self):
        global style_settings
        style_path = "settings/style.ini"
        style_exists = os.path.exists(style_path)
        if style_exists == True:
            print("Файл конфигуряции настроек стиля найден")
            style_settings = configparser.ConfigParser()
            style_settings.read(style_path)
            style_setting(self)
        else:
            print("Проверьте существование файла")


    def general_setting(self):
        global Debug, Height, Width
        Debug = general_settings["General"]["Debug"]
        Height = general_settings["General"]["Height"]
        Width = general_settings["General"]["Width"]
        print(Debug, Height,  Width)

    def style_setting(self):
        global Foreground_main, Background_main, Height_main, Width_main
        Foreground_main = style_settings["Label"]["Foreground_main"]
        Background_main = style_settings["Label"]["Background_main"]
        Height_main = style_settings["Label"]["Height_main"]
        Width_main = style_settings["Label"]["Width_main"]
        print(Foreground_main, Background_main)

class Window(Config):
    global text
    ##Основное окно
    def __init__(self):
        window_main = tk.Tk()
        text(self)
        window_main.mainloop()

    ##Текст
    def text(self):
        label = tk.Label(text="Python рулит!",
                         foreground=Foreground_main,
                         background=Background_main,
                         height=Height_main,
                         width=Width_main
                         )

        label.pack()

Config()